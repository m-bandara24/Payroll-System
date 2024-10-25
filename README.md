**Payroll System for London Packaging Company Limited**

📋 **Project Overview**

This project is a Payroll Management System built using Python with a Graphical User Interface (GUI) powered by tkinter. The system is designed to automate wage calculation and management for employees (full-time, part-time, and interns) while providing a user-friendly interface for adding, updating, removing, and viewing employee details. Additionally, it uses SQLite for storing employee data.

The system leverages object-oriented programming (OOP) principles, including encapsulation, inheritance, and polymorphism, ensuring modular and maintainable code.

✨ **Features**


Employee Types Supported:
  
  * Full-Time Employees: Monthly salary with an 18% income tax deduction
  
  * Part-Time Employees: Hourly wage with a 15% income tax deduction
  
  * Interns: Custom-defined salary structure (no tax deductions)
  
  * Vehicle Ownership Tracking: Assign vehicles to employees and track details.

Graphical User Interface (GUI):
  
 * Switchboard with separate windows for Add, Update, Remove, and View Employees.

Employee Management Operations:
  
  * Add new employees (full-time, part-time, or intern)
  
  * Update employee wage
  
  * Remove employees from the system
  
  * View all employee data in a table format

Data Storage:

  * SQLite database to persist employee records between sessions.
    
Error Handling:

  * Validation to prevent crashes and handle incorrect user inputs gracefully (e.g., invalid employee IDs).

🛠️ **Installation & Setup**


**Clone the Repository:**

```
git clone https://github.com/m-bandara24/payroll-system.git
cd payroll-system
```

**Install Required Dependencies:**

No external dependencies are required beyond Python's standard library. Ensure Python 3.x is installed:

```
python --version
```

**Run the Application:**

```
python main.py
```
📑 **OOP Principles Demonstrated**

* Encapsulation:

  The Employee class and its child classes encapsulate employee details and behavior.
* Inheritance:

  FullTimeEmployee, PartTimeEmployee, and Intern inherit from the Employee class.
* Polymorphism:

  Different types of employees (part-time, full-time, interns) calculate wages differently using overridden methods.
