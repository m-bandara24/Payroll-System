import tkinter as tk
from tkinter import messagebox
import sqlite3
from payroll_system import Payroll
from partTimeEmployee import PartTimeEmployee
from fullTimeEmployee import FullTimeEmployee
from internEmployee import Intern
from vehicle import Vehicle


class UpdateEmployee:
    def __init__(self, root):
        self.root = root
        self.root.title("Update Employee")
        
        self.payroll = Payroll()
            
        # Labels
        outer_frame = tk.LabelFrame(self.root, text="Update Employee Details", pady = 30,padx=30)
        lbl_empid = tk.Label(outer_frame, text = "Employee ID: ", anchor="w", width=30,pady=5)
        lbl_monthly_wage = tk.Label(outer_frame, text = "Employee New Monthly Wage(FT Only): ", anchor="w", width=30,pady=5)
        lbl_hours_worked = tk.Label(outer_frame, text="Hours Worked Updated(PT only): ", anchor="w", width=30,pady=5)
        lbl_hourly_rate = tk.Label(outer_frame, text="Hourly Rate Updated (PT only): ", anchor="w", width=30,pady=5)
        lbl_vehicle_model = tk.Label(outer_frame, text = "Employee New Vehicle Type (If any): ", anchor="w", width=30,pady=5)
        lbl_vehicle_number = tk.Label(outer_frame, text = "Employee New Vehicle Number: ", pady = 20, anchor="w", width=30)
        
        self.txt_empid = tk.Entry(outer_frame, width=50)
        self.txt_monthly_wage = tk.Entry(outer_frame, width=50)
        self.txt_hours_worked = tk.Entry(outer_frame, width=50)
        self.txt_hourly_rate = tk.Entry(outer_frame, width=50)
        self.txt_vehicle_model = tk.Entry(outer_frame, width=50)
        self.txt_vehicle_number = tk.Entry(outer_frame, width=50)
        
        # Submit Button
        self.submit_button = tk.Button(self.root, text="Update Employee", bg= "lightblue", command=self.update_employee)
        self.exit_button = tk.Button(self.root, text="Exit",  bg= "orange", command=self.exitFromThisWindow)
        
        outer_frame.grid(row=0, column=0)
        lbl_empid.grid(row=1,column=0)
        self.txt_empid.grid(row=1,column=2)
        lbl_monthly_wage.grid(row=2,column=0)
        self.txt_monthly_wage.grid(row=2,column=2)
        lbl_hours_worked.grid(row=3,column=0)
        self.txt_hours_worked.grid(row=3,column=2)
        lbl_hourly_rate.grid(row=4,column=0)
        self.txt_hourly_rate.grid(row=4,column=2)
        lbl_vehicle_model.grid(row=5,column=0)
        self.txt_vehicle_model.grid(row=5,column=2)
        lbl_vehicle_number.grid(row=6,column=0)
        self.txt_vehicle_number.grid(row=6,column=2)
        self.submit_button.grid(row=7, columnspan=2, pady=10)
        self.exit_button.grid(row=8,columnspan=2, pady=10)
    
    def update_employee(self):
        emp_id = self.txt_empid.get()
        new_vehicle_model = self.txt_vehicle_model.get()
        new_vehicle_number = self.txt_vehicle_number.get()
        vehicle = Vehicle(new_vehicle_model,new_vehicle_number)
        
         
        conn = sqlite3.connect('payroll_system.db')
        cursor = conn.cursor()
        cursor.execute('SELECT FirstName, LastName, Work_Type FROM Employee WHERE Employee_ID = ?', (emp_id,))
        result = cursor.fetchone()
        if result is not None:    
            first_name = result[0]
            last_name = result[1]
            work_type = result[2]
        else:
            messagebox.showerror("Error", "Employee ID not found!!")
        
        # create employee instances based on employee type
        if work_type.lower() == 'p':
            try:
                hours_worked = int(self.txt_hours_worked.get())
                hourly_rate = float(self.txt_hourly_rate.get())
                employee = PartTimeEmployee(first_name,last_name, emp_id, hourly_rate, hours_worked, vehicle)
                self.payroll.update_employee(employee)
                messagebox.showinfo("Success", "Employee updated successfully!")
                self.root.destroy()
            except ValueError:
                messagebox.showerror("Error", "Enter Numeric Values for rate/hours!")
                
        elif work_type.lower() == 'f':
            try:
                monthly_wage = float(self.txt_monthly_wage.get())
                employee = FullTimeEmployee(first_name,last_name, emp_id, monthly_wage, vehicle)
                self.payroll.update_employee(employee)
                messagebox.showinfo("Success", "Employee updated successfully!")
                self.root.destroy()
            except ValueError:
                messagebox.showerror("Error", "Enter Numeric Values for monthly wage!")
                
        elif work_type.lower() == 'i':  
            employee = Intern(first_name,last_name, emp_id, vehicle)
            self.payroll.update_employee(employee)
            messagebox.showinfo("Success", "Employee Updated successfully!")
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Enter F,P or I as Employee Type!")
            
    def exitFromThisWindow(self):
        self.root.destroy()
            
            
