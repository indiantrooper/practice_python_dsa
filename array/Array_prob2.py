import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sb

#Best time to buy / sell a stock
'''Given an array of time series of stock price; calculate
    1. Maximum profit in the range when one transaction is allowed
    2. Maximum profit in the range when multiple transactions are allowed
'''
price = [4,1,2,5,2,0.4,3,6,4,5,2,7,0.6] 
# Case 1: only one transaction is allowed
def calcMaxprofit(price):
    
    entryPrice = price[0]
    maxProfit = 0

    for i in range(1,len(price)):
        if(price[i]<entryPrice):
            entryPrice = price[i]
            #print(entryPrice)
        else:
            if(price[i]-entryPrice > maxProfit):
                maxProfit = price[i]-entryPrice
                #print(maxProfit)
    return(entryPrice,maxProfit)

# Case 2: multiple transactions are allowed. calculate total profit
def calcTotalprofit(price):
    entryPrice = price[0]
    totalProfit = 0
    maxProfit = 0
    
    for i in range(1,len(price)):
        if((price[i]<entryPrice) or (price[i]<price[i-1])):
            totalProfit +=maxProfit
            maxProfit = 0
            entryPrice=price[i]
            #print(totalProfit)
        else:
            if(price[i]-entryPrice>maxProfit):
                maxProfit = price[i]-entryPrice
    totalProfit +=maxProfit
    return(totalProfit)

print(calcMaxprofit(price),calcTotalprofit(price))