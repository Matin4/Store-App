import tkinter as tk
from HomeView import HomeView
from SignIn import SignInView
from SignUp import SignUpView
from ttkbootstrap.constants import *
import ttkbootstrap as ttk

class View():
    def __init__(self):
        self.root = ttk.Window(themename="superhero")
        self.root.geometry("1200x600")
        self.root.title("TEST")

    def start_mainloop(self):
        self.root.mainloop()

# v = View()
# v.switch_frame("home")
# v.start_mainloop()
