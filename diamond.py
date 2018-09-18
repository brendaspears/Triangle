size=int(input("Enter the length of the diamond:"))
x=0
y=int(size/2)+1
for i in range(0,size):
    numberOfStars=i+1
    numberOfSpaces = size - numberOfStars
    for j in range(0,numberOfSpaces):
        print(" ",end="")
    for k in range(0,numberOfStars+x):
        print("*",end="")
    x=x+1
    print("\n")
for p in range(0,size):
    noOfSpaces=p+1
    noOfStars=size-noOfSpaces
    for q in range(0,noOfSpaces):
        print(" ",end="")
    for v in range(0,noOfStars+y):
        print("*",end="")
    y=y-1
    print("\n")

# hi i was here