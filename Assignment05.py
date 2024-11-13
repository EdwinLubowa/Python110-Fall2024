# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
# Edwin Kintu-Lubowa November 9, 2024,Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''   # Holds the last name of a student entered by the user.
course_name: str = ''         # Holds the name of a course entered by the user.
student_data: dict = {}       # one row of student data
students: list = []           # a table of student data
json_data: str = ''           # Holds combined string data separated by a comma.
file_obj = None               # Holds a reference to an opened file.
menu_choice: str              # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file_obj = open(FILE_NAME, "r")
    students = json.load(file_obj)
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

# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do? ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:  # trap user input errors
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("First name should only contain alphabetic characters!")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Last name should only contain alphabetic characters!")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_data["FirstName"]} {student_data["LastName"]} for {student_data["CourseName"]}.")
        except ValueError as e:
            print(e)  # Prints custom message
            print("-- Technical Error Message --")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!")
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep='\n')
            print("-" * 50)

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}.")
        print("-"*50)
    # Save the data to a file
    elif menu_choice == "3":
        try:  # trap JSON format errors
            file_obj = open(FILE_NAME, "w")
            json.dump(students, file_obj)
            file_obj.close()

            # test if there's no new data to save: alert user
            # otherwise, display data that was saved to file
            if student_data == {}:
                print("No new data to save to file!")
            else:
                print("Data Saved!\n")
                # Display data that was saved to file
                print("The following data was saved to file: ")
                for student in students:
                    print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}.")
                print("-" * 50)
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

    # Exit the program
    elif menu_choice == "4":
        print("Program Ended!")
        break

    # Catch invalid choices
    else:
        print("Invalid Entry!")
        print("Please enter choices: 1, 2, 3, or 4: ")
        continue
input("Pausing until you use the Enter key...")