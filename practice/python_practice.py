"""
====================================================
  Python Practice Exercises
  CSP Python & Cybersecurity - 2026
====================================================
Complete each exercise below.
Run this file when done to check your output.
"""

# ============================================================
# EXERCISE 1: Variables and Output
# ============================================================
# Create variables for:
#   - your name (string)
#   - your grade level (integer)
#   - your GPA (float)
# Then print them in one sentence.

# YOUR CODE HERE
name = "Student"
grade = 11
gpa = 3.5
print(f"My name is {name}, I am in grade {grade}, and my GPA is {gpa}.")


# ============================================================
# EXERCISE 2: Conditionals
# ============================================================
# Given a score, print the letter grade:
#   90-100 = A, 80-89 = B, 70-79 = C, 60-69 = D, below 60 = F

def get_grade(score):
    # YOUR CODE HERE
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print("Score 95 ->", get_grade(95))  # A
print("Score 82 ->", get_grade(82))  # B
print("Score 55 ->", get_grade(55))  # F


# ============================================================
# EXERCISE 3: Loops
# ============================================================
# Print all even numbers from 1 to 20 using a loop.

print("\nEven numbers from 1 to 20:")
# YOUR CODE HERE
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")
print()  # newline


# ============================================================
# EXERCISE 4: Functions
# ============================================================
# Write a function called multiply_list that takes a list of
# numbers and returns their product (all multiplied together).
# Example: multiply_list([2, 3, 4]) -> 24

def multiply_list(numbers):
    # YOUR CODE HERE
    result = 1
    for n in numbers:
        result *= n
    return result

print("\nProduct of [2,3,4]:", multiply_list([2, 3, 4]))   # 24
print("Product of [5,5]:",   multiply_list([5, 5]))       # 25


# ============================================================
# EXERCISE 5: Strings
# ============================================================
# Write a function called count_vowels(text) that returns how
# many vowels (a, e, i, o, u) are in the given string.
# Example: count_vowels("Hello World") -> 3

def count_vowels(text):
    # YOUR CODE HERE
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print("\nVowels in 'Hello World':", count_vowels("Hello World"))  # 3
print("Vowels in 'Cybersecurity':", count_vowels("Cybersecurity"))


# ============================================================
# EXERCISE 6: Lists & Dictionaries
# ============================================================
# A class has these grades stored in a list.
# Find the highest grade, lowest grade, and average.

grades = [78, 92, 85, 67, 99, 74, 88, 91, 55, 83]

highest = max(grades)
lowest  = min(grades)
average = sum(grades) / len(grades)

print(f"\nClass Grades: {grades}")
print(f"Highest: {highest}")
print(f"Lowest:  {lowest}")
print(f"Average: {average:.1f}")


# ============================================================
# EXERCISE 7: File I/O
# ============================================================
# Write a list of 3 cybersecurity tips to a file called
# 'my_tips.txt', then read it back and print the contents.

tips = [
    "1. Use strong, unique passwords for every account.\n",
    "2. Enable multi-factor authentication (MFA).\n",
    "3. Keep your software and operating system updated.\n"
]

# Write tips to file
with open("my_tips.txt", "w") as f:
    f.writelines(tips)

# Read and print
print("\n--- Contents of my_tips.txt ---")
with open("my_tips.txt", "r") as f:
    print(f.read())

print("Practice complete! Check your outputs above.")
