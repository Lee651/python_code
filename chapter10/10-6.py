print("Enter 'q' to quit.")
while True:
    first_number = input("please input the fitst number: ")
    if first_number == 'q':
        break
   
    second_number = input("please input the second number: ") 
    if second_number == 'q':
        break
  
    try:
        F_number = int(first_number)
        S_number = int(second_number)
    except ValueError:
        print("You don't enter numbers")
    else:
        sum = F_number + S_number
        print(sum)