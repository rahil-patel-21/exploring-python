import pandas as pd

# Data frame
df = pd.read_csv('demo.csv')

# Drops the row if null value in any column and returns new data frame
# df = df.dropna()

# Drops the row if null value in perticular column
df.dropna(subset=['Value'], inplace = True)

# Gives default value to cell if null value
df.fillna(0,inplace=True)

# removing duplicates
df.drop_duplicates(inplace = True)
print(df)