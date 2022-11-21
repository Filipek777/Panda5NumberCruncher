import pandas as pd

df = pd.read_csv('OctoberCSV.csv')

#df['Column'].value_counts()
#Counts how many times x in column

print("Terminal Count:")
df['Terminal'].value_counts()

print("Message Type Count:")
df['Message Type'].value_counts()

print("Reason Count:")
df['Reason'].value_counts()

print("Root cause Count:")
df['Root cause Type'].value_counts()
