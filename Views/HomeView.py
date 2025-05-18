import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from Views.NewWindow import NewWindow

class HomeView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None
        self.columnconfigure((0,1), weight=1)
        self.rowconfigure((0,1,2), weight=1)
        height = self.winfo_toplevel().winfo_height()
        width = self.winfo_toplevel().winfo_width()
        self.main_window = ttk.Notebook(self, width=int(width*0.95), height=int(height*0.9))
        self.main_window.pack(anchor="center")
        self.winfo_toplevel().bind("<Configure>", self.on_resize_root_adjust_notebook)

        # Home Tab
        self.tab1 = ttk.Frame(self.main_window)
        self.main_window.add(self.tab1, text="Home")
        self.label1 = ttk.Label(self.tab1, text="Welcome to the GUI App!")
        self.label1.pack(pady=10, padx=10)

        # Add Person Tab
        self.tab2 = ttk.Frame(self.main_window)
        self.main_window.add(self.tab2, text="Personnel")

        self.list_label = ttk.Label(self.tab2, text="Personnel and Customers")
        self.list_label.pack(pady=5)
        self.personnel_table = ttk.Treeview(self.tab2, columns=("First Name", "Last Name", "Phone", "Birthdate", "Role", "Salary"), 
                                            show="headings", selectmode="browse")
        self.personnel_table.pack(fill="both", pady=5, padx=10)
        self.personnel_table.heading("First Name", text="First Name", anchor="w")
        self.personnel_table.heading("Last Name", text="Last Name", anchor="w")
        self.personnel_table.heading("Phone", text="Phone", anchor="w")
        self.personnel_table.heading("Birthdate", text="Birthdate", anchor="w")
        self.personnel_table.heading("Role", text="Role", anchor="w")
        self.personnel_table.heading("Salary", text="Salary", anchor="w")

        self.add_people_button = ttk.Button(self.tab2, text="Add")
        self.add_people_button.pack(side="left", padx=10, pady=20)
        self.update_people_button = ttk.Button(self.tab2, text="Update")
        self.update_people_button.pack(side="left", padx=10, pady=20)

        # Add Product Tab
        self.tab3 = ttk.Frame(self.main_window)
        self.main_window.add(self.tab3, text="Products")

        self.list_label_product = ttk.Label(self.tab3, text="Products")
        self.list_label_product.pack(pady=5)
        self.product_table = ttk.Treeview(self.tab3, columns=("Product Name", "Code", "Buy Price", "Commercial Price", "Barcode", "Quantity"), 
                                          show="headings", selectmode="browse")
        self.product_table.pack(fill="both", pady=5, padx=10)
        self.product_table.heading("Product Name", text="Product Name", anchor="w")
        self.product_table.heading("Code", text="Code", anchor="w")
        self.product_table.heading("Buy Price", text="Buy Price", anchor="w")
        self.product_table.heading("Commercial Price", text="Commercial Price", anchor="w")
        self.product_table.heading("Barcode", text="Barcode", anchor="w")
        self.product_table.heading("Quantity", text="Quantity", anchor="w")
        self.add_product_button = ttk.Button(self.tab3, text="Add")
        self.add_product_button.pack(side="left", padx=10, pady=20)
        self.update_product_button = ttk.Button(self.tab3, text="Update")
        self.update_product_button.pack(side="left", padx=10, pady=20)

    def on_resize_root_adjust_notebook(self, event):
        height = self.winfo_toplevel().winfo_height()
        width = self.winfo_toplevel().winfo_width()
        self.main_window.config(width=int(width*0.95), height=int(height*0.9))

    def new_window(self, controller, window_name):
        if hasattr(self, 'window'):
            self.window.top_window.lift()
            return
        
        self.window = NewWindow(controller, self, window_name)

    def close_top_window(self):
        if hasattr(self, 'window') and self.window.top_window.winfo_exists():
            self.window.top_window.destroy()
            del self.window  # Remove the reference

    def clear_list_box_person(self):
        for item in self.personnel_table.get_children():
            self.personnel_table.delete(item) 

    def update_list_box_person(self, data):
        data_to_insert = data[1:]
        self.personnel_table.insert(parent="", index=tk.END, values=data_to_insert)  

    def clear_list_box_product(self):
        for item in self.product_table.get_children():
            self.product_table.delete(item) 

    def update_list_box_product(self, data):
        data_to_insert = data[1:]
        self.product_table.insert(parent="", index=tk.END, values=data_to_insert) 

    
