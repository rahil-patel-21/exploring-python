import pandas as pd
import re

# Get Data frame from csv
df = pd.read_csv('pokemon_data.csv')
#pd.read_csv('pokemon_data.csv',chunksize=1000)

# Get Data frame from xlsx
#df = pd.read_excel('pokemon_data.xlsx')

# Get Data frame from txt
# delimiter formats the text data
#df = pd.read_csv('pokemon_data.txt', delimiter='\t')

# Drops the row if null value in any column and returns new data frame
# df = df.dropna()

# Drops the row if null value in perticular column
#df.dropna(subset=['Value'], inplace = True)

# Gives default value to cell if null value
#df.fillna(0,inplace=True)

# removing duplicates
#df.drop_duplicates(inplace = True)

# First n rows
#firstRows = df.head(3)
# Last n rows
#lastRows = df.tail(3)

# Name of all columns
#columns=df.columns
# Drops the column
#df = df.drop(columns=['HP'])

# Get row data by index
#rows=df.iloc[2:5]

# Get cell data by x,y
#cell=df.iloc[3,2]

# Get row by row data
# rowsData = df.iterrows()
# for index, row in rowsData:
#     print(index, row['Name'])

# Data Basic Info
#basicDescription=df.describe()

# Sorting (PENDING)
# df.sort_values('Name',ascending=False)
# df.sort_values(['Name', 'Type 1'],ascending=False)
# df.sort_values(['Name', 'Type 1'],ascending=[0,1])

#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Speed']
# df['Total'] = df.iloc[:, 4:10].sum(axis=1) 
# 1 means horizontal 0 means vertical

# Re - arranging the columns
# cols = list(df.columns)
# df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

# print(df)

# Save Data frame
#df.to_csv('updated.csv', index=False)
#df.to_csv('updated.txt', sep='\t')
#df.to_excel('updated.xlsx')
# df.reset_index(drop=True, inplace=True)

# Filtering the data
#df = df.loc[(df['HP'] == 50) | (df['Type 1'] == 'Fire')]
#df = df.loc[~(df['HP'] == 50)]
# df = df.loc[df['Name'].str.contains('chari|maw', flags=re.I)]
#df = df.loc[df['Name'].str.contains('pi[a-z]*', flags=re.I)]

# Conditional changes
# df.loc[df['Type 1'] == 'Fire', 'Type 2'] = 'Poison'
#df.loc[df['Type 1'] == 'Fire', ['Type 1','Type 2']] = 'Fire'
# df.loc[df['Type 1'] == 'Fire', ['Type 1','Type 2']] = ['Water', 'Pani']

# Groupby
# df = df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False)



print(df)