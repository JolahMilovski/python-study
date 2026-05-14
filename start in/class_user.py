class User:
    '''initialized a user'''
    def __init__ (self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age # = 0  default attibute
        self.sex = sex

    def describe_user(self):
        print(f"First name is {self.first_name.upper()}")
        print(f"Last name is {self.last_name}")
        print(f"{self.last_name} is {self.age} years old")
        print(f"{self.first_name} is a {self.sex}\n")


    """gender was determined based on age"""
    def set_sex(self):        
        if self.age <13:
            self.sex = "man"
        else:
            self.sex = "woman"

    '''add 5 year to age'''
    def add_five_year(self):
        self.age += 5


users = {
    User("Nick","Denick", 12, "man"),
    User("Brack","Genick", 15, "woman"),
    User("Rick","Renick", 32, "man"),
    User("Tunik","Menick", 12, "woman")
}


for user in users:
    user.sex = "non"
    user.set_sex()
    user.describe_user()

print(f"5 years have passed\n")

for user in users:
    user.add_five_year()
    user.set_sex()
    user.describe_user()
