# Define the Student class using OOP concepts
class Student:
    def __init__(self, name, marks):
        """Constructor to initialize name and marks"""
        self.name = name
        self.marks = marks

    def display(self):
        """Method to display student details"""
        print("------ Student Details ------")
        print(f"Name  : {self.name}")
        print(f"Marks : {self.marks}")
        print("-----------------------------")

# Taking input from user
name_input = input("Enter student name: ")
marks_input = float(input("Enter student marks: "))

# Creating an object of Student class
student1 = Student(name_input, marks_input)

# Calling the display method
student1.display()
