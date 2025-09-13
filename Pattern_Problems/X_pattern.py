n = 8

for row in range(n):
    for col in range(n):
        if row == col:
            print ("*", end="")
        elif row + col == n-1:
            print("*",  end="")
        print(" ", end="")
    print()