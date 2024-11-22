class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks  # Protected attribute

    def update_marks(self, new_marks):
        self._marks = new_marks

    def get_details(self):
        return f"Name: {self.name}, Marks: {self._marks}"


# Testing the class
student = Student("Alice", 85)
print(student.get_details())
student.update_marks(90)
print(student.get_details())
