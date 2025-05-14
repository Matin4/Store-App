import ttkbootstrap as ttk

class SignUpView(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place(x=0, y=0, relheight=1.0, relwidth=1.0)
        
        self.warning_label = ttk.Label(self)
        self.warning_label.grid(columnspan=2, column=0, row=0, pady=10, padx=10)

        # Username
        self.username_label = ttk.Label(self, text="Username")
        self.username_label.grid(row=1, column=0, pady=5, padx=5)

        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(row=1, column=1, pady=5, padx=5)

        # Password
        self.password_label = ttk.Label(self, text="Password")
        self.password_label.grid(row=2, column=0, pady=5, padx=5)

        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.grid(row=2, column=1, pady=5, padx=5)

        # Back to Sign in link
        self.back_to_sign_in_link = ttk.Label(self, text="Back to sign in", foreground="blue", cursor="hand2")
        self.back_to_sign_in_link.grid(column=1, row=3, sticky="w")

        # Sign Up Button
        self.sign_up_button = ttk.Button(self, text="Sign Up")
        self.sign_up_button.grid(row=4, column=0, columnspan=3, pady=10)

    def empty_field_error(self):
        self.display_warning("Username or password is empty")

    def username_exist_error(self):
        self.display_warning("Username already exists!")

    def display_warning(self, warning_text):
        self.warning_label.config(text=warning_text)

    def clear_entry_fields(self):
        self.warning_label.config(text="")
        self.username_entry.delete(0, ttk.END)
        self.password_entry.delete(0, ttk.END)