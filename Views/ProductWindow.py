from ttkbootstrap.constants import *
import ttkbootstrap as ttk

class ProductWindow:
    def __init__(self, controller, view):      
        self.top_window_product = ttk.Toplevel()
        self.top_window_product.title("Popup Window")
        self.top_window_product.geometry("400x300")
        self.top_window_product.grab_set()
        self.top_window_product.protocol("WM_DELETE_WINDOW", view.close_top_window_product)
        self.top_window_product.resizable(False, False)
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
        self.pname_entry = ttk.Entry(self.tab3_second_column, width=30)
        self.pname_entry.pack(expand=True, pady=5)
        self.pname_label = ttk.Label(self.tab3_first_column, text="Product Name")
        self.pname_label.pack(expand=True, pady=5)  

        self.pcode_entry = ttk.Entry(self.tab3_second_column, width=30)
        self.pcode_entry.pack(expand=True, pady=5)
        self.pcode_label = ttk.Label(self.tab3_first_column, text="Product Code")
        self.pcode_label.pack(expand=True, pady=5)  

        self.buy_price_entry = ttk.Entry(self.tab3_second_column, width=30)
        self.buy_price_entry.pack(expand=True, pady=5)
        self.buy_price_label = ttk.Label(self.tab3_first_column, text="Buy Price")
        self.buy_price_label.pack(expand=True, pady=5)  

        self.commercial_price_entry = ttk.Entry(self.tab3_second_column, width=30)
        self.commercial_price_entry.pack(expand=True, pady=5)
        self.commercial_price_label = ttk.Label(self.tab3_first_column, text="Commercial Price")
        self.commercial_price_label.pack(expand=True, pady=5)

        self.barcode_entry = ttk.Entry(self.tab3_second_column, width=30)
        self.barcode_entry.pack(expand=True, pady=5)
        self.barcode_label = ttk.Label(self.tab3_first_column, text="Barcode")
        self.barcode_label.pack(expand=True, pady=5)

        self.quantity_entry = ttk.Entry(self.tab3_second_column, width=30)
        self.quantity_entry.pack(expand=True, pady=5)
        self.quantity_label = ttk.Label(self.tab3_first_column, text="Quantity")
        self.quantity_label.pack(expand=True, pady=5)  

        self.add_product_button = ttk.Button(self.tab3_lower_frame, text="Add", command=self.controller.add_product)
        self.add_product_button.pack(expand=True, pady=5)