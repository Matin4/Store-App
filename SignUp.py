import ttkbootstrap as ttk

class SignUpView(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place(x=0, y=0, relheight=1.0, relwidth=1.0)
        
        # Username
        self.username_label = ttk.Label(self, text="Username")
        self.username_label.grid(row=0, column=0, pady=10, padx=10)

        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(row=0, column=1, pady=10, padx=10)

        # Password
        self.password_label = ttk.Label(self, text="Password")
        self.password_label.grid(row=1, column=0, pady=10, padx=10)

        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, pady=10, padx=10)

        # Sign Up Button
        self.sign_up_button = ttk.Button(self, text="Sign Up")
        self.sign_up_button.grid(row=2, column=0, columnspan=3, pady=10)

        self.back_to_sign_in_link = ttk.Label(self, text="Back to sign in", foreground="blue", cursor="hand2")
        self.back_to_sign_in_link.grid(column=1, row=2, sticky="e")

        self.warning_label = None

    def push_widgets_down(self):
        for widget in self.winfo_children():
            info = widget.grid_info()
            widget.grid(row=info['row'] + 1, column=info['column'])

    def empty_field_error(self):
        self.display_warning("Username or password is empty")

    def username_exist_error(self):
        self.display_warning("Username already exists!")
    
    def sign_up_successful(self):
        self.username_entry.delete(0, ttk.END)
        self.password_entry.delete(0, ttk.END)

    def display_warning(self, warning_text):
        if self.warning_label == None:
            self.push_widgets_down()
            self.warning_label = ttk.Label(self,text=warning_text)
            self.warning_label.grid(column=1, row=0, pady=10, padx=10)
        else:
            self.warning_label.config(text=warning_text)

    def clear_entry_fields(self):
        self.username_entry.delete(0, ttk.END)
        self.password_entry.delete(0, ttk.END)