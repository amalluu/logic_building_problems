#Implement a basic string compression algorithm

s = input("Enter a String: ")
result = ""
count = 1   # to count repeats

for i in range(1, len(s)):
    if s[i] == s[i-1]:       # if current same as previous
        count += 1
    else:
        result += s[i-1] + str(count)  # add previous char + its count
        count = 1                      # reset count

# add last character + its count
result += s[-1] + str(count)

# check compressed length
if len(result) < len(s):
    print("Compressed:", result)
else:
    print("Original:", s)
