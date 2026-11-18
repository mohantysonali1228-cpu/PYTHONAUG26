def search_department(employees, department):

    found = False

    for emp in employees:

        if emp["department"].lower() == department.lower():

            print(emp["name"], "-", emp["salary"])
            found = True

    if not found:
        print("No employee found in this department")


def highest_paid_employee(employees):

    highest = employees[0]

    for emp in employees:

        if emp["salary"] > highest["salary"]:
            highest = emp

    print("\nHighest Paid Employee:")
    print("Name:", highest["name"])
    print("Department:", highest["department"])
    print("Monthly Salary:", highest["salary"])