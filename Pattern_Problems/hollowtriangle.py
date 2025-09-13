#HOLLOW RIGHT ANGLED TRIANGLE

'''

*
* *
*   *
*     *
* * * * *

Row 0: 1 star
Row 1: star, space(1), star
Row 2: star, space(3), star
Row 3: star, space(5), star
Row 4: full row of stars


'''
n= 5
for r in range(n):
    if r==0:
        print("*")
    elif r== n-1:
        for star in range(n):
            print("*",end=" ")
        print()
    else:
        print("*",end="")
        for space in range(2*r-1):
                print(" ",end="")
        print("*")
    