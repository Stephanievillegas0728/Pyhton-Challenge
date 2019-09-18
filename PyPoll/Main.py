import os
import pandas as pd
import numpy as np
import csv

path is from my local repository
df = pd.read_csv (r"C:\Users\Stephanie Villegas\Documents\UA-PHX-DATA-PT-08-2019-U-C\02-Homework\Resources\PyPoll_Resources_election_data.csv")
print (df)




total_votes = len(df.index)
count = df.Candidate.value_counts()
pd.options.display.float_format = '{:.2f}%'.format
percent = (df.Candidate.value_counts()/len(df.index))*100
df2 = pd.DataFrame({'Percent': percent, 'Count': count})
winner = df.Candidate.mode().values

print("Election Results")
print('-----------------------------')
print('Total Votes: ' + str(total_votes))
print('-----------------------------')
print(df2.to_string(header=None))
print('-----------------------------')
print('Winner' + str(winner))
print('-----------------------------')

