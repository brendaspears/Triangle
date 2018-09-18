size=int(input("Enter the length of the triangle:"))
for i in range(0,size):
    numberOfStars=i+1
    for j in range(0,numberOfStars):
        print ("*",end="")
    print("\n")