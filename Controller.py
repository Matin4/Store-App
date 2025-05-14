from View import View
from Model import Model
from Controllers.SignInController import SignInController
from Controllers.SignUpController import SignUpController
from Controllers.HomeController import HomeController
from Views.HomeView import HomeView
from Views.SignIn import SignInView
from Views.SignUp import SignUpView
import tkinter as tk

class Controller():
    def __init__(self, model: Model, view: View):
        self.model = model
        self.root_view = view
        self.container = tk.Frame(self.root_view.root)
        self.container.pack(anchor="center")
        self.view_frames = {}
        self.controllers = {}
        self.show_view("signin")
        self.root_view.start_mainloop()
    
    def show_view(self, frame_name):
        if frame_name not in self.view_frames:
            if frame_name == "signin":
                view = SignInView(self.container)
                controller = SignInController(self.model, view, self)
            elif frame_name == "signup":
                view = SignUpView(self.container)
                controller = SignUpController(self.model, view, self)
            elif frame_name == "home":
                view = HomeView(self.container)
                controller = HomeController(self.model, view, self)

            self.view_frames[frame_name] = view
            self.controllers[frame_name] = controller
            view.grid(row=0, column=0, sticky="nsew")

        self.view_frames[frame_name].tkraise()