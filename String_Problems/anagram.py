
str1= input("Enter the string1: ")
str2= input("Enter the string2: ")

if len(str1)!= len(str2):
    print("Not an anagram")

if sorted(str1)== sorted(str2):
    print("Yes, It is anagram")
else:
    print("No, It is not anagram")
    