#Find longest palindromic substrings in a string

str=input("Enter the string: ")
longest=""
n = len(str)
for i in range(n):
    for j in range(i+1,n+1):
        sub= str[i:j]
        if sub == sub[::-1] and len(sub)>len(longest):
            longest= sub

print(longest) # at the end, contains the longest palindrome