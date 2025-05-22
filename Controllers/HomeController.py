from tkinter import messagebox
from validate import Validate
from Views.NewWindow import NewWindow
from ttkbootstrap.constants import *
import ttkbootstrap as ttk

class HomeController:
    def __init__(self, model, view, app):
        self.model = model
        self.view = view
        self.app = app
        self.validate = Validate()
        self.refresh_listbox_person()
        self.refresh_listbox_product()
        self.bind()
        self.view.signed_in_user_label.config(text=self.model.signed_in_user)
        self.view.signed_in_user_label.config(font=("Helvetica", 9, "bold"))

    def bind(self):
        self.view.signout_btn.config(command=self.signout)
        self.view.add_people_button.config(command=lambda: self.view.new_window(self, "Add Person"))
        self.view.add_product_button.config(command=lambda: self.view.new_window(self, "Add Product"))
        self.view.update_people_button.config(command=lambda: self.update_person())
        self.view.update_product_button.config(command=lambda: self.update_product())
        self.view.file_menu.add_command(label="Users", command=lambda: self.show_users())

    def add_contact(self):
        # Required fields
        name = self.view.window.name_entry.get()
        role = self.view.window.role_entry.get()

        if not name or not role:
            messagebox.showwarning("Missing Name", "Name and role are required to add a person.")
            return

        if not self.validate.validate_string(name):
            messagebox.showwarning("Missing Name", "Name is not correct!")
            return

        if not self.validate.validate_string(role):
            messagebox.showwarning("Missing Role", "Role is not correct!")
            return

        # Optional fields with validation if present
        lname = self.view.window.lname_entry.get()
        if lname and not self.validate.validate_string(lname):
            messagebox.showwarning("Invalid Last Name", "Last name is not correct!")
            return

        phone = self.view.window.phone_entry.get()
        if phone and not self.validate.validate_phone(phone):
            messagebox.showwarning("Invalid Phone", "Phone number is not correct!")
            return

        birthdate = self.view.window.birth_date_entry.entry.get()
        if birthdate and not self.validate.validate_date(birthdate):
            messagebox.showwarning("Invalid Birth Date", "Birth date is not correct!")
            return

        salary = self.view.window.salary_entry.get()
        if salary and not self.validate.validate_integer(salary):
            messagebox.showwarning("Invalid Salary", "Salary is not correct!")
            return

        # Insert into database
        self.model.db.insert_data(
            "People",
            "first_name, last_name, phone, birth_date, role, salary",
            (name, lname, phone, birthdate, role, salary)
        )

        self.view.close_top_window()
        self.refresh_listbox_person()

    def add_product(self):
        # Required fields
        name = self.view.window.pname_entry.get()
        if not self.validate.validate_string(name) or not name:
            messagebox.showwarning("Missing Name", "Name is not correct!")
            return

        # Optional fields with validation if present
        code = self.view.window.pcode_entry.get()
        if code and not self.validate.validate_integer(code):
            messagebox.showwarning("Invalide Code", "Code is not correct!")
            return
        
        buy_price = self.view.window.buy_price_entry.get()
        if buy_price and not self.validate.validate_float(buy_price):
            messagebox.showwarning("Invalid Buy", "Buy price is not correct!")
            return
        
        commercial_price = self.view.window.commercial_price_entry.get()
        if commercial_price and not self.validate.validate_float(commercial_price):
            messagebox.showwarning("Invalid Commercial price", "Commercial price is not correct!")
            return

        barcode = self.view.window.barcode_entry.get()
        if barcode and not self.validate.validate_integer(barcode):
            messagebox.showwarning("Invalid Barcode", "Barcode is not correct!")
            return

        quantity = self.view.window.quantity_entry.get()
        if quantity and not self.validate.validate_integer(quantity):
            messagebox.showwarning("Invalid quantity", "Quantity is not correct!")
            return

        self.model.db.insert_data(
            "Product",
            "name, code, buy_price, commercial_price, barcode, quantity",
            (name, code, buy_price, commercial_price, barcode, quantity)
        )

        self.view.close_top_window()
        self.refresh_listbox_product()

    def update_person(self):
        selected_item = self.view.personnel_table.selection()
        if selected_item:
            data = self.view.personnel_table.item(selected_item[0])["values"]
            col =  ["first_name", "last_name", "phone", "birth_date", "role", "salary"]
            if(self.model.db.record_exists("People", col, data)):
                conditions = {col: val for col, val in zip(col, data)}
                values = self.model.db.get_record("People", conditions)
                self.person_id = values[0]
                self.view.new_window(self, "Update person")
                self.view.window.name_entry.insert(0, data[0])
                self.view.window.lname_entry.insert(0, data[1])
                self.view.window.phone_entry.insert(0, data[2])
                self.view.window.birth_date_entry.entry.delete(0, "end")
                self.view.window.birth_date_entry.entry.insert(0, data[3])
                self.view.window.role_entry.insert(0, data[4])
                self.view.window.salary_entry.insert(0, data[5])
        else:
            messagebox.showwarning("No Selection", "Please select an item to update.")

    def update_product(self):
        selected_item = self.view.product_table.selection()
        if selected_item:
            data = self.view.product_table.item(selected_item[0])["values"]
            col =  ["name", "code", "buy_price", "commercial_price", "barcode", "quantity"]
            if(self.model.db.record_exists("Product", col, data)):
                conditions = {col: val for col, val in zip(col, data)}
                values = self.model.db.get_record("Product", conditions)
                self.product_id = values[0]
                self.view.new_window(self, "Update product")
                self.view.window.pname_entry.insert(0, data[0])
                self.view.window.pcode_entry.insert(0, data[1])
                self.view.window.buy_price_entry.insert(0, data[2])
                self.view.window.commercial_price_entry.insert(0, data[3])
                self.view.window.barcode_entry.insert(0, data[4])
                self.view.window.quantity_entry.insert(0, data[5])
        else:
            messagebox.showwarning("No Selection", "Please select an item to update.")

    def refresh_listbox_product(self):
        self.view.clear_list_box_product()
        for data in self.model.db.fetch_data("Product"):
            self.view.update_list_box_product(data)

    def refresh_listbox_person(self):
        self.view.clear_list_box_person()
        for data in self.model.db.fetch_data("People"):
            self.view.update_list_box_person(data)
    
    def save_changes_person(self):
        name = self.view.window.name_entry.get()
        role = self.view.window.role_entry.get()

        if not name or not role:
            messagebox.showwarning("Missing Name", "Name and role are required to add a person.")
            return

        if not self.validate.validate_string(name):
            messagebox.showwarning("Missing Name", "Name is not correct!")
            return

        if not self.validate.validate_string(role):
            messagebox.showwarning("Missing Role", "Role is not correct!")
            return

        # Optional fields with validation if present
        lname = self.view.window.lname_entry.get()
        if lname and not self.validate.validate_string(lname):
            messagebox.showwarning("Invalid Last Name", "Last name is not correct!")
            return

        phone = self.view.window.phone_entry.get()
        if phone and not self.validate.validate_phone(phone):
            messagebox.showwarning("Invalid Phone", "Phone number is not correct!")
            return

        birthdate = self.view.window.birth_date_entry.entry.get()
        if birthdate and not self.validate.validate_date(birthdate):
            messagebox.showwarning("Invalid Birth Date", "Birth date is not correct!")
            return

        salary = self.view.window.salary_entry.get()
        if salary and not self.validate.validate_integer(salary):
            messagebox.showwarning("Invalid Salary", "Salary is not correct!")
            return
        
        set_columns = "first_name, last_name, phone, birth_date, role, salary"
        values = (name, lname, phone, birthdate, role, salary)
        self.model.db.update_record("People", set_columns, self.person_id, values)
        self.view.close_top_window()
        self.refresh_listbox_person()

    def save_changes_product(self):
        name = self.view.window.pname_entry.get()
        if not self.validate.validate_string(name) or not name:
            messagebox.showwarning("Missing Name", "Name is not correct!")
            return

        # Optional fields with validation if present
        code = self.view.window.pcode_entry.get()
        if code and not self.validate.validate_integer(code):
            messagebox.showwarning("Invalide Code", "Code is not correct!")
            return
        
        buy_price = self.view.window.buy_price_entry.get()
        if buy_price and not self.validate.validate_float(buy_price):
            messagebox.showwarning("Invalid Buy", "Buy price is not correct!")
            return
        
        commercial_price = self.view.window.commercial_price_entry.get()
        if commercial_price and not self.validate.validate_float(commercial_price):
            messagebox.showwarning("Invalid Commercial price", "Commercial price is not correct!")
            return

        barcode = self.view.window.barcode_entry.get()
        if barcode and not self.validate.validate_integer(barcode):
            messagebox.showwarning("Invalid Barcode", "Barcode is not correct!")
            return

        quantity = self.view.window.quantity_entry.get()
        if quantity and not self.validate.validate_integer(quantity):
            messagebox.showwarning("Invalid quantity", "Quantity is not correct!")
            return
        
        set_columns = "name, code, buy_price, commercial_price, barcode, quantity"
        values = (name, code, buy_price, commercial_price, barcode, quantity)
        self.model.db.update_record("Product", set_columns, self.product_id, values)
        self.view.close_top_window()
        self.refresh_listbox_product()

    def signout(self):
        self.model.signed_in_user = None
        self.view.menu.destroy()
        self.view.winfo_toplevel().unbind("<Configure>")
        self.app.view_frames["home"].destroy()
        self.app.view_frames.pop("home")
        self.app.show_view("signin")
        
    def show_users(self):
        self.window = NewWindow(self, self.view, "roles")
        self.user_role_buttons = {}  # Dictionary to store menubuttons per user

        users = self.model.db.fetch_data("users")
        for i, user in enumerate(users):
            if user[1] != "admin":
                username = user[1]
                label = ttk.Label(self.window.roles_labels_frame, text=username)
                label.grid(row=i, column=0, padx=50, pady=10, sticky="nsew")

                role = self.model.db.get_user_role("users", username)
                menu_selection = ttk.Menubutton(self.window.roles_labels_frame, text=role, direction="below")
                menu_selection.grid(row=i, column=1, padx=50, pady=10, sticky="nsew")

                if self.model.signed_in_user != "admin":
                    menu_selection.configure(state="disabled")
        
                menu = ttk.Menu(menu_selection, tearoff=0)
                menu_selection.config(menu=menu)

                for opt in self.model.roles:
                    menu.add_command(
                        label=opt,
                        command=lambda o=opt, b=menu_selection: b.config(text=o)
                    )

                self.user_role_buttons[username] = menu_selection

        self.window.submit_btn.pack(anchor="s", expand=True, pady=10)
        self.window.submit_btn.config(command=self.update_roles)

    def update_roles(self):
        for username, menubutton in self.user_role_buttons.items():
            selected_role = menubutton.cget("text")
            self.model.db.set_user_role("users", username, selected_role)
        self.close_top_window()

    def close_top_window(self):
        if hasattr(self, 'window') and self.window.top_window.winfo_exists():
            self.window.top_window.destroy()
            del self.window
        