import tkinter as tk
from tkinter import messagebox
import sqlite3
from payroll_system import Payroll
from partTimeEmployee import PartTimeEmployee
from fullTimeEmployee import FullTimeEmployee
from internEmployee import Intern
from vehicle import Vehicle

class AddEmployee:
    def __init__(self, root):
        self.root = root
        self.root.title("Add Employee")

        self.payroll = Payroll()

        # Entry fields - labels
        lbl_instructions_1 = tk.Label(root, text = "Employee Type Details:", anchor="w", width=20)
        lbl_instructions_2 = tk.Label(root, text = "Type 'F' for Full-Time\nType 'P' for Part-Time\nType 'I' for Interns", justify="left", anchor="w", width=30)
        outer_frame = tk.LabelFrame(root, text="Employee Information Form", pady = 10,padx=30)
        lbl_firstname = tk.Label(outer_frame, text = "Employee First Name: ", anchor="w", pady = 20, width=30)
        lbl_lastname = tk.Label(outer_frame, text = "Employee Last Name: ", anchor="w", width=30)
        lbl_empid = tk.Label(outer_frame, text = "Employee ID: ", anchor="w",pady = 20, width=30)
        lbl_work_type = tk.Label(outer_frame, text = "Employee Type (F/P/I): ", anchor="w", width=30)
        lbl_monthly_wage = tk.Label(outer_frame, text = "Employee Monthly Wage (FT Only): ",pady = 20, anchor="w", width=30)
        lbl_hours_worked = tk.Label(outer_frame, text="Hours Worked (PT only): ", anchor="w", width=30)
        lbl_hourly_rate = tk.Label(outer_frame, text="Hourly Rate (PT only): ", anchor="w",pady = 20, width=30)
        lbl_vehicle_model = tk.Label(outer_frame, text = "Employee Vehicle Type (If any): ", anchor="w", width=30)
        lbl_vehicle_number = tk.Label(outer_frame, text = "Employee Vehicle Number: ", pady = 20, anchor="w", width=30)

        # entry fields - text area
        self.txt_firstname = tk.Entry(outer_frame, width=50)
        self.txt_lastname = tk.Entry(outer_frame, width=50)
        self.txt_empid = tk.Entry(outer_frame, width=50)
        self.txt_work_type = tk.Entry(outer_frame, width=50)
        self.txt_monthly_wage = tk.Entry(outer_frame, width=50)
        self.txt_hours_worked = tk.Entry(outer_frame, width=50)
        self.txt_hourly_rate = tk.Entry(outer_frame, width=50)
        self.txt_vehicle_model = tk.Entry(outer_frame, width=50)
        self.txt_vehicle_number = tk.Entry(outer_frame, width=50)
        

        # Submit Button
        self.btn_add_employee = tk.Button(self.root, text="Add Employee", bg= "lightblue", command=self.add_employee)
        self.btn_exit = tk.Button(self.root, text="Exit", bg="orange", command=self.exitFromThisWindow)
        # grid all the elements

        lbl_instructions_1.grid(row=0,column=0)
        lbl_instructions_2.grid(row=1,column=1)
        outer_frame.grid(row=2,column=0, columnspan=3)
        lbl_firstname.grid(row=2,column=0, columnspan=2)
        self.txt_firstname.grid(row=2,column=2)
        lbl_lastname.grid(row=3,column=0, columnspan=2)
        self.txt_lastname.grid(row=3,column=2)
        lbl_empid.grid(row=4,column=0, columnspan=2)
        self.txt_empid.grid(row=4,column=2)
        lbl_work_type.grid(row=5,column=0, columnspan=2)
        self.txt_work_type.grid(row=5,column=2)
        lbl_monthly_wage.grid(row=6,column=0, columnspan=2)
        self.txt_monthly_wage.grid(row=6,column=2)
        lbl_hours_worked.grid(row=7,column=0, columnspan=2)
        self.txt_hours_worked.grid(row=7,column=2)
        lbl_hourly_rate.grid(row=8,column=0, columnspan=2)
        self.txt_hourly_rate.grid(row=8,column=2)
        lbl_vehicle_model.grid(row=9,column=0, columnspan=2)
        self.txt_vehicle_model.grid(row=9,column=2)
        lbl_vehicle_number.grid(row=10,column=0, columnspan=2)
        self.txt_vehicle_number.grid(row=10,column=2)
        self.btn_add_employee.grid(row=11,columnspan=2, pady=10)
        self.btn_exit.grid(row=12,columnspan=2, pady=10)
        #mainloop
        root.mainloop()


    
    def add_employee(self):
        first_name = self.txt_firstname.get()
        last_name = self.txt_lastname.get()
        emp_id = self.txt_empid.get()
        work_type = self.txt_work_type.get()
        model = self.txt_vehicle_model.get()
        vehicle_number = self.txt_vehicle_number.get()
        vehicle = Vehicle(model,vehicle_number)
        
        
        # create employee instances based on employee type and call payroll class
        if work_type.lower() == 'p':
            try:
                hours_worked = int(self.txt_hours_worked.get())
                hourly_rate = float(self.txt_hourly_rate.get())
                employee = PartTimeEmployee(first_name,last_name, emp_id, hourly_rate, hours_worked, vehicle)
                self.payroll.add_employee(employee)
                messagebox.showinfo("Success", "Employee added successfully!")
                self.root.destroy()
                
            except ValueError:
                messagebox.showerror("Error", "Enter Numeric Values for rate/hours!")
                
        elif work_type.lower() == 'f':
            try:
                monthly_wage = float(self.txt_monthly_wage.get())
                employee = FullTimeEmployee(first_name,last_name, emp_id, monthly_wage, vehicle)
                self.payroll.add_employee(employee)
                messagebox.showinfo("Success", "Employee added successfully!")
                self.root.destroy()
            except ValueError:
                messagebox.showerror("Error", "Enter Numeric Values for monthly wage!")
                
        elif work_type.lower() == 'i':  
            employee = Intern(first_name,last_name, emp_id, vehicle)
            self.payroll.add_employee(employee)
            messagebox.showinfo("Success", "Employee added successfully!")
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Enter F,P or I as Employee Type!")
            
    def exitFromThisWindow(self):
        self.root.destroy()

        
