class student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        
    def display(self):
        print(f"Name: {self.name}, Roll no.: {self.roll_no}")
        
student1 = student("John",2)

student1.display()