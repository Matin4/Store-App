import ttkbootstrap as ttk

class SignInView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.warning_label = ttk.Label(self)
        self.warning_label.grid(columnspan=2, column=0, row=0, pady=10, padx=10)
        self.user_label = ttk.Label(self, text="User")
        self.user_label.grid(column=0, row=1, pady=5, padx=5)
        self.password_label = ttk.Label(self, text="Password")
        self.password_label.grid(column=0, row=2, pady=5, padx=5)

        self.user_entry = ttk.Entry(self, width=25)
        self.user_entry.grid(column=1, row=1, pady=5, padx=5)
        self.password_entry = ttk.Entry(self, width=25, show="*")
        self.password_entry.grid(column=1, row=2, pady=5, padx=5)

        self.no_account_text = ttk.Label(self, text="Don't have an account?")
        self.no_account_text.grid(column=1, row=3, sticky="w")

        self.link_label = ttk.Label(self, text="Sign up", foreground="blue", cursor="hand2")
        self.link_label.grid(column=1, row=3, sticky="e")

        self.sign_in_button = ttk.Button(self, text="Sign In")
        self.sign_in_button.grid(column=1, row=4, pady=5, padx=5,sticky="w")

    def user_does_not_exist_error(self):
        self.display_warning("User does not exist!")

    def sign_in_unsuccessful_error(self):
        self.display_warning("Incorrect information")

    def on_sign_up_success(self):
        self.clear_entry_fields()
        self.display_warning("Sign up successful!")

    def display_warning(self, warning_text):
        self.warning_label.config(text=warning_text)

    def clear_entry_fields(self):
        self.warning_label.config(text="")
        self.user_entry.delete(0, ttk.END)
        self.password_entry.delete(0, ttk.END)