import pandas as pd
import tkinter as tk
import config
import common_utils
from tkinter import messagebox
from datetime import datetime
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

def show_window(parent):
    root = tk.Toplevel(parent)
    root.title("売掛金回収状況一覧")
    common_utils.center_window(root, 400, 220)
    root.configure(bg=config.GUI_BG_COLOR)

    def on_closing():
        parent.deiconify() # メニュー画面を再表示
        root.destroy()     # サブ画面を破棄

    root.protocol("WM_DELETE_WINDOW", on_closing) # ×ボタン対策

    def run_query():
        y_in = entry_year.get()
        m_in = entry_month.get()
        
        dt = common_utils.get_date_info(y_in, m_in)
        if not dt:
            messagebox.showwarning("入力エラー", "年と月を正しく入力してください")
            return

        conn = common_utils.get_db_connection()
        cursor = conn.cursor()

        file_name = f"売掛金回収状況一覧_{dt['year']}年{dt['month']}月.xlsx"
        save_path = f"{dt['desktop_path']}/{file_name}"

        try:
            # --- 1. 新規得意先の同期処理を追加 ---
            # T_TOKMSTにあってTable_2にないコードを、sort=9999でINSERT
            sync_query = """
                INSERT INTO Table_2 (code, sort, flag)
                SELECT TOK_TOKCD, 9999, 1
                FROM T_TOKMST
                WHERE NOT EXISTS (
                    SELECT 1 FROM Table_2 WHERE Table_2.code = T_TOKMST.TOK_TOKCD
                )
            """
            cursor.execute(sync_query)
            conn.commit() # 反映

             # --- 2. メインのデータ抽出 ---
            file_name = f"売掛金回収状況一覧_{dt['year']}年{dt['month']}月.xlsx"
            save_path = f"{dt['desktop_path']}/{file_name}"

            query = """
                SELECT TOK_SIMEBI AS 締日
                      ,CAST(code AS INT) AS コード
                      ,TOK_TOKNM1 AS 得意先名
                      ,NULL AS 区分
                      ,ISNULL(SEK_URIAGE, 0) + ISNULL(SEK_TAX, 0) AS 売上金額
                      ,NULL AS 入金額
                      ,NULL AS 備考
                      ,sort AS _sort_val
                FROM   Table_2
                LEFT JOIN T_TOKMST ON code = TOK_TOKCD
                LEFT JOIN (
                    SELECT SEK_SCODE, SEK_URIAGE, SEK_TAX, SES_SIMEDAT
                    FROM T_SESDAT
                    LEFT JOIN T_SEKDAT ON SES_KCODE = SEK_KCODE AND SES_SIMENO = SEK_SIMENO
                    LEFT JOIN T_TOKMST ON SEK_KCODE = TOK_KCODE AND SEK_SCODE = TOK_TOKCD
                    WHERE SES_SIMEDAT BETWEEN ? AND ?
                ) AS a ON code = SEK_SCODE
                WHERE (Table_2.flag = 1) 
                   OR (Table_2.flag = 0 AND (ISNULL(SEK_URIAGE, 0) + ISNULL(SEK_TAX, 0) <> 0))
                ORDER BY sort,code
            """

            df = pd.read_sql(query, conn, params=[dt['start'], dt['end']])
            conn.close()

            if df.empty:
                messagebox.showinfo("結果", "該当データはありませんでした。")
                return

            with pd.ExcelWriter(save_path, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name=dt['sheet_name'])

            wb = load_workbook(save_path)
            ws = wb.active
            s = common_utils.get_excel_styles()

            # 薄緑色のスタイル定義
            from openpyxl.styles import PatternFill
            fill_new = PatternFill(fgColor="E2EFDA", fill_type="solid") # 薄緑色
            sort_col_idx = ws.max_column  # 一番右の _sort_val 列

            for r_idx, row in enumerate(ws.iter_rows(min_row=1, max_row=ws.max_row), 1):
                # sortが9999かチェック
                is_new = (ws.cell(row=r_idx, column=sort_col_idx).value == 9999)

                for c_idx, cell in enumerate(row, 1):
                    cell.border = s["border"]
                    cell.font = s["font"]
                    if r_idx == 1:
                        cell.fill = s["fill_header"]
                        cell.font = s["font_bold"]
                    elif is_new:
                        cell.fill = fill_new # 新規行を薄緑にする

                    if c_idx in [5, 6] and r_idx > 1:
                        cell.number_format = '#,##0'

            # 判定用に使った最後の列(_sort_val)を削除
            ws.delete_cols(sort_col_idx)

            # --- 4. 【改修】列幅調整（削除後の列数で実行） ---
            for i in range(1, ws.max_column + 1):
                col_letter = get_column_letter(i)
                max_len = 0
                for cell in ws[col_letter]:
                    if cell.value:
                        val_len = len(str(cell.value).encode('utf-16-le')) // 2
                        if val_len > max_len: max_len = val_len
                
                if i in [5, 6, 7]:
                    ws.column_dimensions[col_letter].width = 13.5
                else:
                    ws.column_dimensions[col_letter].width = (max_len + 4) * 1.2

            dv = DataValidation(type="list", formula1='"でんさい,振込,相殺"', allow_blank=True)
            dv.add(f'D2:D{ws.max_row}')
            ws.add_data_validation(dv)
            ws.freeze_panes = 'A2'

            last_row = ws.max_row + 1
            ws.cell(row=last_row, column=3).value = "合計"
            sum_col = get_column_letter(5)
            ws.cell(row=last_row, column=5).value = f"=SUM({sum_col}2:{sum_col}{last_row-1})"
            ws.cell(row=last_row, column=5).number_format = '#,##0'

            for c in range(1, 8):
                cell = ws.cell(row=last_row, column=c)
                cell.border = s["border"]
                cell.fill = s["fill_total"]
                cell.font = s["font_bold"]

            wb.save(save_path)
            messagebox.showinfo("完了", f"出力完了:\n{save_path}")
        except PermissionError:
            messagebox.showerror("エラー", "Excelを閉じてから実行してください。")
        except Exception as e:
            messagebox.showerror("エラー", f"失敗しました:\n{e}")

    main_frame = tk.Frame(root, bg=config.GUI_BG_COLOR)
    main_frame.pack(expand=True)
    input_frame = tk.Frame(main_frame, bg=config.GUI_BG_COLOR)
    input_frame.pack(pady=10)

    tk.Label(input_frame, text="対象年月：", bg=config.GUI_BG_COLOR, font=("MS Gothic", 10)).grid(row=0, column=0, padx=(0, 5))
    
    entry_year = tk.Entry(input_frame, width=8, justify="center")
    entry_year.grid(row=0, column=1, padx=2)
    
    # 初期表示で現在の年をセット
    entry_year.insert(0, datetime.now().year)
    
    tk.Label(input_frame, text="年", bg=config.GUI_BG_COLOR).grid(row=0, column=2, padx=5)
    entry_month = tk.Entry(input_frame, width=5, justify="center")
    entry_month.grid(row=0, column=3, padx=2)
    
    # 初期表示で現在の月をセット
    entry_month.insert(0, datetime.now().month)
    
    tk.Label(input_frame, text="月", bg=config.GUI_BG_COLOR).grid(row=0, column=4, padx=5)

    # --- ボタンを一行にまとめるためのフレーム ---
    btn_frame = tk.Frame(main_frame, bg=config.GUI_BG_COLOR)
    btn_frame.pack(pady=(40, 0)) 

    # --- gridを使って左から順に配置 ---
    
    # 戻るボタン（一番左：0列目）
    btn_back = tk.Button(btn_frame, text="戻る", 
                         command=on_closing, 
                         bg="#6c757d", fg="white", font=("MS Gothic", 10, "bold"), 
                         width=12, height=1, relief="flat")
    btn_back.grid(row=0, column=0, padx=5)

    # 出力設定変更ボタン（中央：1列目）
    btn_setting = tk.Button(btn_frame, text="出力設定変更", 
                            command=lambda: show_setting_window(root),
                            bg="#5a6268", fg="white", font=("MS Gothic", 10, "bold"), 
                            width=12, height=1, relief="flat")
    btn_setting.grid(row=0, column=1, padx=5)

    # Excel出力ボタン（右：2列目）
    btn = tk.Button(btn_frame, text="Excel出力", command=run_query, 
                    bg=config.GUI_BTN_COLOR, fg="white", font=("MS Gothic", 10, "bold"), 
                    width=12, height=1, relief="flat")
    btn.grid(row=0, column=2, padx=5)

    def show_setting_window(parent_win):
        setting_win = tk.Toplevel(parent_win)
        setting_win.title("売掛金回収状況一覧（出力設定変更）")
        common_utils.center_window(setting_win, 450, 230)
        setting_win.configure(bg=config.GUI_BG_COLOR)

        # --- 1段目：コード入力エリア ---
        frame1 = tk.Frame(setting_win, bg=config.GUI_BG_COLOR)
        frame1.pack(pady=(20, 5), padx=20, fill="x")

        tk.Label(frame1, text="得意先コード:", bg=config.GUI_BG_COLOR).grid(row=0, column=0, padx=5)
        
        def validate_code(P):
            return len(P) <= 8 and (P == "" or P.isdigit())
        vcmd = (setting_win.register(validate_code), '%P')

        entry_code = tk.Entry(frame1, width=12, justify="center", validate="key", validatecommand=vcmd)
        entry_code.grid(row=0, column=1, padx=5)
        entry_code.focus_set()

        lbl_customer_name = tk.Label(frame1, text="", bg=config.GUI_BG_COLOR, font=("MS Gothic", 10, "bold"), fg="blue")
        lbl_customer_name.grid(row=0, column=2, padx=10)

        # --- 2段目：設定項目エリア（枠線で囲む） ---
        # タイトル（text）を空にすることで、純粋な罫線のみで囲います
        group_frame = tk.LabelFrame(setting_win, bg=config.GUI_BG_COLOR, padx=15, pady=15)
        group_frame.pack(pady=10, padx=25, fill="x")
        
        tk.Label(group_frame, text="表示順:", bg=config.GUI_BG_COLOR).grid(row=0, column=0, padx=5)
        entry_sort = tk.Entry(group_frame, width=10, justify="center")
        entry_sort.grid(row=0, column=1, padx=10)
        
        var_hide_if_zero = tk.BooleanVar()
        chk_hide = tk.Checkbutton(
            group_frame, text="売上金額が0の場合は表示しない", 
            variable=var_hide_if_zero, bg=config.GUI_BG_COLOR, activebackground=config.GUI_BG_COLOR
        )
        chk_hide.grid(row=0, column=2, padx=10)

        # --- 検索ロジック ---
        def on_enter(event):
            raw_code = entry_code.get()
            if not raw_code: return
            code_8 = raw_code.zfill(8)
            entry_code.delete(0, tk.END)
            entry_code.insert(0, code_8)

            conn = common_utils.get_db_connection()
            query = "SELECT TOK_TOKNM1, sort, flag FROM Table_2 LEFT JOIN T_TOKMST ON code = TOK_TOKCD WHERE code = ?"
            res = conn.execute(query, (code_8,)).fetchone()
            conn.close()

            if res:
                # 取得した値がタプル(配列)なので、添字[0]などで文字列・数値として取り出す
                cust_name = res[0] if res[0] else ""
                curr_sort = res[1]
                curr_flag = res[2]

                lbl_customer_name.config(text=cust_name)
                entry_sort.delete(0, tk.END)
                entry_sort.insert(0, str(curr_sort))
                var_hide_if_zero.set(True if curr_flag == 0 else False)
                
                entry_sort.focus_set()
                entry_sort.selection_range(0, tk.END)
            else:
                messagebox.showwarning("未登録", "得意先が見つかりません。")

        entry_code.bind("<Return>", on_enter)

        # --- 更新ロジック ---
        def update_settings():
            code = entry_code.get()
            new_sort_input = entry_sort.get()
            if not code or not new_sort_input.isdigit():
                messagebox.showerror("エラー", "入力内容を確認してください。")
                return

            new_sort = int(new_sort_input)
            new_flag = 0 if var_hide_if_zero.get() else 1
            
            conn = common_utils.get_db_connection()
            cursor = conn.cursor()
            try:
                # 最大値取得
                cursor.execute("SELECT ISNULL(MAX(sort), 0) FROM Table_2 WHERE sort < 9999")
                max_sort_res = cursor.fetchone()
                max_sort = max_sort_res[0] if max_sort_res else 0
                
                if new_sort != 9999 and new_sort > max_sort:
                    messagebox.showerror("入力エラー", f"表示順が大きすぎます。\n最大値は {max_sort} です。")
                    return

                cursor.execute("SELECT sort FROM Table_2 WHERE code = ?", (code,))
                old_sort_res = cursor.fetchone()
                if not old_sort_res: return
                old_sort = old_sort_res[0]

                if old_sort != new_sort:
                    if old_sort < 9999 and new_sort < 9999:
                        if old_sort < new_sort:
                            cursor.execute("UPDATE Table_2 SET sort = sort - 1 WHERE sort > ? AND sort <= ? AND sort < 9999", (old_sort, new_sort))
                        else:
                            cursor.execute("UPDATE Table_2 SET sort = sort + 1 WHERE sort >= ? AND sort < ? AND sort < 9999", (new_sort, old_sort))
                    elif old_sort == 9999 and new_sort <= max_sort:
                        cursor.execute("UPDATE Table_2 SET sort = sort + 1 WHERE sort >= ? AND sort < 9999", (new_sort,))
                    elif old_sort < 9999 and new_sort == 9999:
                        cursor.execute("UPDATE Table_2 SET sort = sort - 1 WHERE sort > ? AND sort < 9999", (old_sort,))

                cursor.execute("UPDATE Table_2 SET sort = ?, flag = ? WHERE code = ?", (new_sort, new_flag, code))
                conn.commit()
                
                messagebox.showinfo("完了", f"得意先コード: {code}\n設定を更新しました。")
                on_enter(None) 
                entry_code.focus_set()
                entry_code.selection_range(0, tk.END)
                
            except Exception as e:
                conn.rollback()
                messagebox.showerror("エラー", f"失敗しました: {e}")
            finally:
                conn.close()

        # --- 3段目：ボタンエリア（余白を多めにとる） ---
        btn_frame = tk.Frame(setting_win, bg=config.GUI_BG_COLOR)
        btn_frame.pack(pady=(40, 0))
               
        tk.Button(btn_frame, text="戻 る", command=setting_win.destroy, 
                bg="#6c757d", fg="white", font=("MS Gothic", 10, "bold"), width=12).grid(row=0, column=0, padx=10)
        
        tk.Button(btn_frame, text="クリア", command=lambda: [entry_code.delete(0, tk.END), entry_sort.delete(0, tk.END), lbl_customer_name.config(text=""), var_hide_if_zero.set(False), entry_code.focus_set()], 
                bg="#6c757d", fg="white", font=("MS Gothic", 10, "bold"), width=12).grid(row=0, column=1, padx=10)
        
        tk.Button(btn_frame, text="変 更", command=update_settings, 
                bg=config.GUI_BTN_COLOR, fg="white", font=("MS Gothic", 10, "bold"), width=12).grid(row=0, column=2, padx=10)
