import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
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

#select all rows and only the 3rd column
print(df.iloc[:, 2])

#select first 3 rows and all columns
print(df.iloc[:3])

#select all rows and only the column score
print(df.loc[:, 'score'])
print(df.score)

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
"""
#replace values based on multiple conditionals
#note that this alters the original table
#ALSO note that you must map every value else they will defualt to NaN
print(df)
df['qualify'] = df['qualify'].map({'yes': True, 'no' : False})
print(df)

#remove rows based on NaN values

#remove rows based on a filter

"""
