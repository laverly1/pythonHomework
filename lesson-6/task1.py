def add_employee():
    with open("employees.txt", "a") as file:
        while True:
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            position = input("Enter Position: ")
            salary = input("Enter Salary: ")
            
            file.write(f"{emp_id}, {name}, {position}, {salary}\n")
            
            more = input("Do you want to add another employee? (yes/no): ").strip().lower()
            if more != "yes":
                break

def view_employees():
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
            if records:
                for record in records:
                    print(record.strip())
            else:
                print("No records found.")
    except FileNotFoundError:
        print("No records found.")

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    try:
        with open("employees.txt", "r") as file:
            for record in file:
                if record.startswith(emp_id + ","):
                    print("Employee Found:", record.strip())
                    return
            print("Employee not found.")
    except FileNotFoundError:
        print("No records found.")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    records = []
    found = False
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
        with open("employees.txt", "w") as file:
            for record in records:
                if record.startswith(emp_id + ","):
                    name = input("Enter new Name: ")
                    position = input("Enter new Position: ")
                    salary = input("Enter new Salary: ")
                    file.write(f"{emp_id}, {name}, {position}, {salary}\n")
                    found = True
                else:
                    file.write(record)
        if found:
            print("Employee record updated successfully.")
        else:
            print("Employee not found.")
    except FileNotFoundError:
        print("No records found.")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    records = []
    found = False
    try:
        with open("employees.txt", "r") as file:
            records = file.readlines()
        with open("employees.txt", "w") as file:
            for record in records:
                if record.startswith(emp_id + ","):
                    found = True
                else:
                    file.write(record)
        if found:
            print("Employee record deleted successfully.")
        else:
            print("Employee not found.")
    except FileNotFoundError:
        print("No records found.")

def menu():
    while True:
        print("\nMenu Options:")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
