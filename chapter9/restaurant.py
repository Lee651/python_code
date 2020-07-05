class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
        self.dinner_number = 5

    def describe_restaurant(self):
        print("\nThe restaurant's name is " + self.name.title() + "," + "and the cuisine type is " + self.type + ".")

    def open_restaurant(self):
        print("The " + self.name.title() + " is opening now!")

    def have_served_number(self):
        print("The restaurant have served " + " " + str(self.number_served) + " " + "peoples.")

    def set_number_served(self):
        print("The restaurant could seat " + str(self.dinner_number) + " people at a time.")

restaurants = {"sichuan restaurant" : "huoguo", "hunan restaurant" : "xiangcai" , "guangdong restaurant" : "baotang"}

for A,B in restaurants.items():
    restaurant_1 = Restaurant(A, B)

    restaurant_1.describe_restaurant()
    restaurant_1.open_restaurant()

    restaurant_1.number_served = 30
    restaurant_1.have_served_number()


    restaurant_1.dinner_number = 20
    restaurant_1.set_number_served()

