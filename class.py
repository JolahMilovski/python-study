class Dog:
    '''A simple attemp to model dog'''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def  sit(self):
        print(f"{self.name} is sitiing now")

    def roll_over(self):
        print(f"{self.name} rolled over")

    
my_dog = Dog("Willie", 6)

print(f"My dog name is {my_dog.name}")
print(f"My dog is {my_dog.age} old")

my_dog.sit()
my_dog.roll_over()


