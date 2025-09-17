#Merge two sorted arrays into a single sorted array.

arr1= list(map(int,input("Enter number separated by space: ").split()))
arr2= list(map(int,input("Enter number separated by space: ").split()))

merge=[]

#list.sort()
'''
Sorts the list in place (modifies the original list).
Returns None (not a new list).
'''

#sorted(list)- Returns a new sorted list, leaves the original unchanged
#sorted1=sorted(arr1)
#sorted2=sorted(arr2)

arr1.sort()
arr2.sort()

print(arr1)
print(arr2)

merge= arr1+arr2
unique=list(set(merge))
unique.sort()
print(unique)