class SignUpController():
    def __init__(self, model, view, app):
        self.model = model
        self.view_frame = view
        self.app = app
        self.bind()

    def bind(self):
        self.view_frame.sign_up_button.config(command=self.sign_up)

    def sign_up(self):
        user = self.view_frame.username_entry.get()
        password = self.view_frame.password_entry.get()
        if not user or not password:
            self.view_frame.empty_field_error()
        elif self.model.db.username_exist("users", user):
            self.view_frame.username_exist_error()
        else:
            self.model.db.insert_data("users", "username, password", (user, password))
            self.view_frame.sign_up_successful()
            self.app.view_frames["signin"].on_sign_up_success()
            self.app.show_view("signin")