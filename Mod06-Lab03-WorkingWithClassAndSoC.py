# ------------------------------------------------- #
# Title: Lab03 - Working with Classes and SoC
# Description: Demonstrates how classes can organize functions
#              and how SoC organizes the placement of those functions
#              into separate classes
# ChangeLog: (Who, When, What)
# Edwin Kintu-Lubowa,11.15.2024,Created Script
# ------------------------------------------------- #
import json
import io as _io  # Needed to try closing in the finally block

# Define the Data Constants
FILE_NAME: str = 'MyLabData.json'


# Define the program's data
MENU: str = '''
---- Student GPAs ------------------------------
  Select from the following menu:  
    1. Show current student data. 
    2. Enter new student data.
    3. Save data to a file.
    4. Exit the program.
-------------------------------------------------- 
'''

student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''   # Holds the last name of a student entered by the user.
student_gpa: float = 0.0      # Holds the GPA of a student entered by the user.
message: str = ''             # Holds a custom message string.
menu_choice: str = ''         # Hold the choice made by the user.
student: dict = {}            # one row of student data.
students: list = []           # a table of student data.
file_data: str = ''           # Holds json data.
file = _io.TextIOWrapper      # This is the actual type of the file handler.

# Processing ------------------------------------------------------------------------#
class FileProcessor:
    """
    A Collection of Processing Layer Functions that work with JSON Files

    ChangeLog: (Who, When, What)
    RRoot,11.15.2024,Created Class
    RRoot,11.15.2024,Added Function to read data from file
    RRoot,11.15.2024,Added Function to write data to file

    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This Function reads data from a file using JSON module

        ChangeLog: (Who, When, What)
        RRoot,11.15.2024,Created Function
        :param file_name:
        :param student_data:
        :return:
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!\n", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!\n", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This Function writes data from a list table to a file using JSON module

        ChangeLog: (Who, When, What)
        RRoot,11.15.2024,Created Function
        :param file_name:
        :param student_data:
        :return:
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format.", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()


# Presentation ----------------------------------------------------------------------#
class IO:
    """
    A Collection of Presentation Layer Functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,11.15.2024,Created Class
    RRoot,11.15.2024,Added menu output and input Functions
    RRoot,11.15.2024,Added a Function to display the data
    RRoot,11.15.2024,Added a Function to display custom error messages
    """
    @staticmethod
    def output_error_messages(message:str, error: Exception = None):
        """
        This Function displays custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,11.15.2024,Created Function
        :param message:
        :param error:
        :return:None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message --")
            print(error, error.__doc__, type(error), sep="\n")


    @staticmethod
    def output_menu(menu: str):
        """
        This Function displays the Menu of Options to the user

        ChangeLog: (Who, When, What)
        RRoot,11.15.2024,Created Function
        :param menu:
        :return:None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.


    @staticmethod
    def input_menu_choice():
        """
        This Function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        RRoot,11.15.2024,Created Function
        :return: string with the user's choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__()) # Not passing e to avoid the technical message
        return choice


    @staticmethod
    def output_letter_by_gpa(student_data: list):
        """
        This Function displays the letter grades based on their GPA to the user

        ChangeLog: (Who, When, What)
        RRoot,11.15.2024,Created Function
        :param student_data:
        :return:None
        """
        # Process the data to create and display a custom message
        print()
        print("-" * 50)
        for student in student_data:
            if student["GPA"] >= 4.0:
                message = " {} {} earned an A with a {:.2f} GPA"
            elif student["GPA"] >= 3.0:
                message = " {} {} earned a B with a {:.2f} GPA"
            elif student["GPA"] >= 2.0:
                message = " {} {} earned a C with a {:.2f} GPA"
            elif student["GPA"] >= 1.0:
                message = " {} {} earned a D with a {:.2f} GPA"
            else:
                message = " {} {}'s {:.2f} GPA was not a passing grade"

            print(message.format(student["FirstName"], student["LastName"], student["GPA"]))
        print("-" * 50)
        print()


    @staticmethod
    def input_student_data(student_data: list):
        """
        This Function gets the first name, last name ,and GPA from the user

        ChangeLog: (Who, When, What)
        RRoot,11.15.2024,Created Function
        :param student_data:
        :return: string
        """
        try:
            # Input the data
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            try:  # using a nested try block to capture when an input cannot be changed to a float
                student_gpa = float(input("What is the student's GPA? "))
            except ValueError:
                raise ValueError("GPA must be a numeric value.")

            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "GPA": float(student_gpa)}
            student_data.append(student)
        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!\n", e)
        return student_data


#  End of function definitions


# Beginning of the main body of this script

# When the program starts, read the file data into table
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Repeat the following tasks
while True:

    IO.output_menu(menu=MENU)
    menu_choice = IO.input_menu_choice()

    # Show the current student data
    if menu_choice == "1":
        IO.output_letter_by_gpa(student_data=students)
        continue

    # Enter new student data
    elif menu_choice == "2":
        students = IO.input_student_data(student_data=students)
        IO.output_letter_by_gpa(student_data=students)  # Add this to improve user experience
        continue

    # Save data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Exit the program
    elif menu_choice == "4":
        break  # out of the while loop
