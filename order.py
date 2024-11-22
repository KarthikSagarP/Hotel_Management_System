import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from decimal import Decimal
import datetime

class orders:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System - Orders")

        # Create a Treeview widget
        self.tree = ttk.Treeview(root, columns=("Customer ID", "Name", "Phone", "Order ID", "Order Date", "Total Amount"), show='headings')
        self.tree.heading("Customer ID", text="Customer ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Order ID", text="Order ID")
        self.tree.heading("Order Date", text="Order Date")
        self.tree.heading("Total Amount", text="Total Amount")

        # Set column widths
        self.tree.column("Customer ID", width=100)
        self.tree.column("Name", width=150)
        self.tree.column("Phone", width=100)
        self.tree.column("Order ID", width=100)
        self.tree.column("Order Date", width=150)
        self.tree.column("Total Amount", width=100)

        # Add a scrollbar
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.pack(side='right', fill='y')

        # Pack the Treeview widget
        self.tree.pack(expand=True, fill='both')

        # Load orders from the database
        self.orders()

    def orders(self):
        conn = None  # Initialize conn to None
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='C@pshe!1',
                database='hbms',
                auth_plugin='mysql_native_password'
            )
            con_cursor = conn.cursor()
            
            # Execute the JOIN query
            con_cursor.execute('''
                SELECT 
                    c.Ref,
                    c.Name,
                    c.Mobile,
                    o.OrderID,
                    o.OrderDate,
                    o.TotalAmount
                FROM 
                    customer c
                LEFT JOIN 
                    orders o ON c.Ref = o.CustomerRef
            ''')
            
            # Fetch all results
            results = con_cursor.fetchall()
            
            # Clear existing data in the Treeview
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Insert data into the Treeview
            for row in results:
                customer_id, customer_name, phone, order_id, order_date, total_amount = row
                # Format the order date and total amount for display
                order_date_str = order_date.strftime("%Y-%m-%d %H:%M") if order_date else "N/A"
                total_amount_str = f"${total_amount:.2f}" if total_amount is not None else "N/A"
                
                self.tree.insert("", tk.END, values=(customer_id, customer_name, phone, order_id, order_date_str, total_amount_str))
            
        except Exception as es:
            messagebox.showwarning('Warning', f'Something went wrong: {str(es)}', parent=self.root)
        
        finally:
            # Ensure the connection is closed
            if conn is not None and conn.is_connected():
                conn.close()

# Create the main application window
if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagementApp(root)
    root.mainloop()