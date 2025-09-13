#Reverse an array in place.



arr = list(map(int,input("Enter numbers separated by space: ").split()))
start=0
n= len(arr)
end= n-1

while (start< end):
    arr[start],arr[end]=arr[end],arr[start]
    #arr[end]=arr[start]
    start= start+1
    end= end-1
print(arr)