# # List
# fruits=['Apple','mango','orange','fruit1']
# for i,fruit in enumerate (fruits):
#     print(i+1,"->",fruit)

# # tuple   
# fruits=('Apple','mango','orange','fruit1')
# for i,fruit in enumerate (fruits):
#     print(i+1,"->",fruit)

# # set
# fruits={'Apple','mango','orange','fruit1'}
# for i,fruit in enumerate (fruits):
#     print(i+1,"->",fruit)


# # dict
# student={
#     "name":"sonali","age":"21","city":"bbsr"
# }
# for key in student:
#     print(key)
# for key, val in student.items():
#     print(key,"is",val)



# function
# 1.simple function:
# def welcome():
#     print("welcome to python")
# welcome()    

# argument
# def welcome_with_name(name,age,city):
#     print("welcome",name)
#     print("age",age)
#     print("city",city)
# welcome_with_name("sona",21,"bbsr") 

# positional argument
# def welcome_with_name(name,age,city):
#     print("welcome",name)
#     print("age",age)
#     print("city",city)
# # keyword argument
# welcome_with_name(name="sona",age=21,city="bbsr") 

# defalut argument
# def welcome_with_name(name="defalut name",age=0,city="defalut city"):
#     print("welcome",name)
#     print("age",age)
#     print("city",city)
# welcome_with_name() 

# # variable length argument
# def showArgs(*numbers):
#     for i in numbers:
#         print(i)
# # numbers=[1,2,3,4]
# showArgs(10,20,30,40)

# msg="welcome to "
# def welcomeMsg():
#     print(msg)
# print(msg)    
# welcomeMsg() 


# return
# def welcome():
#     return "welcome to python"
# res=welcome()
# print(res)




#1. write a function with arg that return  number is even or odd ?
# def Evenodd(num):
#     if num %2 ==0:
#         return "number is even"
#     else:
#         return "number is odd"
# res=Evenodd(23)
# print(res)


# 2. find the largest number
# numer=[10,20,500,300,1100]


# def large_number():
#     large = number[0]

#     for i in number:
#         if i > large:
#             large = i

#     return large

# print("Largest number:", large_number())
    

#3. write of function that take a list of numbers and largest and smallest


numbers = [10, 20, 500, 300, 111,30,10]

# def large_smallnumbers(num):
#     largest = num[0]
#     smallest = num[0]

#     for n in num:
#         if n> largest:
#             largest = n

#         if n < smallest:
#             smallest = n

#     print("Large number:", largest)
#     print("Small number:", smallest)
# large_smallnumbers(numbers)



#4. voting eligibility

# def voat(age):
   
#         if age < 18:
#             return"not eligible"
#         elif age ==18 :
#             return "just 18"
#         else:
#             return "eligible"
     
# print(voat(5))          

# 5. mark

# def find_grade(marks):

#     if marks >= 90:
#         return "A+ Grade"

#     elif marks >= 80:
#         return "A Grade"

    # elif marks >= 70:
    #     return "B Grade"

    # elif marks >= 60:
    #     return "C Grade"

#     elif marks >= 50:
#         return "D Grade"

#     else:
#         return "Fail"

# num = int(input("Enter your marks: "))
# grade = find_grade(num)
# print("Your Grade is:", grade)
     

# 6. even or odd
# numbers=[10,11,530,320,111,30,10]
# 10 - "Even"
# 11 - "odd"
# 530 - ""
# 320
# 111
# numbers = [10, 11, 530, 320, 111, 30, 10]
# for i in numbers:
#     if i % 2 == 0:
#         print(i, "- Even")
#     else:
#         print(i, "-  Odd")


# 7- write a function that takes list and show how many even and odd are there
# numbers=[10,11,530,320,111,30,10]
# def count_even_odd(numbers):
#     even = 0
#     odd = 0
#     for i in numbers:
#         if i % 2 == 0:
#             even += 1
#         else:
#             odd += 1

#     print("Even numbers:", even)
#     print("Odd numbers:", odd)

# count_even_odd(numbers)       



# 8. write a function with n as arg, that show the multiplication table
def multiplication(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

num = int(input("Enter a number: "))
multiplication(num)