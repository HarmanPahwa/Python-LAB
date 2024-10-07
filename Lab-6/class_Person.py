class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("abc", 25)
person2 = Person("xyz", 22)

person1.display()
person2.display()