class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
student1 = student("xyz",20)
student2 = student("abc",23)
student3 = student("pqr",25)

student1.display()
student2.display()
student3.display()