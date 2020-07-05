def E(A,B):
    while A:
        F = A.pop()
        print("Printing model: " + F)
        B.append(F)

def C(B):
    print("The followig models have been printed:")
    for D in B:
        print(D)


#A = ["a", "b", "c"]
#B = [ ]

#E(A, B)
#C(B)