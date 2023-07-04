import tkinter as tk
import os
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("starter")
#使windows圖標可以正確切換
# 獲取當前執行的python文件的絕對路徑
current_file_path = os.path.abspath(__file__)
# 獲取當前執行的python文件的所在目錄
current_directory = os.path.dirname(current_file_path)
print(current_directory)

class UI():
    def __init__(self) -> None:       
        self.root = tk.Tk()
        self.root.title("這是標題")
        self.root.geometry("1000x500")
        self.root.iconphoto(False, tk.PhotoImage(file=f'{current_directory}\\evicon.png'))
        self.f = tk.Frame(self.root)
        self.f.pack(side="top", fill='x')
        self.lblSysState = tk.Label(self.f, text="checking login state...")
        self.lblSysState.pack(side="left")
        self.btnLogin = tk.Button(self.f, text="login")
        self.btnLogin.pack(side="left")
    def run(self):
        print("父類隨後執行")
        self.btnLogin.config(command=self.login_button_clicked) #如果父類跟子類寫了一樣名稱的方法，則self.method會被子類覆蓋。
        self.root.mainloop()

    def login_button_clicked(self):
        print("Login button clicked in parent UI!")


