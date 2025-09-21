#Find palindromic substrings in a string

#Substrings
str= input("Enter the String: ")
sub=[]
n=len(str)
for i in range(n):
    for j in range(i+1,n+1):# runs from i+1 up to n (Python slicing excludes the end index → n+1)
        sub.append(str[i:j])# take substring from index i to j-1 and add to list
print(f"All substrings: {sub}")

# Find palindrome substrings
palindromes=[]
for substring in sub:
   
    if substring[::-1]==substring:
        palindromes.append(substring)
print(f"palindrome substrings are: {palindromes}")


