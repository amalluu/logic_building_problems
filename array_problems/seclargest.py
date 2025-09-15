#Find the second largest element in an array.


arr = list(map(int,input("Enter numbers separated by space: ").split()))

if len(arr) < 2:
    print("Array must have at least two elements")
          
else:
    '''
    max_pos = arr.index(max(arr))
    remove= arr.pop(max_pos)
    second_max= max(arr)

    print(second_max)
    '''
    largest =max(arr)
    arr=[x for x in arr if x!= largest]
    if not arr:
        print("No second largest element (all elements equal)")
    else:
        second_max= max(arr)
        print(second_max)


