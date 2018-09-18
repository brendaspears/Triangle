size=int(input("Enter the length of the triangle:"))
for i in range(0,size):
    numberOfStars=i+1
    numberOfSpaces = size - numberOfStars
    for i in range(0,numberOfSpaces):
        print(" ",end="")
    for i in range(0,numberOfStars):
        numberOfSpaces=size-numberOfStars
        print("*",end="")
    print("\n")