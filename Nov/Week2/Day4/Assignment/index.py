# List
# 1. Create a list of 10 numbers and print all elements using a for loop.

# numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# for i in numbers:
#     print(i)

# 2. Write a program to print only even and odd numbers from a list.

# numbers = [10, 15, 80, 25, 40, 75, 40, 35]
# for i in numbers:
#     if i % 2 == 0:
#         print(i, "- Even")
#     else:
#         print(i, "- Odd")

# 3.Find the largest and smallest numbers in a list using a loop.

# numbers = [10, 50, 20, 100, 5, 80]
# largest = numbers[0]
# smallest = numbers[0]
# for i in numbers:
#     if i > largest:
#         largest = i

#     elif i < smallest:
#         smallest = i
# print("largest number:", largest)
# print("smallest number:", smallest)

# 4.Count how many times a particular number appears in a list.
# numbers = [1, 2, 10, 3, 10, 4, 5]

# count = 0
# num=10
# for i in numbers:
#     if i == num:
#         count += 1

# print("Count:", count)

# 5.Write a function to calculate the sum of all elements in a list without using sum().
# numbers = [10, 15, 20, 25, 30]
# def calculate_sum(numbers):
#     sum = 0
#     for i in numbers:
#         sum += i

#     return sum
# res = calculate_sum(numbers)

# print("Sum:", res)

# 6.Find the second-largest number in a list without using sort() or max().
# numbers = [10, 20, 500, 300, 1100]

# largest = numbers[0]
# second_largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         second_largest = num

# print("Largest number:", largest)
# print("Second largest number:", second_largest)


# 7.Remove duplicate elements from a list without using set().
# numbers = [10, 20, 10, 30, 20, 40, 50]

# list= []
# for i in numbers:
#     if i not in list:
#         list.append(i)

# print(list)

# 8.Separate positive, negative and zero values into three different lists.

# numbers = [40, -5, 0, 10, -10, 0, 30, -2]

# positive = []
# negative = []
# zero = []

# for i in numbers:
#     if i > 0:
#         positive.append(i)

#     elif i < 0:
#         negative.append(i)

#     else:
#         zero.append(i)

# print("Positive:", positive)
# print("Negative:", negative)
# print("Zero:", zero)


# 9.Find the common elements between two lists without using intersection().
# list1 = [10, 20, 30, 40, 50]
# list2 = [30, 40, 50, 60, 70]

# common = []

# for i in list1:
#     if i in list2 and i not in common:
#         common.append(i)

# print("Common Elements:", common)

# 10.Write a function to check whether a list is a palindrome.
# numbers = [1, 2, 3, 2, 1]
# def check_palindrome(numbers):

#     if numbers == numbers[::-1]:
#         return "Palindrome"
#     else:
#         return "Not Palindrome"
# print(check_palindrome(numbers))

# Tuple

# 1.Create a tuple of 10 numbers and print all elements using a for loop.
# numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# for i in numbers:
#     print(i)

# 2.Print all elements along with their index using enumerate().
# numbers = (10, 20, 30, 40, 50)

# for index, value in enumerate(numbers):
#     print(index, value)

# 3.Find the largest and smallest numbers in a tuple using a loop.
# numbers = (10, 50, 20, 100, 5, 80)

# largest = numbers[0]
# smallest = numbers[0]

# for i in numbers:
#     if i > largest:
#         largest = i

#     if i < smallest:
#         smallest = i

# print("Largest:", largest)
# print("Smallest:", smallest)

# 4.Count how many times a particular number appears using count().
# numbers = (10, 20, 10, 30, 10, 40, 50)
# num = 10
# result = numbers.count(num)
# print("Count:", result)

# 5.Calculate the sum of all tuple elements without using sum().

# numbers = (10, 20, 30, 40, 50)
# sum = 0
# for i in numbers:
#     sum += i
# print("Sum:", sum)

# 6.Find the second-largest number in a tuple without using sort() or max().
# numbers = (10, 20, 500, 300, 1100)

# largest = numbers[0]
# second_largest = numbers[0]

# for num in numbers:
#     if num > largest:
#         second_largest = largest
#         largest = num

#     elif num > second_largest and num != largest:
#         second_largest = num

# print("Largest number:", largest)
# print("Second largest number:", second_largest)

# 7.Find all duplicate elements in a tuple.
# numbers = (10, 20, 30, 10, 40, 20, 50, 30)

# duplicates = []

# for i in numbers:
#     if numbers.count(i) > 1 and i not in duplicates:
#         duplicates.append(i)

# print("Duplicates:", duplicates)

# 8.Check whether a tuple is a palindrome without using slicing.
# numbers = (1, 2, 3, 2, 1)

# is_palindrome = True

# for i in range(len(numbers)):
#     if numbers[i] != numbers[len(numbers) - 1 - i]:
#         is_palindrome = False
#         break

# if is_palindrome:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# 9.Find the common elements between two tuples using loops.  
# tuple1 = (10, 20, 30, 40, 50)
# tuple2 = (30, 40, 50, 60, 70)

# common = []

# for i in tuple1:
#     if i in tuple2 and i not in common:
#         common.append(i)

# print("Common Elements:", common)

# 10.Separate even and odd numbers from a tuple into two different lists.
# numbers = (10, 15, 20, 25, 30, 35, 40, 45)

# even = []
# odd = []

# for i in numbers:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print("Even Numbers:", even)
# print("Odd Numbers:", odd)


# Set

# 1. Create a set of 10 numbers and print all elements using a for loop.
# numbers = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}

# for i in numbers:
#     print(i)
# 2. Create two sets and find their union.
# set_A = {10, 20, 30, 40}
# set_B = {30, 40, 50, 60}

# result = set_A.union(set_B)
# print("Union:", result)

# 3. Find the common elements between two sets using intersection().
# set_A = {10, 20, 30, 40, 50}
# set_B = {30, 40, 50, 60, 70}

# result = set_A.intersection(set_B)
# print("intersection:", result)

# 4. Find the difference between two sets using difference().
# set_A = {10, 20, 30, 40, 50}
# set_B = {30, 40, 50, 60, 70}
# result = set_A.difference(set_B)
# print("Difference:", result)

# 5. Find the largest and smallest numbers in a set using a loop.
# numbers = {10, 20, 500, 300, 1100}

# largest = None
# smallest = None

# for num in numbers:
#     if largest is None or num > largest:
#         largest = num

#     if smallest is None or num < smallest:
#         smallest = num

# print("Largest number:", largest)
# print("Smallest number:", smallest)

# 6. Find common elements between two sets without using intersection().
# set_A = {10, 20, 30, 40, 50}
# set_B = {30, 40, 50, 60, 70}

# common = set()
# for i in set_A:
#     if i in set_B:
#         common.add(i)
# print("Common Elements:", common)
# 7. Find the union of two sets without using union().

# set_A = {10, 20, 30, 40}
# set_B = {30, 40, 50, 60}

# result = set()
# for i in set_A:
#     result.add(i)
# for i in set_B:
#     result.add(i)
# print("Union:", result)
# 8. Check whether two sets are equal without using the == operator.
# set_A = {10, 20, 30, 40}
# set_B = {40, 30, 20, 10}

# if len(set_A) == len(set_B):
#     if set_A.issubset(set_B):
#         print("Both sets are equal")
#     else:
#         print("Both sets are not equal")
# else:
#     print("Both sets are not equal")
# 9. Find the elements that are present in exactly one of three sets.
# set1 = {10, 20, 30, 40}
# set2 = {20, 30, 50, 60}
# set3 = {30, 40, 70, 80}

# all_elements = set1.union(set2).union(set3)

# result = set()

# for i in all_elements:
#     count = 0

#     if i in set1:
#         count += 1

#     if i in set2:                    

#     if i in set3:
#         count += 1

#     if count == 1:
#         result.add(i)

# print("Exactly One Set:", result)

# 10. Find the common characters between two strings using sets.
# str1 = "python"
# str2 = "programming"
# set_A = set(str1)
# set_B = set(str2)
# common = set_A.intersection(set_B)
# print("Common Characters:", common)



# Dictionary

# 1. Create a dictionary containing 5 students and their marks. Print all keys and values using a loop.

# students = {
#     "Sonali": 35,
#     "Pratikshya": 75,
#     "elina": 90,
#     "Adyashree": 85,
#     "sweta": 60
# }
# for key, value in students.items():
#     print(key, value)

# 2. Add a new key called city to an existing dictionary.

# student = {
#     "name": "Sonali",
#     "age": 22,
#     "marks": 85
# }
# student["city"] = "BBSR"
# print(student)

# 3. Update the marks of a particular student.

# students = {
#     "Sonali": 35,
#     "Pratikshya": 75,
#     "elina": 90,
#     "Adyashree": 85,
#     "sweta": 60
# }
# students ["sweta"]=78
# print(students) 

# 4. Find the total marks of all students without using sum().
# students = {
#     "Sonali": 35,
#     "Pratikshya": 75,
#     "elina": 90,
#     "Adyashree": 85,
#     "sweta": 60
# }
# sum = 0
# for marks in students.values():
#     sum += marks
# print("Total Marks:", sum)

# 5. Count how many students passed and failed. Consider 40 as the passing mark.
# students = {
#     "Sonali": 35,
#     "Pratikshya": 75,
#     "elina": 90,
#     "Adyashree": 85,
#     "sweta": 60
# }

# passed = 0
# failed = 0
# for marks in students.values():
#     if marks >= 40:
#         passed += 1
#     else:
#         failed += 1
# print("Passed:", passed)
# print("Failed:", failed)

# 6. Find the student with the highest and lowest marks without using max() or min().
# students = {
#    "Sonali": 35,
#     "Pratikshya": 75,
#     "elina": 90,
#     "Adyashree": 85,
#     "sweta": 60
# }
# highest = None
# lowest = None

# for name, marks in students.items():

#     if highest is None or marks > highest[1]:
#         highest = (name, marks)

#     if lowest is None or marks < lowest[1]:
#         lowest = (name, marks)

# print("Highest marks:", highest[0], highest[1])
# print("Lowest marks:", lowest[0], lowest[1])

# 7. Find the second-highest marks from a student dictionary.
# students = {
#      "Sonali": 35,
#         "Pratikshya": 75,
#         "elina": 90,
#         "Adyashree": 85,
#         "sweta": 60
    
# }
# highest = 0
# second_highest = 0

# for name, marks in students.items():

#     if marks > highest:
#         second_highest = highest
#         highest = marks

#     elif marks > second_highest and marks != highest:
#         second_highest = marks
# print("Second highest marks:", second_highest)

# 8. Create a new dictionary containing only students who scored more than 75.

# students = {
#    "Sonali": 35,
#     "Pratikshya": 75,
#     "elina": 90,
#     "Adyashree": 85,
#     "sweta": 60
# }
# result = {}
# for name, marks in students.items():

#     if marks > 75:
#         result[name] = marks
# print(result)

# 9. Find the frequency of each character in a string and store it in a dictionary.

# text = "python programming"

# frequency = {}

# for i in text:

#     if i in frequency:      doubt
#         frequency[i] += 1
#     else:
#         frequency[i] = 1

# print(frequency)

#  10. Merge two dictionaries without using the update() method.


# dict1 = {
#     "name": "Sonali",
#     "age": 22,
#     "city": "Bhubaneswar"
# }
# dict2 = {
#     "course": "MCA",
#     "college": "GITAM",
#     "year": 2026
# }
# res = {}
# for key, value in dict1.items():
#     res[key] = value
# for key, value in dict2.items():
#     res[key] = value
# print(res)
