""" 
Angela Gale 
Module 2 Lab - Case Study 
Code Description: 
This Python code will ask for and accept 
student names and GPAs to determine whether they qualify for 
the Dean's List or Honor Roll
using if, else, and while statements.
"""


while True: 
    student_lastname = input("Enter your last name ['ZZZ' to quit]: ")
    if student_lastname.upper() == "ZZZ":
        break 

    student_firstname = input("Enter your first name: ")

    gpa = float(input("Enter your GPA: "))

    if gpa >= 3.5: 
        print(f"Congradulations {student_firstname} {student_lastname}!!! You've made the Dean's List!")
    elif 3.25 <= gpa < 3.5: 
        print(f"Congradulations {student_firstname} {student_lastname}! You've made Honor Roll!")



