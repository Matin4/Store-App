import tkinter as tk

class SignInView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relheight=1.0, relwidth=1.0)
        self.columnconfigure((0,1), weight=1)
        self.rowconfigure((0,1,2,3), weight=1)

        self.user_label = tk.Label(self, text="User")
        self.user_label.grid(column=0, row=0, pady=5, padx=5)
        self.password_label = tk.Label(self, text="Password")
        self.password_label.grid(column=0, row=1, pady=5, padx=5)

        self.user_entry = tk.Entry(self)
        self.user_entry.grid(column=1, row=0, pady=5, padx=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(column=1, row=1, pady=5, padx=5)

        self.sign_in_button = tk.Button(self, text="Sign In")
        self.sign_in_button.grid(column=1, row=3, pady=5, padx=5,sticky="w")
        
        self.no_account_text = tk.Label(self, text="Don't have an account?")
        self.no_account_text.grid(column=0, row=2, sticky="w")

        self.link_label = tk.Label(self, text="Sign up", fg="blue", cursor="hand2")
        self.link_label.grid(column=1, row=2, sticky="e")

        self.warning_label = None

    def on_enter(self, event):
        self.no_account_text.tag_config("signup_link", underline=1)
        self.no_account_text.config(cursor="hand2")

    def on_leave(self, event):
        self.no_account_text.tag_config("signup_link", underline=0)
        self.no_account_text.config(cursor="")

    def push_widgets_down(self):
        for widget in self.winfo_children():
            info = widget.grid_info()
            widget.grid(row=info['row'] + 1, column=info['column'])

    def user_does_not_exist_error(self):
        self.display_error("User does not exist!")

    def sign_in_unsuccessful_error(self):
        self.display_error("Incorrect information")

    def on_sign_up_success(self):
        self.display_error("Sign up successful!")
        self.password_entry.delete(0, tk.END)
        self.user_entry.delete(0, tk.END)

    def display_error(self, warning_text):
        if self.warning_label == None:
            self.push_widgets_down()
            self.warning_label = tk.Label(self,text=warning_text)
            self.warning_label.grid(column=1, row=0, pady=10, padx=10)
        else:
            self.warning_label.config(text=warning_text)
