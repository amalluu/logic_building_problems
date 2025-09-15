# Check if two arrays are rotations of each other

arr1 = list(map(int, input("Enter first array separated by space: ").split()))
arr2 = list(map(int, input("Enter second array separated by space: ").split()))

n1 = len(arr1)
n2 = len(arr2)

# Step 1: If lengths are different, they cannot be rotations
if n1 != n2:
    print("Not Rotations")
else:
    # Step 2: Make a temp array by joining arr1 with itself
    temp = arr1 + arr1
    
    # Step 3: Check if arr2 appears inside temp
    is_rotation = False
    for i in range(len(temp) - n2 + 1):
        if temp[i:i+n2] == arr2:
            is_rotation = True
            break
    
    # Step 4: Print result
    if is_rotation:
        print("Yes, they are rotations of each other")
    else:
        print("No, they are not rotations")
