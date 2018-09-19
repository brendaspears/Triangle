size = int(input("enter the size of your triangle"))
noOfStars = size
for i in range (0,size):
    noOfSpaces = i
    for j in range (0,noOfSpaces):
        print(" ",end="")
    for k in range(0,noOfStars):
        print("*",end="")
    print("\n")
    noOfStars = noOfStars - 1