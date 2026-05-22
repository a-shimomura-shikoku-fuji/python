import tkinter as tk
import config
import app_urikake
import app_nouhin
import app_juchushokai
import common_utils

def open_urikake():
    root.withdraw()
    app_urikake.show_window(root)

def open_nouhin():
    root.withdraw()
    app_nouhin.show_window(root)

def open_juchushokai():
    root.withdraw()
    app_juchushokai.show_window(root)

# メインメニュー画面
root = tk.Tk()
root.title("業務支援ツール")

# 共通関数で中央配置
common_utils.center_window(root, 350, 300)
root.configure(bg=config.GUI_BG_COLOR)

# --- 以下、ボタン等の配置（変更なし） ---
label = tk.Label(
    text="メインメニュー", # ラベルに文字がないと寂しいので追加
    bg=config.GUI_BG_COLOR, font=("游ゴシック", 12, "bold"), pady=20
)
label.pack()

btn1 = tk.Button(
    root, text="売掛金回収状況一覧", 
    command=open_urikake,
    bg=config.GUI_BTN_COLOR, fg="white", font=("游ゴシック", 10, "bold"),
    width=30, height=2, relief="flat"
)
btn1.pack(pady=10)

btn2 = tk.Button(
    root, text="納品書に基づく売上内訳", 
    command=open_nouhin,
    bg=config.GUI_BTN_COLOR, fg="white", font=("游ゴシック", 10, "bold"),
    width=30, height=2, relief="flat"
)
btn2.pack(pady=10)

btn3 = tk.Button(
    root, text="受注照会", 
    command=open_juchushokai,
    bg=config.GUI_BTN_COLOR, fg="white", font=("游ゴシック", 10, "bold"),
    width=30, height=2, relief="flat"
)
btn3.pack(pady=10)

root.mainloop()