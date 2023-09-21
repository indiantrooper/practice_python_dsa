import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Trapping rain water array problem. 
rain = [3,0,2,0,4]
n = len(rain)
#plot how the containers will look like
X_axis = np.arange(n))
plt.bar(X_axis,rain,width=1)
plt.show()

# Logic: If we calculate water[i] for i in index (array); water[i]= -array[i] + min(Left[i],right[i])
# where Left[i] and right[i] are the highest bars on either side of the ith block

water = 0
left =[0]*n
left[1]=rain[0]
right = [0]*n
right[n-1]=0

for i in range(2,n):
    left[i]=max(left[i-1],rain[i-1])

for j in range(n-2,0,-1):
    right[j]=max(right[j+1],rain[j+1])

for i in range(0,n):
    if(min(left[i],right[i])-rain[i]>0):
        water+=min(left[i],right[i])-rain[i]
        print(water)

print("Total water stored =", water,"units")