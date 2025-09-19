#Find the first non-repeating character in a string.

def non_repeat(str):
    freq={}

    for char in str:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
        
    for ch in str:
        if freq[ch]==1:
            print(f"First non-repeating character: {ch}")
            return
    print("not any")
str= input("Enter the string: ")
non_repeat(str)