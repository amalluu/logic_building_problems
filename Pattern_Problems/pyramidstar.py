#Pyramid Star

n= 5

for row in range(n):
    print(" " * (n-(row+1)), end="")
    print("* " * (row+1), end="")
    print()
