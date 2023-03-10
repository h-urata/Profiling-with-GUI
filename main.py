import sys
import tkinter
import ctypes
import cProfile
import pstats
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox

# 解像度を上げる処理
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass


def ask_folder():
    """ 参照ボタンの動作"""
    typ = [('pyファイル', '*.py')]
    dir = 'C:'
    fle = filedialog.askopenfilename(filetypes=typ, initialdir=dir)
    folder_path.set(fle)


def app():
    """ 実行ボタンの動作"""
    input_dir = folder_path.get()
    profile(input_dir)

    # メッセージボックス
    messagebox.showinfo("完了", "完了しました。")

    sys.exit()


import cProfile
import pstats

def profile(file_path):
    # 外部のPythonファイルのコードを読み込み、グローバル変数を設定
    with open(file_path, encoding="utf-8") as f:
        code = compile(f.read(), file_path, 'exec')
    globals_dict = {'__file__': file_path}
    
    # プロファイリングを実行
    profiler = cProfile.Profile()
    profiler.runctx(code, globals_dict, {})
    
    # 結果を整形して返却
    stats = pstats.Stats(profiler)
    stats.sort_stats(pstats.SortKey.TIME)
    return stats.print_stats()



def delete_window():
    """xボタンの動作"""
    # 終了確認のメッセージ表示
    ret = messagebox.askyesno(
        title="終了確認",
        message="プログラムを終了しますか？")

    if ret == True:
        # 「はい」がクリックされたとき
        sys.exit()


# """"メインウィンドウ""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
main_win = tkinter.Tk()
main_win.title("Python高速化のすゝめ")
main_win.update_idletasks()
ww = main_win.winfo_screenwidth()
lw = 1000
wh = main_win.winfo_screenheight()
lh = 120
main_win.geometry(str(lw)+"x"+str(lh)+"+" +
                  str(int(ww/2-lw/2))+"+"+str(int(wh/2-lh/2)))

# メインフレーム
main_frm = ttk.Frame(main_win)
main_frm.grid(column=0, row=0, sticky=tkinter.NSEW, padx=5, pady=10)

# パラメータ
folder_path = tkinter.StringVar()

# ウィジェット（フォルダ名）
folder_label = ttk.Label(main_frm, text="フォルダ指定")
folder_box = ttk.Entry(main_frm, textvariable=folder_path)
folder_btn = ttk.Button(main_frm, text="参照", command=ask_folder)

# ウィジェット（実行ボタン）
app_btn = ttk.Button(main_frm, text="実行", command=app)

# ウィジェットの配置
folder_label.grid(column=0, row=0, pady=10)
folder_box.grid(column=1, row=0, sticky=tkinter.EW, padx=5)
folder_btn.grid(column=2, row=0)
app_btn.grid(column=1, row=2)

# 配置設定
main_win.columnconfigure(0, weight=1)
main_win.rowconfigure(0, weight=1)
main_frm.columnconfigure(1, weight=1)

# xボタン押された時の処理
main_win.protocol("WM_DELETE_WINDOW", delete_window)

# ルートウィンドウの非表示
# root = tkinter.Tk()
# root.withdraw()

main_win.mainloop()
# """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
