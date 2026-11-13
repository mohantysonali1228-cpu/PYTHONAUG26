# OPERATOR

# 1. add two numbers.
a = 10
b = 20
print(a+b)

# 2.calculate the remainder of two numbers.
a = 10
b = 3
print(a % b) 

# 3.calculate the square of a numbers.
num = 5
print(num**2)

# 4. to compare two numbers.
a = 20
b = 10
print(a > b)
print(a < b)
print(a == b)
print(a <= b)
print(a >= b)

# 5.check whether a number is between 10 and 50 using logical operators.
a = 25
if a >= 10 and a <= 50:
    print("Number is between 10 and 50")
else:
    print("Number is not between 10 and 50")



# Conditional Statements

# 1.to check whether a number is positive or negative.
i= 30
if i > 0:
    print("Positive number")
else:
    print("Negative number")

# 2.to check whether a number is even or odd. 
i=24
if i % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# 3.to check voting eligibility.
age = 18
if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting") 

# 4.to find the largest of two numbers. 
a = 10
b = 30
if a > b:
    print("Largest number:", a)
else:
    print("Largest number:", b)

# 5.to calculate grades based on marks.
marks = 80
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Fail")

# 6.to check whether a number is positive, negative, or zero.
num = 6
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 7.to create a simple calculator using if-elif-else.
a = 2
b = 5
op ="+"
if op == "+":
    print( a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print( a * b)
elif op == "/":
    print( a / b)    
else:
    print("Invalid operator") 


# Loops

# 1. Print numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i) 

# 2. Print numbers from 10 to 1 using a while loop.
i = 10
while i >= 1:
    print(i)
    i -= 1    

# 3. Print even numbers from 2 to 20.
for i in range(2, 21, 2):
    print(i)

# 4. Print odd numbers from 1 to 20.
for i in range(1, 21, 2):
    print(i)    

# 5. Print the multiplication table of any number.
num=8
for i in range(1, 11):
    print( num, "*", i, "=", num * i)

# 6. Print numbers from 5 to 25 with a step of 5.

for i in range(5, 26, 5):
    print(i)    

# 7. Print numbers in reverse order from 5 to 1.

for i in range(5,0,-1):
    print(i)


# 8. Calculate the sum of numbers from 1 to 10.

total=0
for i in range(1, 11):
    total = total+ i
print("sum=", total) 

# 9. Print the following pattern:
# 1
# 2
# 3
# 4
# 5

for i in range(1, 6):
    print(i)

# 10. Print the following star pattern using a for loop.

# *
# **
# ***
# ****
# *****   
for i  in range(1,6):
    print("*" * i)