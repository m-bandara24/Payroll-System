# payroll.py
import sqlite3
import tkinter as tk
from tkinter import messagebox
from employee import Employee
from vehicle import Vehicle

class Payroll:
    def __init__(self):
        self.employee_list = []
        self.conn = sqlite3.connect('payroll_system.db')
        self.cursor = self.conn.cursor()

    def add_employee(self, employee):
        self.employee_list.append(employee)
        self.cursor.execute('''
        INSERT INTO Employee (FirstName, LastName, employee_ID, Work_Type, Wage, Vehicle_Model, Vehicle_number) VALUES (?, ?, ?, ?,?,?,?)
        ''', (employee.get_first_name(), employee.get_last_name(), employee.get_employee_id(), employee.get_work_type(), employee.calculate_salary(), employee.vehicle_model, employee.vehicle_number))
        self.conn.commit()

    
    def remove_employee(self, employee_id): # Check if the employee ID exists in the database 
        self.cursor.execute('SELECT employee_ID FROM Employee WHERE employee_ID = ?', (employee_id,)) 
        result = self.cursor.fetchone() 
    
        if result is not None: # Employee ID exists 
            self.employee_list = [emp for emp in self.employee_list if emp.get_employee_id() != employee_id] 
            self.cursor.execute('DELETE FROM Employee WHERE employee_ID = ?', (employee_id,)) 
            self.conn.commit() 
            messagebox.showinfo("Success", "Employee removed successfully!") 
        else: # Employee ID does not exist 
            messagebox.showerror("Error", "Employee ID not found!!")
        self.conn.close()

    def update_employee(self, employee):        
        self.employee_list.append(employee)
        self.cursor.execute('UPDATE Employee SET Wage = ?, Vehicle_Model = ?, Vehicle_number=? WHERE employee_id = ?',
                       (employee.calculate_salary(), employee.vehicle_model, employee.vehicle_number, employee.get_employee_id()))
        self.conn.commit()
        messagebox.showinfo("Success", "Employee updated successfully!")
        
        self.conn.close()

    def display_all_employees(self):
        for emp in self.employee_list:
            print(emp.display_details())
