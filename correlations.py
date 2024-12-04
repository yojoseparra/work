

from datetime import datetime


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd


a = pd.read_csv('data/Data_Jobs.csv')
a.drop([ 'level_0'], axis=1, inplace=True)
b=a[ [ "index","Job", "Salary", "Rate" ,"Company","job_skills",  "Skills",  "Country"] ]
b.head()

# Bargraphs .3.1 MIN
c=b.pivot_table(values='Salary', columns='Skills', index='Job', aggfunc='mean')

d=c.corr(method="pearson" ).round(2)
d.reset_index(inplace=True)
d.to_csv('data/correlations.csv', sep = ',', index=True)

#print(list(d.columns))d

#f.to_csv('data/correlations.csv', sep = ',', index=False)













