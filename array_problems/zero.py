#Move all zeros in an array to the end.

arr= list(map(int, input("Enter no separated by spaces: ").split()))
zeroend=[]
num= 0

for i in range(len(arr)):
    if arr[i]!= 0:
        zeroend.append(arr[i])
    else:
        num=num+1
        
        #add it to the end of zeroend

if num==0:
    print("No zeroes")
else:
    zeroend.extend([0]*num)#--> [7, 2, 4, 3, 0, 0]
#zeroend.append([0]*num)#--> [7, 2, 4, 3, [0, 0]]
#zeroend.append(2*num)#--> [7, 8, 2, 6, 0] --- 0 * num -(0) will be appended at the end.

    print(zeroend)