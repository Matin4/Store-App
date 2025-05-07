import tkinter as tk
from tkinter import ttk

class HomeView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None
        self.main_window = ttk.Notebook(self)
        self.main_window.pack()#(relx=0, rely=0, relheight=1.0, relwidth=1.0)
        self.columnconfigure((0,1), weight=1)
        self.rowconfigure((0,1,2), weight=1)

        # Home Tab
        self.tab1 = ttk.Frame(self.main_window)
        self.main_window.add(self.tab1, text="Home")
        self.label1 = tk.Label(self.tab1, text="Welcome to the GUI App!")
        self.label1.pack(pady=10, padx=10)

        # Add Person Tab
        self.tab2 = ttk.Frame(self.main_window)
        self.main_window.add(self.tab2, text="Personnel")

        self.list_label = tk.Label(self.tab2, text="Personnel and Customers")
        self.list_label.pack(pady=5)
        self.personnel_listbox = tk.Listbox(self.tab2, width=100)
        self.personnel_listbox.pack(fill="both", pady=5, padx=10)
        self.add_people_button = tk.Button(self.tab2, text="Add")
        self.add_people_button.pack(side="left", pady=20)
        self.update_people_button = tk.Button(self.tab2, text="Update")
        self.update_people_button.pack(side="left", pady=20)

        # Add Product Tab
        self.tab3 = ttk.Frame(self.main_window)
        self.main_window.add(self.tab3, text="Products")

        self.list_label_product = tk.Label(self.tab3, text="Products")
        self.list_label_product.pack(pady=5)
        self.product_listbox = tk.Listbox(self.tab3, width=100,background="red")
        self.product_listbox.pack(fill="both", pady=5, padx=10)
        self.add_product_button = tk.Button(self.tab3, text="Add")
        self.add_product_button.pack(side="left", pady=20)
        self.update_product_button = tk.Button(self.tab3, text="Update")
        self.update_product_button.pack(side="left", pady=20)

    def new_window_add_product(self, controller):
        if hasattr(self, 'top_window_product'):
            self.top_window_product.lift()
            return
        
        self.top_window_product = tk.Toplevel()
        self.top_window_product.title("Popup Window")
        self.top_window_product.geometry("400x300")
        self.top_window_product.grab_set()
        self.top_window_product.protocol("WM_DELETE_WINDOW", self.close_top_window_product)
        self.controller = controller

         # Frames
        self.tab3_upper_frame = ttk.Frame(self.top_window_product)
        self.tab3_upper_frame.pack(side="top",expand=True, fill="both")
        self.tab3_lower_frame = ttk.Frame(self.top_window_product)
        self.tab3_lower_frame.pack(side="bottom",expand=True, fill="both")

        self.tab3_first_column = ttk.Frame(self.tab3_upper_frame)
        self.tab3_first_column.pack(side="left",expand=True, fill="both")
        self.tab3_second_column = ttk.Frame(self.tab3_upper_frame)
        self.tab3_second_column.pack(side="right",expand=True, fill="both")

        # Widgets
        self.pname_entry = tk.Entry(self.tab3_second_column, width=30)
        self.pname_entry.pack(expand=True, pady=5)
        self.pname_label = tk.Label(self.tab3_first_column, text="Product Name")
        self.pname_label.pack(expand=True, pady=5)  

        self.pcode_entry = tk.Entry(self.tab3_second_column, width=30)
        self.pcode_entry.pack(expand=True, pady=5)
        self.pcode_label = tk.Label(self.tab3_first_column, text="Product Code")
        self.pcode_label.pack(expand=True, pady=5)  

        self.buy_price_entry = tk.Entry(self.tab3_second_column, width=30)
        self.buy_price_entry.pack(expand=True, pady=5)
        self.buy_price_label = tk.Label(self.tab3_first_column, text="Buy Price")
        self.buy_price_label.pack(expand=True, pady=5)  

        self.commercial_price_entry = tk.Entry(self.tab3_second_column, width=30)
        self.commercial_price_entry.pack(expand=True, pady=5)
        self.commercial_price_label = tk.Label(self.tab3_first_column, text="Commercial Price")
        self.commercial_price_label.pack(expand=True, pady=5)

        self.barcode_entry = tk.Entry(self.tab3_second_column, width=30)
        self.barcode_entry.pack(expand=True, pady=5)
        self.barcode_label = tk.Label(self.tab3_first_column, text="Barcode")
        self.barcode_label.pack(expand=True, pady=5)

        self.quantity_entry = tk.Entry(self.tab3_second_column, width=30)
        self.quantity_entry.pack(expand=True, pady=5)
        self.quantity_label = tk.Label(self.tab3_first_column, text="Quantity")
        self.quantity_label.pack(expand=True, pady=5)  

        self.add_product_button = tk.Button(self.tab3_lower_frame, text="Add", command=self.controller.add_product)
        self.add_product_button.pack(expand=True, pady=5)

    def close_top_window_product(self):
        if hasattr(self, 'top_window_product') and self.top_window_product.winfo_exists():
            self.top_window_product.destroy()
            del self.top_window_product  # Remove the reference

    def new_window_add_person(self, controller):
        if hasattr(self, 'top_window_person'):
            self.top_window_person.lift()
            return
        
        self.top_window_person = tk.Toplevel()
        self.top_window_person.title("Popup Window")
        self.top_window_person.geometry("400x300")
        self.top_window_person.grab_set()
        self.top_window_person.protocol("WM_DELETE_WINDOW", self.close_top_window_person)
        self.controller = controller

        # Frames
        self.tab2_upper_frame = ttk.Frame(self.top_window_person)
        self.tab2_upper_frame.pack(side="top",expand=True, fill="both")
        self.tab2_lower_frame = ttk.Frame(self.top_window_person)
        self.tab2_lower_frame.pack(side="bottom",expand=True, fill="both")

        self.tab2_first_column = ttk.Frame(self.tab2_upper_frame)
        self.tab2_first_column.pack(side="left",expand=True, fill="both")
        self.tab2_second_column = ttk.Frame(self.tab2_upper_frame)
        self.tab2_second_column.pack(side="right",expand=True, fill="both")

        # Widgets
        self.name_entry = tk.Entry(self.tab2_second_column, width=30)
        self.name_entry.pack(expand=True, pady=5)
        tk.Label(self.tab2_first_column, text="First Name").pack(expand=True, pady=5)

        self.lname_entry = tk.Entry(self.tab2_second_column, width=30)
        self.lname_entry.pack(expand=True, pady=5)
        tk.Label(self.tab2_first_column, text="Last Name").pack(expand=True, pady=5)

        self.phone_entry = tk.Entry(self.tab2_second_column, width=30)
        self.phone_entry.pack(expand=True, pady=5)
        tk.Label(self.tab2_first_column, text="Phone").pack(expand=True, pady=5)

        self.birth_date_entry = tk.Entry(self.tab2_second_column, width=30)
        self.birth_date_entry.pack(expand=True, pady=5)
        tk.Label(self.tab2_first_column, text="Birth Date").pack(expand=True, pady=5)

        self.role_entry = tk.Entry(self.tab2_second_column, width=30)
        self.role_entry.pack(expand=True, pady=5)
        tk.Label(self.tab2_first_column, text="Role").pack(expand=True, pady=5)

        self.salary_entry = tk.Entry(self.tab2_second_column, width=30)
        self.salary_entry.pack(expand=True, pady=5)
        tk.Label(self.tab2_first_column, text="Salary").pack(expand=True, pady=5)

        self.add_button = tk.Button(self.tab2_lower_frame, text="Add Person", command=self.controller.add_contact)
        self.controller = None
        self.add_button.pack(expand=True)

    def close_top_window_person(self):
        if hasattr(self, 'top_window_person') and self.top_window_person.winfo_exists():
            self.top_window_person.destroy()
            del self.top_window_person  # Remove the reference

    def clear_list_box_person(self):
        self.personnel_listbox.delete(0, tk.END) 

    def update_list_box_person(self, data):
        self.personnel_listbox.insert(tk.END, f"{data[0]}: {' | '.join(str(item) for item in data[1:])}")

    def clear_list_box_product(self):
        self.product_listbox.delete(0, tk.END) 

    def update_list_box_product(self, data):
        self.product_listbox.insert(tk.END, f"{data[0]}: {' | '.join(str(item) for item in data[1:])}")

    def clear_inputs(self):
        self.name_entry.delete(0, tk.END)
        self.lname_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.birth_date_entry.delete(0, tk.END)
        self.role_entry.delete(0, tk.END) 
        self.salary_entry.delete(0, tk.END)

    
