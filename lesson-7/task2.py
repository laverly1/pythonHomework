import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "w"):  # Create file if it doesn't exist
                pass

    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        
        with open(self.FILE_NAME, "a") as file:
            file.write(f"{emp_id},{name},{position},{salary}\n")
        print("Employee added successfully!\n")
    
    def view_employees(self):
        with open(self.FILE_NAME, "r") as file:
            employees = file.readlines()
        
        if not employees:
            print("No employee records found.\n")
            return
        
        print("Employee Records:")
        for emp in employees:
            print(emp.strip())
        print()
    
    def search_employee(self):
        emp_id = input("Enter Employee ID to search: ")
        with open(self.FILE_NAME, "r") as file:
            employees = file.readlines()
        
        for emp in employees:
            if emp.startswith(emp_id + ","):
                print("Employee Found:")
                print(emp.strip(), "\n")
                return
        print("Employee not found.\n")
    
    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ")
        with open(self.FILE_NAME, "r") as file:
            employees = file.readlines()
        
        updated_employees = []
        found = False
        
        for emp in employees:
            if emp.startswith(emp_id + ","):
                print("Current Record:", emp.strip())
                name = input("Enter New Name: ")
                position = input("Enter New Position: ")
                salary = input("Enter New Salary: ")
                updated_employees.append(f"{emp_id},{name},{position},{salary}\n")
                found = True
            else:
                updated_employees.append(emp)
        
        if found:
            with open(self.FILE_NAME, "w") as file:
                file.writelines(updated_employees)
            print("Employee record updated successfully!\n")
        else:
            print("Employee not found.\n")
    
    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ")
        with open(self.FILE_NAME, "r") as file:
            employees = file.readlines()
        
        updated_employees = [emp for emp in employees if not emp.startswith(emp_id + ",")]
        
        if len(updated_employees) == len(employees):
            print("Employee not found.\n")
            return
        
        with open(self.FILE_NAME, "w") as file:
            file.writelines(updated_employees)
        print("Employee record deleted successfully!\n")
    
    def menu(self):
        while True:
            print("Welcome to the Employee Records Manager!")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_employees()
            elif choice == "3":
                self.search_employee()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
