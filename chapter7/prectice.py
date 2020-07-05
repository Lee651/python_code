places = {}

active = True

while active :
    name = input("what is your name? ")
    place = input("If you could visit one place in the world,where would you go? ")

    places[name] = place

    answer = input("would you want to visit one place? (yes/no) ")
    if answer == "no":
        active = False

print("\n---Poll results---")
for name,place_1 in places.items():
    print(name + " " + "would go to" + " " + place_1)