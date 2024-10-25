import tkinter as tk
from tkinter import ttk
import sqlite3

class ViewEmployees:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee List")
        
        # Style Treeview
        self.style = ttk.Style()
        self.style.theme_use('clam')
        #print(self.style.theme_names()) ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')        
        self.style.configure('Treeview.Heading', background="lightblue")
        
        # Create a Treeview widget
        self.tree = ttk.Treeview(self.root, columns=("First Name", "Last Name","Employee ID", "Work Type", "Wage", "Vehicle Model","Vehicle Number"), show='headings', height=20)
        self.tree.pack(padx=10, pady=10)

        # Define the column headings
        self.tree.heading("First Name", text="First Name", anchor=tk.W)
        self.tree.heading("Last Name", text="Last Name", anchor=tk.W)
        self.tree.heading("Employee ID", text="Employee ID", anchor=tk.W)
        self.tree.heading("Work Type", text="Work Type", anchor=tk.W)
        self.tree.heading("Wage", text="Wage/Salary", anchor=tk.W)
        self.tree.heading("Vehicle Model", text="Vehicle Model", anchor=tk.W)
        self.tree.heading("Vehicle Number", text="Vehicle Number", anchor=tk.W)

        # Set the column widths
        self.tree.column("First Name", width=100, anchor=tk.W)
        self.tree.column("Last Name", width=100, anchor=tk.W)
        self.tree.column("Employee ID", width=100, anchor=tk.W)
        self.tree.column("Work Type", width=100, anchor=tk.W)
        self.tree.column("Wage", width=100, anchor=tk.W)
        self.tree.column("Vehicle Model", width=100, anchor=tk.W)
        self.tree.column("Vehicle Number", width=100, anchor=tk.W)

        # Scrollbar for the Treeview
        self.scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.tree.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        
        # Fetch and display the employee data
        self.fetch_employee_data()
    
    def fetch_employee_data(self):
        conn = sqlite3.connect('payroll_system.db')
        cursor = conn.cursor()
        cursor.execute('SELECT FirstName, LastName, employee_ID,Work_Type, Wage, Vehicle_Model, Vehicle_number FROM Employee')
        employees = cursor.fetchall()

        # Insert the employee data into the Treeview
        for emp in employees:
            self.tree.insert("", tk.END, values=(emp[0], emp[1], emp[2], emp[3], round(emp[4]), emp[5], emp[6]))

        conn.close()
