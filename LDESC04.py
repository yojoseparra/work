
import pandas as pd
from datetime import datetime
from plotnine import *
from plotnine.mapping.evaluation import reorder
import numpy as np
import matplotlib.pyplot as plt

a = pd.read_csv('C:/Users/USUARIO/projects/python/portfolio/work/data/Data_Jobs.csv')
a.drop([ 'level_0'], axis=1, inplace=True)
# We want to calculate dataset variables by groups#
c=a.groupby(['Country', 'Skills']).size().reset_index(name='n')
e =pd.merge(a, c, on=['Country', 'Skills'], how='left').sort_values(by=['Country', 'Skills'])

def gettots(x):
 out = {}
 out['mean'] = x.mean()
 return pd.Series(out)


f=a.groupby(['Country', 'Skills'])['Salary'].apply(gettots)
f=f.unstack()
f.reset_index(inplace=True)

g =pd.merge(e, f, on=['Country', 'Skills'], how='left').sort_values(by=[ 'mean','Skills', 'Country'], ascending=False)


h=g[['Skills', 'Country', 'n', 'mean', 'Job']].copy()


h.reset_index(inplace=True)
h=h.drop('index', axis=1)
i =h[h['n'] > 0 ].copy()


j=i.drop_duplicates().copy()
j['mean']= j['mean']/1000
j['mean']= j['mean'].round(0)


j.to_csv('data/LDESC04.csv', sep = ',', index=False)