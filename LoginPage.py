from breezypythongui import EasyFrame
from tkinter.font import Font
import numpy as np

class Login(EasyFrame):
    """To create a login page for the game"""

    #Creating the main frame
    def __init__(self, title="CONNECT FOUR", resizable=False):
        super().__init__(title, resizable)

        #Creating a nested frame for the data panel
        helloPanel = self.addPanel(row=0, column=0, background="grey")
        WelcomeLabel = helloPanel.addLabel(text="CONNECT FOUR", row=0, column=0, columnspan=2, sticky="N")
        label1 = helloPanel.addLabel(text="SIGN UP", row=1, column=0, columnspan=2, sticky="N")
        dataPanel = self.addPanel(row=1, column=0)
        label2 = dataPanel.addLabel(text="Username of Player1", row=3, column=0)
        label3 = dataPanel.addLabel(text="Username of Player2", row=4, column=0)
        text1 = dataPanel.addTextField(text="", row=3, column=1, width=20)
        text2 = dataPanel.addTextField(text="", row=4, column=1, width=20)
        btPanel = self.addPanel(row=2, column=0, background="black")
        bt1 = btPanel.addButton(text="Start", row=0, column=0, columnspan=2)

        #FONT and COLOUR for welcome caption
        font = Font(family = "Courier New", size=20)
        WelcomeLabel["font"] = font
        WelcomeLabel["foreground"] = "blue"
        font1 = Font(family="Courier New", size=14)
        label1["font"] = font1
        bt1["font"] = font1

def main():
    Login().mainloop()

if __name__ == "__main__":
    main()
