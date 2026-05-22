import os
import calendar
import pyodbc
from openpyxl.styles import Border, Side, Font, PatternFill
import config

def center_window(win, width, height):
    """ウィンドウを画面中央に配置し、サイズを固定する共通関数"""
    win.update_idletasks()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    
    win.geometry(f"{width}x{height}+{x}+{y}")

def get_date_info(year_val, month_val):
    """入力値から日付範囲、シート名、保存先を生成する"""
    try:
        y = int(year_val)
        m = int(month_val)
        m_str = str(m).zfill(2)
        _, last_day = calendar.monthrange(y, m)
        
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        
        return {
            "start": f"{y}-{m_str}-01",
            "end": f"{y}-{m_str}-{last_day}",
            "sheet_name": f"{y}年{m}月",
            "desktop_path": desktop,
            "year": y,
            "month": m
        }
    except ValueError:
        return None

def get_excel_styles():
    """共通のExcelスタイル一式を返す"""
    side = Side(style='thin', color='000000')
    return {
        "border": Border(top=side, bottom=side, left=side, right=side),
        "font": Font(name=config.FONT_NAME),
        "font_bold": Font(name=config.FONT_NAME, bold=True),
        "fill_header": PatternFill(start_color=config.BG_HEADER, end_color=config.BG_HEADER, fill_type='solid'),
        "fill_total": PatternFill(start_color=config.BG_TOTAL, end_color=config.BG_TOTAL, fill_type='solid')
    }

def get_db_connection():
    """データベースに接続する"""
    return pyodbc.connect(config.CONN_STR)