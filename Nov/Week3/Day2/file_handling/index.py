# print("hello from file_handling")
# file = open("students.txt", "x")
# file.close()
# print("student file created")

# open file
# file = open("students.txt", "r")
# print("file opened")
# file.close()


# file = open("students.txt", "r")
# info = file.read()
# print(info)
# file.close()

# # read each line
# file = open("students.txt","r")
# info = file.readlines()
# print(info)
# file.close()

# add text in same line
# file = open("students.txt","w")
# file.write("this is new line for student 4 ")
# file.write("this is new line for student 5 ")
# file.write("this is new line for student 6 ")
# file.write("this is new line for student 7 ")
# file.close()
# print("new student add")

# # add txt multiple lines
# file = open("students.txt","w")
# file.write("this is new line for student 4 \n")
# file.write("this is new line for student 5 \n")
# file.write("this is new line for student 6 \n")
# file.write("this is new line for student 7 \n")
# file.close()
# print("new student add")


# students= ["Student 1\n","Student 2\n","Student 3\n","Student 4\n"]
# file = open("students.txt","w")
# file.writelines(students)
# file.close()
# print("new txt add in ")


# students= ["Student 1\n","Student 2\n","Student 3\n","Student 4\n"]
# file = open("students.txt","a")
# file.writelines(students)
# file.close()
# print("new txt add in ")


# import os
# os.rename("students.txt", "students-rename.txt")
# print("rename succesfully")

# import os
# os.remove("students-rename.txt")
# print("delete succesfully")

# import os 
# file = os.path.exists("students.txt")
# if file:
#     print("file exit")
# else:
#     print("no exit")   

# import os
# size = os.path.getsize("students.txt")
# print(size)

# import os
# os.makedirs("student")
# print("directory created")

# import csv
# with open ("students.csv","w",newline="") as file:
#     wr= csv.writer(file)
#     wr.writerow(["Name","Age","Address"])
#     wr.writerow(["st1","89","ctc"])
#     wr.writerow(["st2","8","bbsr"])
#     wr.writerow(["st3","88","svn"])


# print("csv file craeted")   


# import csv
# with open ("student.csv","r") as file:
#     rd= csv.reader (file)
#     for i in rd:
#         print(i)


# import json
# student = {
#     "name":"student1",
#     "age":22,
#     "address":"bbsr"
# }   
# with open("students.json","w")  as file:
#     json.dump(student,file,indent=4)

# import json
# with open("students.json","r")  as file:
#     data = json.load(file)  
# print(data['name'])    