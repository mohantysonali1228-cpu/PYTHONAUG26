def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Monthly Salary: "))

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    return employee


def display_employee(employee):
    print("\nEmployee Details")
    print("Employee ID:", employee["id"])
    print("Employee Name:", employee["name"])
    print("Department:", employee["department"])
    print("Monthly Salary:", employee["salary"])