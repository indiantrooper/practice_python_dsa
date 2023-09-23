# Chocolate distribution problem
'''
Given an array of N integers where each value represents the number of chocolates in a packet. 
Each packet can have a variable number of chocolates. 
There are m students, the task is to distribute chocolate packets such that: 
1. Each student gets one packet.
2. The difference between the number of chocolates in the packet with maximum chocolates and 
   the packet with minimum chocolates given to the students is minimum.
'''

inputArray = [5,3,6,2,4,10,11,7,9,9]
m = 4 #input as number of students
n = len(inputArray)

temp = sorted(inputArray)

minDiff=temp[n-1]-temp[0]
print("Max difference:",minDiff)

j = 0
for i in range(0,n-m+1):
    if(temp[i+m-1]-temp[i]<minDiff):
        minDiff = temp[i+m-1]-temp[i]
        j = i
    i+=1

print("Minimum difference =",minDiff)
print("Distribution as follows")
for i in range(j,j+m):
    print(temp[i])
    i+=1
