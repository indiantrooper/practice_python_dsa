import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Trapping height water array problem. 
height = [3,0,2,0,4]
n = len(height)
#plot how the containers will look like
X_axis = np.arange(n)
plt.bar(X_axis,height,width=1)
plt.show()

# Logic: If we calculate water[i] for i in index (array); water[i]= -array[i] + min(Left[i],right[i])
# where Left[i] and right[i] are the highest bars on either side of the ith block

water = 0
left =[0]*n
left[1]=height[0]
right = [0]*n

for i in range(1,n-1):
    left[i+1]=max(left[i],height[i])

for j in range(n-2,0,-1):
    right[j]=max(right[j+1],height[j+1])

for i in range(0,n):
    if(min(left[i],right[i])-height[i]>0):
        water+=min(left[i],right[i])-height[i]
        print(water)

print("Total water stored =", water,"units")