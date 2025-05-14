from tkinter import messagebox
from validate import Validate

class HomeController:
    def __init__(self, model, view, app):
        self.model = model
        self.view = view
        self.app = app
        self.validate = Validate()
        self.bind()

    def bind(self):
        self.view.add_people_button.config(command=lambda: self.view.new_window_add_person(self))
        self.view.add_product_button.config(command=lambda: self.view.new_window_add_product(self))
        self.view.update_people_button.config(command=lambda: self.update_person())
        self.view.update_product_button.config(command=lambda: self.update_product())

    def add_contact(self):
        # Required fields
        name = self.view.name_entry.get()
        role = self.view.role_entry.get()

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
        lname = self.view.lname_entry.get()
        if lname and not self.validate.validate_string(lname):
            messagebox.showwarning("Invalid Last Name", "Last name is not correct!")
            return

        phone = self.view.phone_entry.get()
        if phone and not self.validate.validate_phone(phone):
            messagebox.showwarning("Invalid Phone", "Phone number is not correct!")
            return

        birthdate = self.view.birth_date_entry.entry.get()
        if birthdate and not self.validate.validate_date(birthdate):
            messagebox.showwarning("Invalid Birth Date", "Birth date is not correct!")
            return

        salary = self.view.salary_entry.get()
        if salary and not self.validate.validate_integer(salary):
            messagebox.showwarning("Invalid Salary", "Salary is not correct!")
            return

        # Insert into database
        self.model.db.insert_data(
            "People",
            "first_name, last_name, phone, birth_date, role, salary",
            (name, lname, phone, birthdate, role, salary)
        )

        self.view.close_top_window_person()
        self.refresh_listbox_person()

    def add_product(self):
        # Required fields
        name = self.view.product_window.pname_entry.get()
        if not self.validate.validate_string(name) or not name:
            messagebox.showwarning("Missing Name", "Name is not correct!")
            return

        # Optional fields with validation if present
        code = self.view.product_window.pcode_entry.get()
        if code and not self.validate.validate_integer(code):
            messagebox.showwarning("Invalide Code", "Code is not correct!")
            return
        
        buy_price = self.view.product_window.buy_price_entry.get()
        if buy_price and not self.validate.validate_float(buy_price):
            messagebox.showwarning("Invalid Buy", "Buy price is not correct!")
            return
        
        commercial_price = self.view.product_window.commercial_price_entry.get()
        if commercial_price and not self.validate.validate_float(commercial_price):
            messagebox.showwarning("Invalid Commercial price", "Commercial price is not correct!")
            return

        barcode = self.view.product_window.barcode_entry.get()
        if barcode and not self.validate.validate_integer(barcode):
            messagebox.showwarning("Invalid Barcode", "Barcode is not correct!")
            return

        quantity = self.view.product_window.quantity_entry.get()
        if quantity and not self.validate.validate_integer(quantity):
            messagebox.showwarning("Invalid quantity", "Quantity is not correct!")
            return

        # Insert into database
        self.model.db.insert_data(
            "Product",
            "name, code, buy_price, commercial_price, barcode, quantity",
            (name, code, buy_price, commercial_price, barcode, quantity)
        )

        self.view.close_top_window_product()
        self.refresh_listbox_product()

    def update_person(self):
        selected_item = self.view.personnel_listbox.curselection()
        if selected_item:
            pass

    def update_product(self):
        pass

    def refresh_listbox_product(self):
        self.view.clear_list_box_product()
        for data in self.model.db.fetch_data("Product"):
            self.view.update_list_box_product(data)

    def refresh_listbox_person(self):
        self.view.clear_list_box_person()
        for data in self.model.db.fetch_data("People"):
            self.view.update_list_box_person(data)