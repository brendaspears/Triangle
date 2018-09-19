size=int(input("Enter the length of the triangle:"))
x=0
for i in range(0,size):
    numberOfStars=i+1
    numberOfSpaces = size - numberOfStars
    for i in range(0,numberOfSpaces):
        print(" ",end="")
    for i in range(0,numberOfStars+x):
        print("*",end="")
    x=x+1
    print("\n")