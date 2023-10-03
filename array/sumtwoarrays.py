# An array represents an integer. Eg. Arr = [1,2,3] represents 123
# Find sum of two such arrays and return output as array. Inputs can have different lengths. All elements are positive int
# Eg. A = [9,9], B = [3] => A + B = [1,0,2]
# A=[1,4], B  = [1,2] => A+B = [2,6]

def sumTwoArrays(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    n = max(n1,n2)
    outArr=[0]*(n+1)
    carry = 0
    temp1 = 0
    temp2 = 0
    for i in range(n-1,-1,-1):
        if(n1>=n2):
            temp1 = arr1[i]
            if(i-n1+n2+1>0):
                temp2 = arr2[i-(n1-n2)]
            else:
                temp2 = 0
        else:
            temp2 = arr2[i]
            if(i-n2+n1+1>0):
                temp1 = arr1[i-(n2-n1)]
            else:
                temp1 = 0
        
        temp = temp1+temp2+carry
        
        if(temp//10==0):
            outArr[i+1] = temp
            carry = 0
        else:
            outArr[i+1] = temp%10
            carry = temp//10
    
    if (carry==0):
        outArr.remove(0)
    else:
        outArr[0]=carry
    return outArr


input1 = [1,2,3,4]
input2 = [9,9,9,4]

c = sumTwoArrays(input1, input2)
for i in c:
    print(i,end=" ")
