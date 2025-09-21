#Check if a string is a palindrome.

#s[start:end:step] - slicing

str = input("Enter the string: ")
str= str.lower()

rev= str[::-1] # reverse
print(f"reverse string is: {rev}")

if rev==str:
    print("Yes, It is a pallindrome")
else:
    print("No, It is not a pallindrome")
