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
        self.personnel_listbox = tk.Listbox(self.tab2, width=100)
        self.personnel_listbox.pack(fill="both", pady=5, padx=10)
        self.add_people_button = ttk.Button(self.tab2, text="Add")
        self.add_people_button.pack(side="left", padx=10, pady=20)
        self.update_people_button = ttk.Button(self.tab2, text="Update")
        self.update_people_button.pack(side="left", padx=10, pady=20)

        # Add Product Tab
        self.tab3 = ttk.Frame(self.main_window)
        self.main_window.add(self.tab3, text="Products")

        self.list_label_product = ttk.Label(self.tab3, text="Products")
        self.list_label_product.pack(pady=5)
        self.product_listbox = tk.Listbox(self.tab3, width=100)
        self.product_listbox.pack(fill="both", pady=5, padx=10)
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
        self.personnel_listbox.delete(0, ttk.END) 

    def update_list_box_person(self, data):
        self.personnel_listbox.insert(ttk.END, f"{data[0]}: {' | '.join(str(item) for item in data[1:])}")

    def clear_list_box_product(self):
        self.product_listbox.delete(0, ttk.END) 

    def update_list_box_product(self, data):
        self.product_listbox.insert(ttk.END, f"{data[0]}: {' | '.join(str(item) for item in data[1:])}")

    
