#Find all pairs in an array whose sum equals a target.

arr = list(map(int,input("Enter numbers separated by space: ").split()))
target= int(input("Enter your target number: "))
found = False
for i in range(len(arr)):
    for j in range(i+1,len(arr)):

        
        if arr[i]+ arr[j]==target:
            print(f"Yes, pair found:({arr[i]},{arr[j]})")
            found = True  # mark that we found at least one

if not found:
    print("No pairs found with the given target")
       
    
