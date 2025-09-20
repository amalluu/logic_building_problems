#HOLLOW SQUARE PATTERN

n= 5
for r in range(n):
    if r==0 or r== n-1 :        # Top and bottom rows
        print("* " * n)
    else:               # Middle rows
        
        print("*", end=" ")        # Left star
        print("  " * (n - 2), end="")  # Spaces in between
        print("*")                 # Right star

 
 
'''
* * * * *
*       *
*       *
*       *
* * * * *

| Row | Spaces | Stars |
| --- | ------ | ----- |
| 0   | 0      | 6     |
| 1   | 4      | 2     |
| 2   | 4      | 2     |
| 3   | 4      | 2     |
| 4   | 4      | 2     |
| 5   | 0      | 6     |

'''
