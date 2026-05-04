class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name



person1 = Person("Alice", 30, "Female")

print(person1.get_name())  # Output: Alice