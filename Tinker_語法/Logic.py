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