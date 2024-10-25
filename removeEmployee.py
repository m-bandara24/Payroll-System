import tkinter as tk
from tkinter import messagebox
import sqlite3
from payroll_system import Payroll

class RemoveEmployee:
    def __init__(self, root):
        self.root = root
        self.root.title("Remove Employee")
        
        # Employee ID
        lbl_remove_empid = tk.Label(root, text = "Employee ID: ", pady = 20)
        self.txt_remove_empid = tk.Entry(root, width=30)
        
        lbl_remove_empid.grid(row=1,column=0)
        self.txt_remove_empid.grid(row=1,column=1, columnspan=2)
        
        self.payroll = Payroll()
        # Submit Button
        self.submit_button = tk.Button(self.root, text="Remove Employee",  bg= "lightblue", command=self.remove_employee)
        self.exit_button = tk.Button(self.root, text="Exit",  bg= "orange", command=self.exitFromThisWindow)
        self.submit_button.grid(row=3, columnspan=3, pady=10)
        self.exit_button.grid(row=4, columnspan=3, pady=10)
    
    
    def remove_employee(self):        
        emp_id = self.txt_remove_empid.get()
        self.payroll.remove_employee(emp_id)
        self.root.destroy()
        
    def exitFromThisWindow(self):
        self.root.destroy()
