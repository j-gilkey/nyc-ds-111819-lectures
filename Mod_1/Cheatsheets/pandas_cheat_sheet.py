import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
'dates': ['2019-05-07', '2019-07-13', '2019-11-23', '2019-04-20', '2019-06-08', '2019-10-20', '2019-10-14', '2019-07-17', '2019-02-23', '2019-09-13']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data , index=labels)

#COPYING A DATAFRAME

"""
#a deep copy creates an actual copy of the dataframe instead of another pointer
df_copy = df.copy(deep = True)
"""

#EXPLORATION METHODS
"""
#first 5 rows
print(df.head())

#overview
df.info()

#see index info
print(df.index)

#see list of column names
print(df.columns)

#see column data types
print(df.dtypes)

#see dataframe shape
print(df.shape)
"""

#SELECTION with .iloc() and .loc()
"""
#select all rows and only the 3rd column
print(df.iloc[:, 2])

#select first 3 rows and all columns
print(df.iloc[:3])

#select all rows and only the column score
print(df.loc[:, 'score'])
print(df.score)

#select rows 3 - 5 and only columns 'score' and 'attempts'
print(df.iloc[3:6][['score', 'attempts']])
"""

#SELECTION TIPS AND TRICKS
"""
#get value counts for column name
print(df['attempts'].value_counts())

#Percentage distribution
print(df['attempts'].value_counts(normalize = True))
"""

#FILTERING
"""
#filter based on single conditional
attempts_over_2 = df[df['attempts'] > 2]
print(attempts_over_2)

#filter based on multiple conditionals
attempts_under_2_score_over_15 = df[(df['attempts'] < 2) & (df['score'] > 15)]
print(attempts_under_2_score_over_15)

#filtered on NaN values
missing_score = df[df['score'].isna()]
print(missing_score)
"""

#DATA CLEANING

#replace values based on multiple conditionals
#NOTE that you must map every value else they will defualt to NaN
#print(df)
#df['qualify'] = df['qualify'].map({'yes': True, 'no' : False})
#print(df)

#second and better way
print(df)
map_dict = {'yes': True, 'no' : False}
df['qualify'] = df['qualify'].replace(map_dict)
print(df)

#remove rows based on NaN values in ['score']
#print(df)
df = df.dropna(subset = ['score'])
#print(df)

#remove rows based on a filter

#clean whitespace off column names
df.columns = [column.strip() for column in df.columns]

#change ['attempts'] to a float
df['attempts'] = df['attempts'].astype(float)
#print(df['attempts'].dtype)

#and back again
df['attempts'] = df['attempts'].astype(int)
#print(df['attempts'].dtype)

#convert ['dates'] from string to datetime
df['dates'] = pd.to_datetime(df['dates'])
#print(df['dates'].dtype)
