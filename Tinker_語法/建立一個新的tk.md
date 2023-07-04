建立一個新的tk
===
## Gui.py
```py
import tkinter as tk
import os

# 获取当前执行的 Python 文件的绝对路径
current_directory = os.getcwd()
print(current_directory)
class UI():
    def __init__(self) -> None:       
        self.root = tk.Tk()
        self.root.title("這是標題")
        self.root.geometry("1000x500")
        self.root.iconphoto(False, tk.PhotoImage(file=f'{current_directory}/evicon.png'))
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
```

## Logic.py
```py
from Gui import UI

class ChildUI(UI):
    def __init__(self) -> None:
        super().__init__()  #其實就是執行繼承過來的UI的__init__():

    def run(self):       
        self.btnLogin.config(command=super().login_button_clicked)
        self.lblSysState['text']="OK"
        self.lblSysState.config()
        print("子類優先")
        super().run()
        
        
    def login_button_clicked(self):
        super().login_button_clicked()
        print("Login button clicked in child UI!")
        # 在这里添加子类特定的逻辑

if __name__ == "__main__":
    child_ui = ChildUI()
    child_ui.run()
```