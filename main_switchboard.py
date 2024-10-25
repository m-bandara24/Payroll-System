import tkinter as tk
from addEmployee import AddEmployee
from removeEmployee import RemoveEmployee
from updateEmployee import UpdateEmployee
from viewEmployee import ViewEmployees

class Switchboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Payroll System")
        # Style root
        self.root.geometry("300x300")
        self.root.configure(bg ="lightblue", cursor="hand2")
        
        # Add Employee button
        self.add_button = tk.Button(self.root, text="ADD", width=20, command=self.open_add_employee)
        self.add_button.pack(pady=10)
        
        # Remove Employee button
        self.remove_button = tk.Button(self.root, text="REMOVE", width=20, command=self.open_remove_employee)
        self.remove_button.pack(pady=10)
        
        # Update Employee button
        self.update_button = tk.Button(self.root, text="UPDATE", width=20, command=self.open_update_employee)
        self.update_button.pack(pady=10)

        # View Employees button
        self.view_button = tk.Button(self.root, text="VIEW EMPLOYEES", width=20, command=self.open_view_employees)
        self.view_button.pack(pady=10)
        
        # exit button
        self.exit_button = tk.Button(self.root, text="Exit", width=20, command=self.exitFromSwitchBoard)
        self.exit_button.pack(pady=10)
    
    def open_add_employee(self):
        add_window = tk.Toplevel(self.root)
        AddEmployee(add_window)
    
    def open_remove_employee(self):
        remove_window = tk.Toplevel(self.root)
        RemoveEmployee(remove_window)
    
    def open_update_employee(self):
        update_window = tk.Toplevel(self.root)
        UpdateEmployee(update_window)
    
    def open_view_employees(self):
        view_window = tk.Toplevel(self.root)
        ViewEmployees(view_window)
        
    def exitFromSwitchBoard(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Switchboard(root)
    root.mainloop()
