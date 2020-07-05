class Employee():
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self):
        self.annual_salary += 5000
        message = self.first_name.title() + " " + self.last_name.title() + "'s annual salary is" + " " + str(self.annual_salary) + "!"
        print(message)

#employee1 = Employee("xiangfei", "ai", 1000)
#employee1.give_raise()