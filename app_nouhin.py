import pandas as pd
import tkinter as tk
import config
import common_utils
from tkinter import messagebox
from datetime import datetime
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Alignment
from copy import copy

def show_window(parent):
    """メニューから呼び出されるメインウィンドウ作成関数"""
    root = tk.Toplevel(parent)
    root.title("納品書に基づく売上内訳")
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

        file_name = f"納品書に基づく売上内訳_{dt['year']}年{dt['month']}月.xlsx"
        save_path = f"{dt['desktop_path']}/{file_name}"

        try:
            query = """
                SELECT  URH_DENDAT AS 日付
                       ,SUM(CASE WHEN SHO_KBN = 3 AND URM_SHOCD NOT IN ('806000', '806005', '807000') THEN URM_URIKIN ELSE 0 END) AS 商品
                       ,SUM(CASE WHEN URM_SHOCD = '806005' THEN URM_URIKIN ELSE 0 END) AS 荷造梱包費
                       ,SUM(CASE WHEN URM_SHOCD = '807000' THEN URM_URIKIN ELSE 0 END) AS 雑収入
                       ,SUM(CASE WHEN URM_SHOCD = '806000' THEN URM_URIKIN ELSE 0 END) AS 運賃
                       ,SUM(CASE WHEN SHO_KBN = 2 THEN URM_URIKIN ELSE 0 END) AS 製品
                       ,0 AS 売上合計
                       ,SUM(CASE WHEN URM_SHOCD = '805000' THEN URM_SURYO ELSE 0 END) AS TPH_数量
                       ,SUM(CASE WHEN URM_SHOCD = '805000' THEN URM_URIKIN ELSE 0 END) AS TPH_金額
                       ,SUM(CASE WHEN URM_SHOCD = '804001' THEN URM_SURYO ELSE 0 END) AS 電纜_数量
                       ,SUM(CASE WHEN URM_SHOCD = '804001' THEN URM_URIKIN ELSE 0 END) AS 電纜_金額
                FROM   T_URHDAT
                INNER JOIN T_URMDAT ON URH_KCODE = URM_KCODE AND URH_DENNO = URM_DENNO
                LEFT JOIN T_SHOMST ON URM_SHOCD = SHO_SHOCD
                WHERE  URH_DENDAT BETWEEN ? AND ?
                GROUP BY URH_DENDAT
                ORDER BY URH_DENDAT
            """

            conn = common_utils.get_db_connection()
            df = pd.read_sql(query, conn, params=[dt['start'], dt['end']])
            conn.close()

            if df.empty:
                messagebox.showinfo("結果", "該当するデータは見つかりませんでした。")
                return

            # Excel出力 (ヘッダーを2行にするため、データは後で装飾)
            with pd.ExcelWriter(save_path, engine='openpyxl') as writer:
                # startrow=1 とすることでExcelの2行目から書き出し（1行目は結合用）
                df.to_excel(writer, index=False, sheet_name=dt['sheet_name'], startrow=1)

            wb = load_workbook(save_path)
            ws = wb.active
            s = common_utils.get_excel_styles()
            center_align = Alignment(horizontal='center', vertical='center',wrap_text=True)

            # --- 1-2行目のタイトル・結合設定 ---
            # 2行目の個別ラベル（H2～K2）
            ws['H2'] = "数量"
            ws['I2'] = "金額"
            ws['J2'] = "数量"
            ws['K2'] = "金額"

            header_map = [
                ('A1:A2', '日付'), ('B1:B2', '商品売上'), 
                ('C1:C2', '荷造梱包費'), ('D1:D2', '雑収入\n（梱包破損補償等）'), # 追加
                ('E1:E2', '運賃'), ('F1:F2', '製品'), ('G1:G2', '売上合計'), 
                ('H1:I1', 'TPH8512RED'), ('J1:K1', '電纜ホース')
            ]
            for cell_range, title in header_map:
                ws.merge_cells(cell_range)
                top_left_cell = ws[cell_range.split(':')[0]]
                top_left_cell.value = title

           # --- 書式装飾 ---
            for i, col in enumerate(ws.iter_cols(min_row=1, max_col=ws.max_column), 1):
                col_letter = get_column_letter(i)
                for cell in col:
                    cell.border = s["border"]
                    
                    # 1-2行目（ヘッダー）の設定
                    if cell.row <= 2:
                        cell.fill = s["fill_header"]
                        cell.alignment = center_align
                        # D1セルだけサイズを9にする（コピーして再代入）
                        if cell.coordinate == "D1":
                            small_font = copy(s["font_bold"])
                            small_font.sz = 9
                            cell.font = small_font
                        else:
                            cell.font = s["font_bold"]
                    else:
                        # データ行の設定
                        cell.font = s["font"]
                        if i == 1:
                            cell.number_format = 'm"月"d"日"'
                        elif i >= 2:
                            cell.number_format = '#,##0'
                            if i == 7: # 売上合計 (B列～F列の合計)
                                cell.value = f"=SUM(B{cell.row}:F{cell.row})"
                
                # 列幅の指定
                if i == 1:
                    ws.column_dimensions[col_letter].width = 10
                elif i in [8, 10]:
                    ws.column_dimensions[col_letter].width = 8
                elif i in [9, 11]:
                    ws.column_dimensions[col_letter].width = 10
                else:
                    ws.column_dimensions[col_letter].width = 15

            # --- 合計行の追加 ---
            last_row = ws.max_row + 1
            ws.cell(row=last_row, column=1).value = "合計"
            for c in range(2, ws.max_column + 1):
                col_let = get_column_letter(c)
                target_cell = ws.cell(row=last_row, column=c)
                # データは3行目からなので SUM(X3:Xn)
                target_cell.value = f"=SUM({col_let}3:{col_let}{last_row-1})"
                target_cell.number_format = '#,##0'

            # 合計行のスタイル適用
            for c in range(1, ws.max_column + 1):
                cell = ws.cell(row=last_row, column=c)
                cell.border = s["border"]
                cell.fill = s["fill_total"]
                cell.font = s["font_bold"]

            # ウィンドウ枠固定（3行目からスクロール）
            ws.freeze_panes = 'A3'

            wb.save(save_path)
            messagebox.showinfo("完了", f"出力が完了しました。\n保存先: {save_path}")

        except PermissionError:
            messagebox.showerror("エラー", "Excelファイルが開いています。閉じてから再実行してください。")
        except Exception as e:
            messagebox.showerror("エラー", f"失敗しました:\n{e}")

    # --- GUIレイアウト ---
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

    btn = tk.Button(
        btn_frame, text="Excel出力", command=run_query,
        bg=config.GUI_BTN_COLOR, fg="white", font=("MS Gothic", 10, "bold"),
        width=12, height=1, relief="flat"
    )
    btn.grid(row=0, column=1, padx=5)

    btn_back = tk.Button(
        btn_frame, text="戻る", 
        command=on_closing, # 作成した閉じる処理を呼ぶ
        bg="#6c757d", fg="white", font=("MS Gothic", 10, "bold"),
        width=12, height=1, relief="flat"
    )
    btn_back.grid(row=0, column=0, padx=5)