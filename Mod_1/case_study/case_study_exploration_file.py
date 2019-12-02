import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 100)

case_study = pd.read_csv('case_study.csv', index_col = 'Unnamed: 0')

print(case_study.head())
