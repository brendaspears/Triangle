#Input the size of the square
size = int(input("Enter the size(odd)"))
#Look for the middle box
middle = size/2
#Make an empty square
array=[[for j in range (0,size)]for i in range (0,size)]
for i in range (0,size):
    for j in range (0,size):
        array[i][j]=0
noOfSquare = size * size
value = 1
horizontal = middle
vertical = 0
array[vertical][horizontal] = value
for k in range (0,noOfSquare):
    if horizontal != size and vertical != 0 :
        horizontal = horizontal + 1
        vertical = vertical - 1
