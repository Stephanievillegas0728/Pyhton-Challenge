import os
import pandas as pd
import numpy as np
import csv

df = pd.read_csv("budget_data.csv")
df


print("Final Analysis")
count1 = df['Date'].count()
sum1 = df['Profit/Losses'].sum()
mean1 = df['Profit/Losses'].mean()
max1 = df['Profit/Losses'].max()
min1 = df['Profit/Losses'].min()

print('Total Months: ' + str(count1))
print('Total: ' + str(sum1))
print('Average Change: ' + str(mean1))
print('Greatest Increase In Profits:Feb-2012 ' + str(max1))
print('Greatest Decrease In Profits: Sep-2013 ' + str(min1))
