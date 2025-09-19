#Count the frequency of each character in a string.


def char_count(str):
    freq={}

    for char in str:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1

    #print(freq)

    # .items() → gives all key–value pairs as tuples

    for ch, count in freq.items():
        print(f"{ch} → {count}")
        
str= input("Enter the string: ")
char_count(str)