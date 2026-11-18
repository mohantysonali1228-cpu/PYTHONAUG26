# Question 1 --College Information

#  college_name = input("Enter College Name: ")
# location = input("Enter Location: ")
# year = input("Enter Establishment Year: ")
# departments = input("Enter Number of Departments: ")

# with open("college_info.txt", "w") as file:

#     file.write("College Name: " + college_name + "\n")
#     file.write("Location: " + location + "\n")
#     file.write("Establishment Year: " + year + "\n")
#     file.write("Departments: " + departments + "\n")

# with open("college_info.txt", "r") as file:

#     data = file.read()
#     print("\nCollege Information:")
#     print(data)



# Question 2--Employee Records

# with open("employee_records.txt", "w") as file:

    # for i in range(5):

    #     print("\nEmployee", i + 1)

    #     emp_id = input("Enter Employee ID: ")
    #     name = input("Enter Employee Name: ")
#         department = input("Enter Department: ")
#         salary = input("Enter Monthly Salary: ")

#         file.write("Employee ID: " + emp_id + "\n")
#         file.write("Name: " + name + "\n")
#         file.write("Department: " + department + "\n")
#         file.write("Salary: " + salary + "\n")
#         file.write("-------------------\n")

# with open("employee_records.txt", "r") as file:

#     print("\nAll Employee Records:")
#     print(file.read())


# Question 3--Shopping List

# items = ["Rice", "Sugar", "Milk", "Oil", "Salt"]

# with open("shopping_list.txt", "w") as file:

#     for item in items:
#         file.write(item + "\n")

# with open("shopping_list.txt", "a") as file:

#     file.write("Tea\n")
#     file.write("Coffee\n")
#     file.write("Bread\n")

# with open("shopping_list.txt", "r") as file:

#     print("Shopping List:")
#     print(file.read())


# Question 4--Paragraph Analysis

# with open("article.txt", "w") as file:

#     file.write("Technology makes our life easier. ")
#     file.write("Python is a popular programming language.\n")
#     file.write("It is used in web development and AI.")

# with open("article.txt", "r") as file:

#     data = file.read()

#     characters = len(data)
#     words = len(data.split())
#     lines = len(data.splitlines())

#     print("Paragraph:")
#     print(data)

#     print("\nTotal Characters:", characters)
#     print("Total Words:", words)
#     print("Total Lines:", lines)


# Question 5--Search for a Product

# products = [
#     "Laptop",
#     "Mobile",
#     "Keyboard",
#     "Mouse",
#     "Monitor",
#     "Laptop",
#     "Printer",
#     "Mobile",
#     "Headphones",
#     "Tablet"
# ]

# with open("product_catalog.txt", "w") as file:

#     for product in products:
#         file.write(product + "\n")

# search = input("Enter Product Name: ")

# with open("product_catalog.txt", "r") as file:

#     data = file.read().splitlines()

#     count = data.count(search)

#     if count > 0:
#         print("Product Found!")
#         print("Product Appears:", count, "Times")

#     else:
#         print("Product Not Found!")


# Question 6-- Copy Notes

# with open("python_notes.txt", "w") as file:

#     file.write("Python is a programming language.\n")
#     file.write("Python supports OOP.\n")
#     file.write("Python is easy to learn.")

# with open("python_notes.txt", "r") as file:

#     data = file.read()

# with open("backup_notes.txt", "w") as file:

#     file.write(data)

# print("File Copied Successfully!")


# Question 7--File Management Menu

# import os

# while True:

    # print("\n-- FILE MANAGEMENT MENU --")

    # print("1. Create File")
    # print("2. Write File")
    # print("3. Read File")
    # print("4. Append File")
    # print("5. Rename File")
    # print("6. Delete File")
    # print("7. Exit")

    # choice = input("Enter Your Choice: ")

    # if choice == "1":

    #     with open("company_profile.txt", "x") as file:
    #         print("File Created Successfully!")

    # elif choice == "2":

    #     with open("company_profile.txt", "w") as file:

    #         name = input("Enter Company Name: ")
    #         location = input("Enter Location: ")

    #         file.write("Company Name: " + name + "\n")
    #         file.write("Location: " + location + "\n")

    #     print("Information Written Successfully!")

    # elif choice == "3":

    #     if os.path.exists("company_profile.txt"):

    #         with open("company_profile.txt", "r") as file:
    #             print(file.read())

    #     else:
    #         print("File Not Found!")

    # elif choice == "4":

    #     if os.path.exists("company_profile.txt"):

    #         with open("company_profile.txt", "a") as file:

    #             details = input("Enter New Company Details: ")

    #             file.write(details + "\n")

    #         print("Details Appended Successfully!")

    #     else:
    #         print("File Not Found!")

    # elif choice == "5":

    #     if os.path.exists("company_profile.txt"):

    #         os.rename("company_profile.txt", "business_profile.txt")

    #         print("File Renamed Successfully!")

    #     else:
    #         print("File Not Found!")

    # elif choice == "6":

    #     if os.path.exists("business_profile.txt"):

    #         os.remove("business_profile.txt")
    #         print("File Deleted Successfully!")

    #     elif os.path.exists("company_profile.txt"):

    #         os.remove("company_profile.txt")
    #         print("File Deleted Successfully!")

    #     else:
    #         print("File Not Found!")

    # elif choice == "7":

    #     print("Thank You!")
    #     break

    # else:

    #     print("Invalid Choice! Try Again.")


#  Question 8-- Examination Result

# name = input("Enter Student Name: ")
# roll = input("Enter Roll Number: ")

# marks = []

# for i in range(5):

#     mark = int(input("Enter Marks: "))
#     marks.append(mark)

# total = sum(marks)

# percentage = (total / 500) * 100

# if all(mark >= 33 for mark in marks):
#     result = "Pass"
# else:
#     result = "Fail"

# with open("exam_result.txt", "w") as file:

#     file.write("Student Name: " + name + "\n")
#     file.write("Roll Number: " + roll + "\n")
#     file.write("Marks: " + str(marks) + "\n")
#     file.write("Total Marks: " + str(total) + "\n")
#     file.write("Percentage: " + str(percentage) + "%\n")
#     file.write("Result: " + result + "\n")

# with open("exam_result.txt", "r") as file:

#     print("\nExamination Result:")
    # print(file.read())


#  Question 9--Product Inventory (CSV)

# import csv

# products = [
#     [101, "Laptop", "Electronics", 50000, 5],
#     [102, "Mouse", "Accessories", 500, 10],
#     [103, "Keyboard", "Accessories", 1000, 8],
#     [104, "Mobile", "Electronics", 20000, 6],
#     [105, "Monitor", "Electronics", 12000, 4]
# ]

# with open("inventory.csv", "w", newline="") as file:

#     writer = csv.writer(file)

#     writer.writerow(["ID", "Name", "Category", "Price", "Quantity"])

#     writer.writerows(products)

# with open("inventory.csv", "r") as file:

#     reader = csv.reader(file)

#     print("Product Inventory:")

#     for row in reader:
        # print(row)


#  Question 10--Hospital Patient Information (JSON)

# import json

# patient = {
#     "patient_id": 101,
#     "name": "sonali",
#     "age": 25,
#     "disease": "Fever",
#     "doctor_name": "Dr. Sharma"
# }

# with open("patient_info.json", "w") as file:

#     json.dump(patient, file, indent=4)

# with open("patient_info.json", "r") as file:

#     data = json.load(file)

#     print("Patient Information:")

#     for key, value in data.items():

#         print(key, ":", value)


# Question 11--Electricity Bill Calculation

# units = [120, 150, 200, 180, 250, 300, 100, 220, 170, 190]

# with open("electricity_units.txt", "w") as file:

#     for unit in units:

#         file.write(str(unit) + "\n")

# with open("electricity_units.txt", "r") as file:

#     data = file.readlines()

# units = []

# for line in data:

#     units.append(int(line.strip()))

# total = sum(units)

# highest = max(units)

# lowest = min(units)

# average = total / len(units)

# print("Total Units:", total)
# print("Highest Consumption:", highest)
# print("Lowest Consumption:", lowest)
# print("Average Consumption:", average)



# Question 12--- User Login System

username = input("Enter Username: ")
email = input("Enter Email: ")
password = input("Enter Password: ")

with open("account_details.txt", "w") as file:

    file.write(username + "\n")
    file.write(email + "\n")
    file.write(password + "\n")

print("\nRegistration Successful!")

login_username = input("\nEnter Login Username: ")
login_email = input("Enter Login Email: ")
login_password = input("Enter Login Password: ")

with open("account_details.txt", "r") as file:

    data = file.readlines()

saved_username = data[0].strip()
saved_email = data[1].strip()
saved_password = data[2].strip()

if (login_username == saved_username and
    login_email == saved_email and
    login_password == saved_password):

    print("\nLogin Successful!")

else:

    print("\nInvalid Credentials!")