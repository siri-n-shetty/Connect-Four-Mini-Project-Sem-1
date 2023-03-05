import turtle
import time
from breezypythongui import EasyFrame
from tkinter.font import Font

class MyFrame(EasyFrame):
    def __init__(self):
        super().__init__("My Frame")
        # Create a turtle canvas
        self.canvas = self.addCanvas(row=0, column=0, columnspan=2)
        # Create and display the login page
        self.login_page = self.LoginPage(self, background="sky blue")
        self.login_page.grid(row=0, column=0)        

    class LoginPage(EasyFrame):
        def __init__(self, parent, background):
            super().__init__(parent, background="sky blue")
            self.parent = parent
            # Add GUI components and logic for the login form
            label1 = self.addLabel("Username of Player 1:", row=0, column=0)
            self.usernameField1 = self.addTextField(text="", row=0, column=1)

            label2 = self.addLabel("Username of Player 2:", row=1, column=0)
            self.usernameField2 = self.addTextField(text="", row=1, column=1)

            bt1 = self.submit_button = self.addButton(text="Start Game!", row=2, column=0, command=self.login)

            #Create a font object
            font = Font(family="Cambria", size=16)

            #Apply the font to the label
            label1["font"] = font
            label1["background"] = "sky blue"
            label2["font"] = font
            label2["background"] = "sky blue"

            bt1["font"] = font
            self.usernameField1.configure(font=font)
            self.usernameField2.configure(font=font)


        def login(self):
            # global username1
            # global username2
            # Validate the user input and authenticate the user
            username1 = self.usernameField1.getText()
            username2 = self.usernameField2.getText()
            if username1 != username2:               
                self.parent.play_game(username1, username2)
            else:
                self.addLabel(text="Please enter correct username", row=3, column=0)
            
    def play_game(self, username1, username2):
        import sys
        sys.path.append("D:\Python_Sem1")
        import test1

def main():
    # Create and display the frame
    frame = MyFrame()
    frame.mainloop()

if __name__ == "__main__":
    main()
