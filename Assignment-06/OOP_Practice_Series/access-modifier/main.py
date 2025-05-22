class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected
        self.__ssn = ssn          # Private

    def show_info(self):
        print("Inside class:")
        print("Name   :", self.name)
        print("Salary :", self._salary)
        print("SSN    :", self.__ssn)


# Create an object of Employee
emp = Employee("Alice", 50000, "123-45-6789")


print("\nAccessing from outside the class:")
print("Public - Name   :", emp.name)           
print("Protected - Salary:", emp._salary)       
print("Private - SSN (via name mangling):", emp._Employee__ssn)  
print("\nAccessing using class method:")
emp.show_info()
