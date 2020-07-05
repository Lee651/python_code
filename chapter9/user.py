class User():
    def __init__(self, first_name, last_name, age, height, gender):
        self.full_name = first_name + " " + last_name
        self.Age = str(age)
        self.Height = str(height)
        self.Gender = gender
    
    def discribe_user(self):
        print("\nThe person's message are: ")
        print("name: " + self.full_name.title() + "\nage: " + self.Age + "\nheight: " + self.Height + "\ngender: " + self.Gender)

    def greet_user(self):
        print("\nHello, " + self.full_name + "!")

user_1 = User("xiangfei", "ai", 28, 170, "man")

user_1.discribe_user()
user_1.greet_user()

    