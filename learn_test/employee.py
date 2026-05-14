class Employee:
    def __init__ (self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self):
        self.annual_salary += 5000
        self.bonus_for_annual_salary = self.annual_salary + self.annual_salary * 0.1
        print(f"For {self.first_name} {self.last_name} anual salary is {self.annual_salary} and bonus of {self.bonus_for_annual_salary}")



