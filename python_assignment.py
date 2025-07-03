# Chapter 1

# 1. Create variables to store your name, age, and country
name = "Your Name"
age = 25
country = "Your Country"

print(f"Name: {name}, Age: {age}, Country: {country}")

# 2. Convert Celsius to Fahrenheit
celsius = 25  # You can change this value
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

# 3. Check if a number is even or odd
number = 7  # You can change this value
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# 4. Store a user profile and print it in a sentence
user_profile = {
    "name": "Alice",
    "age": 30,
    "country": "Wonderland"
}
print(f"{user_profile['name']} is {user_profile['age']} years old and lives in {user_profile['country']}.")

# 5. Take user input for three numbers and find the average
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print(f"The average of the three numbers is {average}")

# Chapter 2

# 1. Create a list of your 5 favorite movies
favorite_movies = [
    "Inception",
    "The Matrix",
    "Interstellar",
    "The Dark Knight",
    "Forrest Gump"
]
print("My favorite movies are:", favorite_movies)

# 2. Make a dictionary with keys: name, age, course
student_info = {
    "name": "John Doe",
    "age": 21,
    "course": "Computer Science"
}
print("Student Info:", student_info)

# 3. Add and remove items from a set
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")  # Add an item
fruits.remove("banana")  # Remove an item
print("Fruits set:", fruits)

# 4. Sort a list of numbers
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print("Sorted numbers:", numbers)

# 5. Loop through a dictionary and print each key-value pair
for key, value in student_info.items():
    print(f"{key}: {value}")


# Chapter 3

# 1. Check if a number is positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print(f"{num} is positive.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print("The number is zero.")

# 2. Create a simple login system using if-else
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Invalid username or password.")

# 3. Print even numbers from 1 to 20 using a for loop
print("Even numbers from 1 to 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")
print()

# 4. Find the factorial of a number
n = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Factorial of {n} is {factorial}")

# 5. Sum all numbers in a list using a while loop
numbers_list = [3, 7, 2, 9, 4]
sum_total = 0
index = 0
while index < len(numbers_list):
    sum_total += numbers_list[index]
    index += 1
print(f"Sum of all numbers in the list is {sum_total}")

# Chapter 4

# 1. Print numbers from 1 to 10, skip 5
for i in range(1, 11):
    if i == 5:
        continue
    print(i, end=" ")
print()

# 2. Use pass in an empty function
def empty_function():
    pass

# 3. Write a loop to sum numbers until it reaches 100
sum_total = 0
num = 1
while sum_total < 100:
    sum_total += num
    num += 1
print(f"Sum reached: {sum_total}")

# 4. Break the loop if a negative number is entered
while True:
    n = int(input("Enter a number (negative to stop): "))
    if n < 0:
        print("Negative number entered. Loop stopped.")
        break
    print(f"You entered: {n}")

# 5. Print all vowels in a string
input_str = input("Enter a string: ")
vowels = "aeiouAEIOU"
print("Vowels in the string:", end=" ")
for char in input_str:
    if char in vowels:
        print(char, end=" ")
print()

# Chapter 5

# 1. Function to add two numbers
def add_numbers(a, b):
    return a + b
print("Sum of 3 and 5:", add_numbers(3, 5))

# 2. Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print("Is 7 prime?", is_prime(7))

# 3. Function to reverse a string
def reverse_string(s):
    return s[::-1]
print("Reverse of 'hello':", reverse_string('hello'))

# 4. Use *args and **kwargs in a function
def demo_args_kwargs(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)
demo_args_kwargs(1, 2, 3, name="Alice", age=25)

# 5. Function to count vowels in a sentence
def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count
print("Number of vowels in 'Hello World':", count_vowels('Hello World'))

# Chapter 6

# 1. Create a lambda to multiply two numbers
multiply = lambda x, y: x * y
print("Product of 4 and 5:", multiply(4, 5))

# 2. Use lambda to sort a list of tuples
list_of_tuples = [(1, 3), (2, 2), (4, 1), (3, 5)]
sorted_tuples = sorted(list_of_tuples, key=lambda x: x[1])
print("Sorted list of tuples by second element:", sorted_tuples)

# 3. Use lambda with filter to get even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# 4. Use lambda with map to square a list of numbers
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)

# 5. Combine lambda with reduce to sum a list
from functools import reduce
sum_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_numbers)

# Chapter 7

# 1. Count vowels and consonants
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")

# 2. Check if a string is a palindrome
pal_str = input("Enter a string to check palindrome: ")
if pal_str == pal_str[::-1]:
    print(f"'{pal_str}' is a palindrome.")
else:
    print(f"'{pal_str}' is not a palindrome.")

# 3. Replace spaces with dashes
sentence = input("Enter a sentence: ")
replaced = sentence.replace(' ', '-')
print("With dashes:", replaced)

# 4. Take full name and split into first and last
full_name = input("Enter your full name: ")
parts = full_name.split()
if len(parts) >= 2:
    first_name = parts[0]
    last_name = parts[-1]
    print(f"First name: {first_name}, Last name: {last_name}")
else:
    print("Please enter at least first and last name.")

# 5. Capitalize each word in a sentence
sentence2 = input("Enter a sentence to capitalize: ")
capitalized = sentence2.title()
print("Capitalized:", capitalized)

# Chapter 10

# 1. Create class Student with name and marks
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # marks should be a list

    # 2. Add a method to calculate average
    def calculate_average(self):
        if self.marks:
            return sum(self.marks) / len(self.marks)
        return 0

    def display(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}, Average: {self.calculate_average()}")

# Example usage:
student1 = Student("Alice", [85, 90, 78])
student1.display()

# 3. Inherit from class Person to create Teacher
class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"Hello, my name is {self.name}.")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def introduce(self):  # 5. Override a method using polymorphism
        print(f"Hello, I am {self.name} and I teach {self.subject}.")

# Example usage:
teacher1 = Teacher("Mr. Smith", "Mathematics")
teacher1.introduce()

# 4. Use private variables
class Secret:
    def __init__(self, data):
        self.__data = data  # private variable
    def reveal(self):
        print(f"The secret data is: {self.__data}")

secret_obj = Secret("Top Secret!")
secret_obj.reveal()
# print(secret_obj.__data)  # This will raise an AttributeError

# Chapter 12

# 1. Use lambda to add 10 to each number
nums = [1, 2, 3, 4, 5]
plus_ten = list(map(lambda x: x + 10, nums))
print("Add 10 to each number:", plus_ten)

# 2. Filter even numbers from a list
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", even_nums)

# 3. Square numbers using map()
squared = list(map(lambda x: x ** 2, nums))
print("Squared numbers:", squared)

# 4. Sum values using reduce()
from functools import reduce
total = reduce(lambda x, y: x + y, nums)
print("Sum of numbers:", total)

# 5. Sort list of tuples with lambda
tuple_list = [(2, 5), (1, 2), (4, 1), (3, 3)]
sorted_tuples = sorted(tuple_list, key=lambda x: x[1])
print("Sorted tuples by second element:", sorted_tuples)

# Chapter 13

# 1. Create list of even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)

# 2. Dict of numbers and their cubes
cubes = {x: x ** 3 for x in numbers}
print("Number and their cubes:", cubes)

# 3. Flatten a 2D list
matrix = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened = [item for sublist in matrix for item in sublist]
print("Flattened list:", flattened)

# 4. Create set of unique characters
sample_str = "hello world"
unique_chars = {char for char in sample_str if char != ' '}
print("Unique characters:", unique_chars)

# 5. Filter out negative numbers
nums_with_neg = [5, -3, 8, -1, 0, 4, -7]
non_negative = [x for x in nums_with_neg if x >= 0]
print("Non-negative numbers:", non_negative)












    




