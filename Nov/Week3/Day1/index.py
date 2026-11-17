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


# Local scope, Global Scope
# msg="welcome to "
# def welcomeMsg():
#     print(msg)
# print(msg)      
# welcomeMsg()  

# print() -> Show something
# return -> keep the value 


# return
# def welcome():
#     return "welcome to python"
# res=welcome()
# print(res)




# 1 - Write a function with a arg, that return number is even or odd ?
def EvenOdd(number):
    if number % 2 ==0:
        return number ," is Even" 
    else:
        return number, " is Odd"

res = EvenOdd(100)
print(res)


# 2- Write a function that Take a List of numbers and return the largest number
def LargestNum(num):
    largest = num[0]
    
    for n in num:
        if n > largest:
            largest = n
    
    return largest        


numbers = [10,20,500,300,111,30,10]

print(LargestNum(numbers))


# 3 - Write a function that takes a List of numbers and return largest and smallest numbers

numbers = [10,20,500,300,111,30,10]
def LargestNum(num):
    largest = num[0]
    smallest = num[0]
    
    for n in num:
        if n > largest:
            largest = n
        if n < smallest:
            smallest = n
    
    return f"smallest - {smallest} , largest - {largest}"
print(LargestNum(numbers))


# 4 - Write a function that take a arg as age and return Voting eligibility 
# - Not Eligible
# - Just 18 
# - Eligible

def Voat(age):
    if age < 18:
        return "Not Eligibale..."
    elif age == 18:
        return "Just 18"
    else:
        return "Eligable"
    
print(Voat(18))         


# 5 - Write a function that takes mark and show grade
# Mark        Grade
# 90 - 100  -> A
# 80 - 89   -> B 
# 70 - 79   -> C 
# 60 - 69   -> C 
# 50 - 59   -> D 
# less the 50 -> Fail  

def GradeCalculater(mark):
    if mark >= 90:
        print("A") 
    elif mark >= 80:
        print("B") 
    elif mark >= 70:
        print("C") 
    elif mark >= 60:
        print("D") 
    elif mark >= 50:
        print("E") 
    else:
        print("Fail")
GradeCalculater(48)  


# 6 - Write a function that takes a number list and show the numbers are even or Odd
numbers = [10,11,530,320,111,30,10]

# 10 - "Even"
# 11 - "Odd"
# 530 - "Even"
# 320 - "Even"
# 111 - "Odd"
# 30 - "Even"
# 10 - "Odd"
numbers = [10,11,530,320,111,30,10]
def evenOdd(num):
    for i in num:
        if i % 2 == 0:
            print(i,"- Even")
        else:
            print(i,"- Odd")    

evenOdd(numbers)


# 7 - Write a function that takes a number List and show how manu even and odds are there
numbers = [10,11,530,320,111,30,10]
# Odd numbers are 2 and even numbers are 5
def EvenOddCount(nums):
        even = 0
        odd = 0
    
        for i in nums:
            if i % 2 == 0:
             even+=1
            else:
                odd+=1
                
        return f"Odd numbers are {odd} and even numbers are {even}"
    
print(EvenOddCount(numbers))    
     
# 8 - Write a function with n as arg, that show the multiplcation Table

# n = 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# .....
# 5 x 10 = 50


def MultiplactioTabel(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

MultiplactioTabel(7)
