
age = "enter 'quit' to end the program."

active = True

while active:
    age = input("please enter your age: ")
    if age == 'quit':
        active == False
    else :
        if age < 3:
            print("The ticket is free.")
        elif age <= 12:
            print("The ticket is $10.")
        else:
            print("The ticket is $15.")
        
        
