class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  

    def show_details(self):
        print(f"Department: {self.dept_name}")
        print(f"Employee: {self.employee.name}")

emp1 = Employee("Alice")
dept1 = Department("HR", emp1)
dept1.show_details()
