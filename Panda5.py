import pandas as pd

df = pd.read_csv('OctoberCSV.csv')

#df['Column'].value_counts()
#Counts how many times x in column

print("Terminal Count:")
df['SITE'].value_counts(ascending=True)

print("Message Type Count:")
df['MESSAGE'].value_counts(ascending=True)

print("Reason Count:")
df['REASON'].value_counts(ascending=True)

print("Root cause Count:")
df['CAUSE'].value_counts(ascending=True)


## ^ but with site occurances

data = {
  "calories": [420, 420, 390],
  "duration": [50, 50, 45]
}
df['calories'].value_counts(ascending=True)
myvar = pd.DataFrame(data)
