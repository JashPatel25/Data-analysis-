# 1. What are the types of applications?
# Applications can be categorized into:

# Web Applications: Hosted on servers and accessed via browsers (e.g., Facebook, Instagram).
# Mobile Applications: Built for mobile devices (e.g., WhatsApp, Uber).
# Desktop Applications: Installed on computers (e.g., Microsoft Word, Photoshop).
# Enterprise Applications: Designed for businesses, such as ERP or CRM systems.
# Gaming Applications: Used for entertainment (e.g., PUBG, Minecraft).


# 2. What is programming?
# Programming is the process of writing instructions for computers to perform specific tasks. It involves using a programming language to design, write, test, and maintain code.

#3. What is Python?
# Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple paradigms like object-oriented, procedural, and functional programming. Python is widely used in web development, data analysis, artificial intelligence, and more.



# 4. Python program to check if a number is positive, negative, or zero
def check_number(num):
    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

# Example usage
number = float(input("Enter a number: "))
check_number(number)



# 5. Python program to find the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
number = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {number} is {factorial(number)}")



# 6. Python program to get the Fibonacci series of a given range

def fibonacci_series(n):
    a, b = 0, 1
    print("Fibonacci Series:", end=" ")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Example usage
terms = int(input("Enter the number of terms for Fibonacci series: "))
fibonacci_series(terms)



# 7. How is memory managed in Python?
# Memory management in Python is handled by:

# Private Heap: All Python objects and data structures are stored in a private heap.
# Garbage Collection: Python automatically cleans up unused objects using garbage collection to free memory.
# Memory Allocation: Managed by Python’s memory manager, which handles requests for memory and optimizes its use.


# 8. What is the purpose of the continue statement in Python?
# The continue statement is used inside loops to skip the current iteration and move to the next iteration of the loop.

for num in range(5):
    if num == 2:
        continue  # Skip when num is 2
    print(num)


# 9. Python program to swap two numbers with and without a temporary variable

# With Temporary Variable:
def swap_with_temp(a, b):
    temp = a
    a = b
    b = temp
    return a, b

# Example usage
x, y = 5, 10
print("Before Swap:", x, y)
x, y = swap_with_temp(x, y)
print("After Swap:", x, y)

# Without Temporary Variable:
def swap_without_temp(a, b):
    a, b = b, a
    return a, b

# Example usage
x, y = 5, 10
print("Before Swap:", x, y)
x, y = swap_without_temp(x, y)
print("After Swap:", x, y)




# 10. Python program to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

# Example usage
number = int(input("Enter a number: "))
check_even_odd(number)




# 11. Python program to check if a letter is a vowel
def is_vowel(letter):
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        return True
    return False

# Example usage
print("Check if a letter is a vowel:")
letter = input("Enter a single letter: ")

if len(letter) != 1 or not letter.isalpha():
    print("Invalid input. Please enter a single alphabetical character.")
else:
    if is_vowel(letter):
        print(f"'{letter}' is a vowel.")
    else:
        print(f"'{letter}' is not a vowel.")


# 12. Python program to sum three given integers; if two values are equal, return 0

def custom_sum(a, b, c):
    if a == b or b == c or a == c:
        return 0
    return a + b + c

# Example usage
x, y, z = map(int, input("Enter three integers: ").split())
print("Result:", custom_sum(x, y, z))



# 13. Python program to return True if two integers are equal, or their sum or difference is 5
def check_values(a, b):
    if a == b or abs(a - b) == 5 or (a + b) == 5:
        return True
    return False

# Example usage
x, y = map(int, input("Enter two integers: ").split())
print("Result:", check_values(x, y))


# 14. Python program to sum the first n positive integers
def sum_of_integers(n):
    return n * (n + 1) // 2

# Example usage
n = int(input("Enter a positive integer: "))
print(f"The sum of the first {n} positive integers is {sum_of_integers(n)}")


# 15. Python program to calculate the length of a string
def string_length(s):
    return len(s)

# Example usage
text = input("Enter a string: ")
print(f"The length of the string is {string_length(text)}")


# 16. Python program to count the frequency of characters in a string

def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Example usage
text = input("Enter a string: ")
print("Character Frequency:", char_frequency(text))

#17 What are negative indexes, and why are they used?
# Negative Indexing: Negative indexes in Python allow you to access elements from the end of a list, tuple, or string.
# Use Case: Useful when you want to traverse or access elements in reverse order.

my_list = [10, 20, 30, 40, 50]
print(my_list[-1])  # Output: 50 (last element)
print(my_list[-2])  # Output: 40 (second-to-last element)


#18. Python program to count occurrences of a substring in a string
def count_substring(string, substring):
    return string.count(substring)

# Example usage
text = input("Enter a string: ")
sub = input("Enter the substring to count: ")
print(f"Occurrences of '{sub}':", count_substring(text, sub))

#19. Python program to count the occurrences of each word in a sentence
def word_count(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

# Example usage
text = input("Enter a sentence: ")
print("Word Frequency:", word_count(text))

#20. Python program to create a string from two given strings, swapping the first two characters of each

def swap_first_two_chars(str1, str2):
    if len(str1) < 2 or len(str2) < 2:
        return "Strings must have at least two characters."
    swapped_str1 = str2[:2] + str1[2:]
    swapped_str2 = str1[:2] + str2[2:]
    return swapped_str1 + " " + swapped_str2

# Example usage
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
print("Result:", swap_first_two_chars(string1, string2))


#21. Python program to add 'ing' at the end of a string

def add_ing_or_ly(s):
    if len(s) < 3:
        return s
    if s.endswith('ing'):
        return s + 'ly'
    return s + 'ing'

# Example usage
string = input("Enter a string: ")
print("Result:", add_ing_or_ly(string))


#22. Python function to reverse a string if its length is a multiple of 4
def reverse_if_multiple_of_4(s):
    if len(s) % 4 == 0:
        return s[::-1]
    return s

# Example usage
string = input("Enter a string: ")
print("Result:", reverse_if_multiple_of_4(string))


#23. Python program to get a string made of the first 2 and last 2 chars

def first_and_last_two(s):
    if len(s) < 2:
        return ""
    return s[:2] + s[-2:]

# Example usage
string = input("Enter a string: ")
print("Result:", first_and_last_two(string))


# 24. Python function to insert a string in the middle of another string
def insert_middle(main_string, insert_string):
    middle_index = len(main_string) // 2
    return main_string[:middle_index] + insert_string + main_string[middle_index:]

# Example usage
main_str = input("Enter the main string: ")
insert_str = input("Enter the string to insert: ")
print("Result:", insert_middle(main_str, insert_str))

"""25. What is a List How will you reverse a list
List A list is a mutable data structure in Python that can hold a collection of items, such as integers, strings, or other lists.
Reversing a List You can reverse a list using the reverse() method or slicing."""
#Example

my_list = [1, 2, 3, 4, 5]
my_list.reverse()  # Using reverse()
print(my_list)  # Output [5, 4, 3, 2, 1]

# Using slicing
reversed_list = my_list[-1]
print(reversed_list)  # Output [1, 2, 3, 4, 5]

"""26. How will you remove the last object from a list
You can remove the last object from a list using the pop() method or slicing.
"""
# Example

my_list = [10, 20, 30, 40, 50]
my_list.pop()  # Removes the last element
print(my_list)  # Output [10, 20, 30, 40]

# Using slicing
my_list = my_list[-1]
print(my_list)  # Output [10, 20, 30, 40].

""""27. What does list1[-1] return if list1 = [2, 33, 222, 14, 25]
list1[-1] returns the last element of the list.
Answer 25"""
#Example
list1 = [2, 33, 222, 14, 25]
print(list1[-1])  # Output 25

""" 28. Differentiate between append() and extend() methods
 append() Adds a single element to the end of the list.
 extend() Adds all elements of an iterable (e.g., list, tuple) to the list."""

# Example

my_list = [1, 2, 3]
my_list.append([4, 5])  # Adds as a single element
print(my_list)  # Output [1, 2, 3, [4, 5]]

my_list = [1, 2, 3]
my_list.extend([4, 5])  # Adds each element individually
print(my_list)  # Output [1, 2, 3, 4, 5]

"""29. Python function to get the largest number, smallest number, and sum of all numbers from a list"""
# example

def list_statistics(lst):
    largest = max(lst)
    smallest = min(lst)
    total_sum = sum(lst)
    return largest, smallest, total_sum

# Example usage
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
largest, smallest, total = list_statistics(numbers)
print(f"Largest: {largest}, Smallest: {smallest}, Sum: {total}")


'''30. How will you compare two lists
You can compare two lists using

Equality (==) Checks if the lists have the same elements in the same order.
Set Comparison If the order doesn't matter, you can compare lists as sets.
Manually Iterate through both lists and compare each element.'''
#Example
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [3, 2, 1]

# Method 1: Direct Comparison
print(list1 == list2)  # True
print(list1 == list3)  # False

# Method 2: Set Comparison (ignores order)
print(set(list1) == set(list3))  # True

"""31. Python program to count strings with the same first and last character (length >= 2)"""

def count_strings(lst):
    count = 0
    for string in lst:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

# Example usage
strings = input("Enter a list of strings separated by spaces: ").split()
print("Count:", count_strings(strings))


"""32. Python program to remove duplicates from a list"""

def remove_duplicates(lst):
    return list(set(lst))

# Example usage
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("List without duplicates:", remove_duplicates(numbers))


"33. Python program to check if a list is empty"

def is_empty(lst):
    return len(lst) == 0

# Example usage
numbers = []
print("Is the list empty?", is_empty(numbers))

"34. Python function to check if two lists have at least one common member"
def have_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

# Example usage
list1 = input("Enter the first list (space-separated): ").split()
list2 = input("Enter the second list (space-separated): ").split()
print("Do the lists have common members?", have_common_member(list1, list2))


"35. Python program to generate a list of squares of numbers, selecting first and last 5 elements"

def squares_list():
    squares = [i ** 2 for i in range(1, 31)]
    return squares[:5] + squares[-5:]

# Example usage
print("First and last 5 squares:", squares_list())


'36. Python function to return a new list with unique elements'

def unique_elements(lst):
    return list(set(lst))

# Example usage
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("Unique elements:", unique_elements(numbers))

'37. Python program to convert a list of characters into a string'

def list_to_string(char_list):
    return ''.join(char_list)

# Example usage
chars = input("Enter a list of characters (space-separated): ").split()
print("Converted string:", list_to_string(chars))


'38. Python program to select an item randomly from a list'

import random

def select_random_item(lst):
    return random.choice(lst)

# Example usage
items = input("Enter a list of items separated by spaces: ").split()
print("Random item:", select_random_item(items))


"39. Python program to find the second smallest number in a list"

def second_smallest(lst):
    unique_numbers = sorted(set(lst))
    if len(unique_numbers) < 2:
        return None  # Not enough unique numbers
    return unique_numbers[1]

# Example usage
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("Second smallest number:", second_smallest(numbers))


'40. Python program to get unique values from a list'
def unique_values(lst):
    return list(set(lst))

# Example usage
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("Unique values:", unique_values(numbers))


'41. Python program to check whether a list contains a sublist'

def contains_sublist(lst, sublst):
    n, m = len(lst), len(sublst)
    for i in range(n - m + 1):
        if lst[i:i + m] == sublst:
            return True
    return False

# Example usage
main_list = list(map(int, input("Enter the main list (space-separated): ").split()))
sub_list = list(map(int, input("Enter the sublist (space-separated): ").split()))
print("Contains sublist:", contains_sublist(main_list, sub_list))


'42. Python program to split a list into different variables'

def split_list(lst):
    return lst

# Example usage
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
var1, var2, *rest = numbers  # Example of unpacking
print("First variable:", var1)
print("Second variable:", var2)
print("Rest:", rest)


'''43. What is a Tuple? Difference between List and Tuple
Tuple: A tuple is an immutable (unchangeable) ordered collection of items in Python. It is defined using parentheses ().
Differences:

Mutability: Lists are mutable (can be changed), while tuples are immutable.
Syntax: Lists use square brackets [], tuples use parentheses ().
Performance: Tuples are generally faster than lists.'''

# Example
my_list = [1, 2, 3]  # List
my_tuple = (1, 2, 3)  # Tuple

'44. Python program to create a tuple with different data types'
my_tuple = (1, "hello", 3.14, True)
print("Tuple with different data types:", my_tuple)

'45. Python program to unzip a list of tuples into individual lists'

def unzip_tuples(tuples_list):
    return list(zip(*tuples_list))

# Example usage
tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
list1, list2 = unzip_tuples(tuples)
print("First list:", list1)
print("Second list:", list2)


'46. Python program to convert a list of tuples into a dictionary'


def tuples_to_dict(tuples_list):
    return dict(tuples_list)

# Example usage
tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
print("Dictionary:", tuples_to_dict(tuples))


'''47. How will you create a dictionary using tuples in Python?
You can create a dictionary using a tuple of key-value pairs:'''

# Example
my_tuples = (('a', 1), ('b', 2), ('c', 3))
my_dict = dict(my_tuples)
print("Dictionary:", my_dict)


"48. Python script to sort a dictionary by value (ascending and descending)"

def sort_dict_by_value(d, ascending=True):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=not ascending))

# Example usage
my_dict = {'a': 3, 'b': 1, 'c': 2}
print("Ascending:", sort_dict_by_value(my_dict))
print("Descending:", sort_dict_by_value(my_dict, ascending=False))


"49. Python script to concatenate dictionaries to create a new one"

def concatenate_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

# Example usage
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
print("Concatenated Dictionary:", concatenate_dicts(dict1, dict2))

# 50. Python script to check if a given key already exists in a dictionary

def key_exists(d, key):
    return key in d

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 3}
key = input("Enter a key to check: ")
print("Key exists:", key_exists(my_dict, key))


"""
51. How do you traverse through a dictionary in Python?
You can traverse through a dictionary using a for loop in three ways"""

my_dict = {'a': 1, 'b': 2, 'c': 3}

# Traverse keys
for key in my_dict:
    print("Key:", key)

# Traverse values
for value in my_dict.values():
    print("Value:", value)

# Traverse key-value pairs
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")


"""52. How do you check the presence of a key in a dictionary?
You can check if a key exists using the in keyword."""

#example
my_dict = {'a': 1, 'b': 2, 'c': 3}
key = input("Enter a key to check: ")

if key in my_dict:
    print("Key exists in the dictionary.")
else:
    print("Key does not exist in the dictionary.")

"""53. Python script to print a dictionary where the keys are numbers from 1 to 15"""    
def generate_dict():
    return {i: i**2 for i in range(1, 16)}

# Example usage
print("Generated Dictionary:", generate_dict())


"""54. Python program to check if multiple keys exist in a dictionary"""

def multiple_keys_exist(d, keys):
    return all(key in d for key in keys)

# Example usage
my_dict = {'a': 1, 'b': 2, 'c': 3}
keys_to_check = ['a', 'b']
print("All keys exist:", multiple_keys_exist(my_dict, keys_to_check))


# 55. Python script to merge two dictionaries
def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

# Example usage
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
print("Merged Dictionary:", merge_dicts(dict1, dict2))


"56. Python program to map two lists into a dictionary"

def map_lists_to_dict(keys, values):
    return dict(zip(keys, values))

# Example usage
keys = input("Enter keys (space-separated): ").split()
values = input("Enter values (space-separated): ").split()
print("Mapped Dictionary:", map_lists_to_dict(keys, values))


"57. Python program to find the highest 3 values in a dictionary"
def highest_values(d, n=3):
    return sorted(d.values(), reverse=True)[:n]

# Example usage
my_dict = {'a': 10, 'b': 20, 'c': 5, 'd': 8}
print("Highest 3 values:", highest_values(my_dict))


"58. Python program to combine values in a list of dictionaries"
#Sample data:

data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

#program

from collections import Counter

def combine_values(dict_list):
    counter = Counter()
    for d in dict_list:
        counter[d['item']] += d['amount']
    return counter

# Example usage
data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
print("Combined Values:", combine_values(data))


"59. Python program to create a dictionary from a string (letter count)"

def string_to_dict(s):
    from collections import Counter
    return Counter(s)

# Example usage
text = input("Enter a string: ")
print("Dictionary of letter counts:", string_to_dict(text))


"60. Python program to count the occurrences of each letter in a string"

#Sample
# String: 'w3resource'

def count_letters(s):
    return {char: s.count(char) for char in set(s)}

# Example usage
string = 'w3resource'
print("Occurrences of each letter:", count_letters(string))


"61. Python function to calculate the factorial of a number (non-negative integer)"
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
num = int(input("Enter a non-negative integer: "))
print(f"Factorial of {num} is {factorial(num)}")


"62. Python function to check whether a number is in a given range"

def is_in_range(num, start, end):
    return start <= num <= end

# Example usage
num = int(input("Enter a number: "))
start, end = map(int, input("Enter the range (start and end): ").split())
print(f"Is {num} in range {start}-{end}:", is_in_range(num, start, end))


# 63. Python function to check whether a number is perfect or not
# A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding itself)

def is_perfect(num):
    if num <= 0:
        return False
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

# Example usage
num = int(input("Enter a number: "))
print(f"Is {num} a perfect number?", is_perfect(num))


# 64. Python function to check if a string is a palindrome
# A palindrome is a string that reads the same backward as forward.

def is_palindrome(s):
    return s == s[::-1]

# Example usage
string = input("Enter a string: ")
print(f"Is '{string}' a palindrome?", is_palindrome(string))


# 65. How many basic types of functions are available in Python?
# There are two basic types of functions in Python:

# Built-in Functions: Functions that are pre-defined in Python (e.g., print(), len(), sum()).
# User-defined Functions: Functions created by the user to perform specific tasks.

"""66. How can you pick a random item from a list or tuple?
You can use the random.choice() method from the random module."""
# Example:

import random

items = [1, 2, 3, 4, 5]
print("Random item from list:", random.choice(items))

tuple_items = ('a', 'b', 'c', 'd')
print("Random item from tuple:", random.choice(tuple_items))


"""67. How can you pick a random item from a range?
You can use the random.randrange() method or random.randint()."""

#Example

import random

print("Random number from range (1-10):", random.randrange(1, 11))

"""68. How can you get a random number in Python?
Use the random.randint() or random.uniform() methods."""
#example

import random

# Random integer
print("Random integer (1-100):", random.randint(1, 100))

# Random float
print("Random float (0-1):", random.random())


"""69. How will you set the starting value in generating random numbers?
You can set the seed using random.seed(). Setting a seed ensures reproducible results."""

#Example
import random

random.seed(10)  # Set seed
print("Random number with seed 10:", random.randint(1, 100))


"""70. How will you randomize the items of a list in place?
Use the random.shuffle() method to randomize the items."""
#Example

import random

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("Shuffled list:", my_list)


""""71. What is a file function in Python? What are the keywords to create and write files?
File Functions: Python provides functions like open(), read(), write(), and close() for working with files.
Keywords for File Operations:
'r': Read mode (default).
'w': Write mode (overwrites the file if it exists).
'a': Append mode (adds content to the end of the file).
'x': Exclusive creation (fails if the file exists).
'b': Binary mode (used with 'rb', 'wb').
't': Text mode (default, used with 'rt', 'wt')."""


#72. Python program to read an entire text file

def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

# Example usage
file_name = input("Enter the file name: ")
print("File content:\n", read_file(file_name))

"73. Python program to append text to a file and display the text"

def append_and_read_file(filename, text):
    with open(filename, 'a') as file:
        file.write(text + '\n')
    with open(filename, 'r') as file:
        content = file.read()
    return content

# Example usage
file_name = input("Enter the file name: ")
text_to_append = input("Enter the text to append: ")
print("Updated File Content:\n", append_and_read_file(file_name, text_to_append))


# 74. Python program to read the first n lines of a file

def read_first_n_lines(filename, n):
    with open(filename, 'r') as file:
        lines = [file.readline() for _ in range(n)]
    return ''.join(lines)

# Example usage
file_name = input("Enter the file name: ")
n_lines = int(input("Enter the number of lines to read: "))
print("First", n_lines, "lines:\n", read_first_n_lines(file_name, n_lines))


"""75. Python program to read the last n lines of a file"""

def read_last_n_lines(filename, n):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return ''.join(lines[-n:])

# Example usage
file_name = input("Enter the file name: ")
n_lines = int(input("Enter the number of lines to read: "))
print("Last", n_lines, "lines:\n", read_last_n_lines(file_name, n_lines))


# 76. Python program to read a file line by line and store it in a list
def read_lines_to_list(filename):
    with open(filename, 'r') as file:
        return file.readlines()

# Example usage
file_name = input("Enter the file name: ")
print("Lines stored in a list:", read_lines_to_list(file_name))


"77. Python program to read a file line by line and store it into a variable"

def read_lines_to_variable(filename):
    with open(filename, 'r') as file:
        return ''.join(file.readlines())

# Example usage
file_name = input("Enter the file name: ")
print("File content in a variable:\n", read_lines_to_variable(file_name))

# 78. Python program to find the longest words in a file
def find_longest_word(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    longest_word = max(words, key=len)
    return longest_word

# Example usage
file_name = input("Enter the file name: ")
print("Longest word in the file:", find_longest_word(file_name))

"79. Python program to count the number of lines in a text file"
def count_lines(filename):
    with open(filename, 'r') as file:
        return len(file.readlines())

# Example usage
file_name = input("Enter the file name: ")
print("Number of lines in the file:", count_lines(file_name))

"80. Python program to count the frequency of words in a file"

from collections import Counter

def word_frequency(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    return Counter(words)

# Example usage
file_name = input("Enter the file name: ")
print("Word frequency:\n", word_frequency(file_name))

"81. Python program to write a list to a file"

def write_list_to_file(filename, lst):
    with open(filename, 'w') as file:
        for item in lst:
            file.write(str(item) + '\n')

# Example usage
file_name = input("Enter the file name: ")
items = input("Enter items for the list (space-separated): ").split()
write_list_to_file(file_name, items)
print("List written to file successfully.")


"82. Python program to copy the contents of one file to another"

def copy_file_contents(source, destination):
    with open(source, 'r') as src, open(destination, 'w') as dest:
        dest.write(src.read())

# Example usage
source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")
copy_file_contents(source_file, destination_file)
print(f"Contents of {source_file} copied to {destination_file}")


# 83. Explain Exception Handling? What is an Error in Python?
"""Exception Handling: Python provides a mechanism to handle runtime errors (exceptions) to prevent the program from crashing.
Exceptions occur during the execution of a program (e.g., division by zero, accessing a non-existent file).
Exception handling uses try, except, else, and finally blocks."""

#Example

try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a number.")
finally:
    print("Execution completed.")


"""84. How many except statements can a try-except block have? Name some built-in exception classes.
Number of except Statements: A try block can have multiple except statements to handle different exceptions.
Some Built-in Exception Classes:
ValueError
ZeroDivisionError
TypeError
IndexError
KeyError """

"""|85. When will the else part of try-except-else be executed?
The else part will execute only if no exceptions are raised in the try block."""

#Example

try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Division successful!")


"""86. Can one block of except statements handle multiple exceptions?
Yes, a single except block can handle multiple exceptions by specifying them as a tuple."""

#Example:.
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except (ZeroDivisionError, ValueError):
    print("Either a division by zero or invalid input occurred.")


"""87. When is the finally block executed?
The finally block is always executed, regardless of whether an exception was raised or not."""

#Example:
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("This block is always executed.")


"""88. What happens when '1' == 1 is executed?
When '1' == 1 is executed:

It evaluates to False because Python compares both the value and the type, and the string '1' is not the same type as the integer 1."""


"""89. How do you handle exceptions with try/except/finally in Python?
You use try to attempt a block of code, except to catch exceptions, and finally to execute code regardless of exceptions."""

#Example:
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input.")
finally:
    print("Cleaning up resources.")


"90. Write a Python program to require the user to enter only odd numbers; otherwise, raise an exception."

def check_odd_number():
    try:
        num = int(input("Enter an odd number: "))
        if num % 2 == 0:
            raise ValueError("This is not an odd number!")
        print(f"{num} is an odd number.")
    except ValueError as e:
        print(e)

# Example usage
check_odd_number()







