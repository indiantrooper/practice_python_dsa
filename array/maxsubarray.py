# Maximum subarray (Kadane's algo)
arr3 = [-2,1,-3,4,-1,2,1,-5,4]

n=len(arr3)
maxSum = 0
out_subarray =[]

#bruteforce O(N^2)
for i in range(0,n-1):
    temp = 0
    for j in range(i,n-1):
        temp += arr3[j]
        if temp>maxSum:
            maxSum=temp
#print("Maximum sum =",maxSum)

#optimal solution O(N) - sliding window approach

maxSub = arr3[0]
curSum = 0

for num in arr3:
    if curSum < 0:
        curSum = 0
    curSum += num
    if maxSub<curSum:
        maxSub = curSum
        
print(maxSub)