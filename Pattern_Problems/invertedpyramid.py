#Inverted Pyramid Star Pattern
'''
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''

n= 5

for row in range(n):
    print(" " * row, end="")
    print("*" * (((n-row)*2)-1), end="")
    print()

