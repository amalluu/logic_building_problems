'''

* * * * *
*     *
*   *
* *
*


0 0 5
1 3 2
2 2 2
3 1 2
4 0 1
'''
n = 5
for r in range(n):
    if r == 0:
        print("* " * n)   # top row
    elif r == n - 1:
        print("*")        # last row
    else:
        print("*", end="")  # left star
        for space in range(2*(n-r-1) - 1):
            print(" ", end="")
        print("*")          # right star
