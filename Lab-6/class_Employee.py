class Employee:
    def __init__(self, name, age, salary):
        self.name = name  # Public attribute
        self._age = age  # Protected attribute
        self.__salary = salary  # Private attribute

    # Public method
    def display_employee(self):
        print(f"Name: {self.name}, Age: {self._age}")
        self.__display_salary()  # Calling a private method

    # Protected method
    def _update_age(self, new_age):
        self._age = new_age

    # Private method
    def __display_salary(self):
        print(f"Salary: {self.__salary}")


# Testing the class
employee = Employee("John", 30, 50000)
employee.display_employee()  # Accessing public method
employee._update_age(32)  # Accessing protected method (discouraged but possible)
employee.display_employee()

# Accessing private method or attribute will raise an error
# print(employee.__salary)  # Uncommenting this will cause an AttributeError
