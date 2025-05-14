import tkinter as tk
from Views.HomeView import HomeView
from Views.SignIn import SignInView
from Views.SignUp import SignUpView
from ttkbootstrap.constants import *
import ttkbootstrap as ttk

class View():
    def __init__(self):
        self.root = ttk.Window(themename="superhero")
        self.root.geometry("1200x600")
        self.root.title("Store App")

    def start_mainloop(self):
        self.root.mainloop()

# v = View()
# v.switch_frame("home")
# v.start_mainloop()
