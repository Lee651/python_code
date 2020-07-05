class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
        self.could_served_number = 0

    def describe_restaurant(self):
        print("\nThe restaurant's name is " + self.name.title() + "," + "and the cuisine type is " + self.type + ".")

    def served_number(self):
        print("The restaurant have served " + str(self.number_served) + " " + "peoples.")

    def set_number_served(self):
        print("The restaurant could serve " + str(self.could_served_number) + " " + "peoples everytime.")

    def open_restaurant(self):
        print("The " + self.name.title() + " is opening now!")

restaurant = {"sichuan restaurant" : "huoguo", "hunan restaurant" : "xiangcai" , "guangdong restaurant" : "baotang"}
for A,B in restaurant.items():
    restaurant_1 = Restaurant(A, B)

    restaurant_1.describe_restaurant()
    restaurant_1.open_restaurant()

    restaurant_1.number_served = 23
    restaurant_1.served_number()

    restaurant_1.could_served_number = 15
    restaurant_1.set_number_served()

