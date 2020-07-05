#x = [num for num in range(1,1000001)]
#print(x)
#print(min(x))
#print(max(x))
#print(sum(x)) 

#x = [num for num in range(1,20,2)]
#print(x)

#x = [num**3 for num in range(1,11)]
#print(x)

#x =""
#for num in range(1,11):
#   num**=3
#   x+=str(num) + " " 
#print(x)

#x = []
#for num in range(3,30):
#    num**=3
#    x.append(num)
#print(x)

#x = [num**3 for num in range(1,11)]
#z = " "
#for y in x[-5:]:
#    z+=str(y) + " "
#print(z)


#x = [num for num in range(1,10000)]
#y = x[:10]
#print("the first ten items in the list are")
#print(y)

cars = ["audi","bmw","subaru","toyota"]

for x in cars:
    if x == "bmw":
        print(x.upper())

    else:
        print(x.title())

