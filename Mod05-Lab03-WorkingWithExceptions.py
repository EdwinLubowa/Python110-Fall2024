# ------------------------------------------------------------------------------------------
# Title: Working With Dictionaries And Files
# Desc: Shows how work with dictionaries and files when using a table of data
# Change Log: (Who, When, What)
#  Edwin Kintu-Lubowa, November 8, 2024,Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
FILE_NAME: str = "MyLabData.json"

# Define the program's data
MENU: str = """
----------Student GPAs---------
Select from the following menu:
  1. Show current student data. 
  2. Enter new student data.
  3. Save data to file.
  4. Exit the program.
"""
student_first_name: str = "" # holds student first name entered by the user
student_last_name: str = ""  # holds student last name entered by the user
student_gpa: float = 0.0     # holds gpa of student entered by the user
message: str = ""            # holds custom message string
menu_choice: str = ""        # holds the choice made by the user
student_data: dict = {}      # holds one row of student data
students: list = []          # holds a table of student data
file_data: str = ""          # holds combined string data separated by comma
file_obj = None              # not using Type Hint to help PyCharm

# When the program starts, read the file data into a list of dictionary rows (table)
try:
    file_obj = open(FILE_NAME, "r")
    students = json.load(file_obj)
    file_obj.close()

except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message --")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message --")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file_obj.closed == False:
        file_obj.close()

# file_obj = open(FILE_NAME, "r")
# for row in file_obj.readlines():
#     # Transform the data from the file
#     student_data = row.split(",")
#     student_data = {"FirstName": student_data[0],
#                     "LastName": student_data[1],
#                     "GPA": float(student_data[2].strip())}
#     # Load it into the collection
#     students.append(student_data)
# file_obj.close()

# Repeat the follow tasks
while True:
    print(MENU)
    menu_choice = input("Enter your menu choice number: ")
    print()      # adding an extra space to make it look nicer
    # display the table's current data
    if menu_choice == "1":
        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            if student["GPA"] >= 4.0:
                message = " {} {} earned an A with a {:.2f} GPA"
            elif student["GPA"] >= 3.0:
                message = " {} {} earned a B with a {:.2f} GPA"
            elif student["GPA"] >= 2.0:
                message = " {} {} earned a C with a {:.2f} GPA"
            elif student["GPA"] >= 1.0:
                message = " {} {} earned a D with a {:.2f} GPA"
            else:
                message = " {} {}'s {:.2f} GPA is not a passing grade"
            print(message.format(student["FirstName"], student["LastName"], student["GPA"]))
        print("-"*50)
        continue
    elif menu_choice == "2":
        # Input the data
        print("-" * 50)
        try:
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers."
                                 "")
            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            try:  # using a nested try block to capture when input cannot be changed to a float
                student_gpa = float(input("What is the student's GPA? "))
            except ValueError:
                raise ValueError("GPA must be a numeric value.")
            # Add student data to a dictionary variable "student-data
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "GPA": student_gpa}
            # Adding data to the table
            students.append(student_data)
        except ValueError as e:
            print(e)     # Prints custom message
            print("-- Technical Error Message --")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!")
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep='\n')
            print("-"*50)

    elif menu_choice == "3":
        try:
            # Save the data to the file
            file_obj = open(FILE_NAME, "w")
            json.dump(students, file_obj)
            file_obj.close()
            print("Data Saved!")
            continue
        except TypeError as e:
            print("Please check that the data is a valid JSON format.")
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message --")
            print("Built-in Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file_obj.closed == False:
                file_obj.close()

        # file_obj = open(FILE_NAME, "w")
        # for student in students:
        #     file_obj.write(f"{student["FirstName"]},{student["LastName"]},{student["GPA"]}\n")
        # file_obj.close()
        # print("Data Saved!")
        # continue
    elif menu_choice == "4":
        # Exit the program
        print("Program ended!")
        break

    else:  # catch invalid entry choices
        print("Invalid entry!")
        print("Please enter choice: 1, 2, 3, or 4: ")
        continue
input("Pausing until you use the Enter key...")
