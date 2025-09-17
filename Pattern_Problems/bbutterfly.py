'''

*      *
**    **
***  ***
********
********
***  ***
**    **
*      *


n=8
total rows = 2*n


'''

#top
n=4
for r in range(1,n+1):
    for star in range (r):
        print("*", end= "")
    
    for spaace in range(n-1-star):
        print(" ", end ="")
    
    for space in range (n-r):
            print(" ", end= "" )
    for staar in range(r):
            print("*", end= "")

    print()
    
print("*" * n + "*" * n)#middle

#bottom
for r in range(1,n+1):
    for star in range(n-r):
        print("*", end= "")
    for spaace in range(n-1-star):
        print(" ", end ="")

    for space in range (r):
        print(" ", end= "" )
    for star in range(n-r):
        print("*", end= "")
        
    print()
    

