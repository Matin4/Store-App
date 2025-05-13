import tkinter as tk

class SignInController():
    def __init__(self, model, view, app):
        self.model = model
        self.view_frame = view
        self.app = app
        self.bind()

    def bind(self):
        self.view_frame.sign_in_button.config(command=self.login_check)
        self.view_frame.link_label.bind("<Button-1>", lambda e: self.on_sign_up())

    def login_check(self):
        user = self.view_frame.user_entry.get()
        password = self.view_frame.password_entry.get()
        
        if not self.model.username_exist(user):
            self.view_frame.user_does_not_exist_error()
        elif not self.model.user_exist(user, password):
            self.view_frame.sign_in_unsuccessful_error()
        else:
            self.app.show_view("home")

    def on_sign_up(self):
        if self.view_frame.warning_label != None:
            self.view_frame.warning_label.destroy()
            self.view_frame.warning_label = None
        self.view_frame.clear_entry_fields()
        self.app.show_view("signup")
