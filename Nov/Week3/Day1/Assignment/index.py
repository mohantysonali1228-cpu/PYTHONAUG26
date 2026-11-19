# 1. Create a function to check whether a number is even or odd.

def even_odd(n):
    if n % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

even_odd(10)


# 2. Create a function to find the largest of three numbers.

def largest(a, b, c):
    if a > b and a > c:
        print("Largest:", a)
    elif b > a and b > c:
        print("Largest:", b)
    else:
        print("Largest:", c)

largest(10, 50, 30)


# 3. Create a function to calculate factorial.

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    print("Factorial:", fact)

factorial(5)


# 4. Create a function to check whether a number is prime.

def check_prime(num):
    if num <= 1:
        return "Not Prime"

    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"

    return "Prime Number"

res = check_prime(7)
print(res)



# 5. Create a function to reverse a string.

def reverse_string(s):
    print(s[::-1])

reverse_string("Python")


# 6. Create a function to calculate the sum of all elements in a list.

def list_sum(numbers):
    sum = 0

    for i in numbers:
        sum = sum + i

    print("sum:", sum)

list_sum([10, 20, 30, 40, 50])



# 7. Create a calculator using separate functions for addition, subtraction, multiplication, and division.

def addition(a, b):
    print("Addition:", a + b)

def subtraction(a, b):
    print("Subtraction:", a - b)

def multiplication(a, b):
    print("Multiplication:", a * b)

def division(a, b):
    if b != 0:
        print("Division:", a / b)
    else:
        print("Cannot divide by zero")

addition(10, 5)
subtraction(10, 5)
multiplication(10, 5)
division(10, 5)


# 8. Create a function using `args` to calculate the sum of multiple numbers.

def total(*args):
    sum = 0

    for i in args:
        sum = sum + i

    print("Total:", sum)
total(10, 20, 30, 40, 50)


# 9. Create a function using `*kwargs` to display student details.

def student(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student(
    name="Sonali",
    age=22,
    course="MCA",
    college="GITAM"
)


# 10. Create a recursive function to calculate the Fibonacci sequence.

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i), end=" ")