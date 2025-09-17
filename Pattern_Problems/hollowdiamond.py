# Hollow Diamond Star Pattern


n =5
for row in range(n):

    print(" " * (n-row-1),end="")
    print("*", end="")
    
    if (row>0):
        print(" " *(row * 2),end="")
        print("*", end="")
        
        
    print()


for row in range(n-2, -1, -1):#n-2 = start value(3),-1 = stop value(stop BEFORE reaching -1),-1 = step value(decrease by 1 each time)

    print(" " * (n-row-1), end="")
    print("*", end="")
    
    if (row > 0):
        print(" " *(row * 2), end="")
        print("*", end="")
    
    print()