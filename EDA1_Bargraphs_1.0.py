

import pandas as pd
import datetime
import plotnine
import numpy as np
import matplotlib.pyplot as plt

a = pd.read_csv('data/Data_jobs.csv')
b =a.copy()


# Bargraphs 1.0 MIN
c=b.pivot_table(values='Salary', columns='Job', index='Year', aggfunc='min')
c.loc['MIN']= c.mean()
d=c.copy()

c = c.drop('MIN')
plt.close('all')
c.plot(kind='bar')

#EDA1 Bargraphs 1.1 Median
c=b.pivot_table(values='Salary', columns='Job', index='Year', aggfunc='median')
c.loc['MEDIAN']= c.mean()
d= pd.concat([d,c], ignore_index=False)

c = c.drop('MEDIAN')
plt.close('all')
c.plot(kind='bar')

#EDA1 Bargraphs 1.2 Mean
c=b.pivot_table(values='Salary', columns='Job', index='Year', aggfunc='mean')
c.loc['MEAN']= c.mean()
d= pd.concat([d,c], ignore_index=False)

c = c.drop('MEAN')
plt.close('all')
c.plot(kind='bar')


#EDA1 Bargraphs 1.3 Max+++
c=b.pivot_table(values='Salary', columns='Job', index='Year', aggfunc='max')
c.loc['MAX']= c.mean()
d= pd.concat([d,c], ignore_index=False)

c = c.drop('MAX')
plt.close('all')
c.plot(kind='bar')
#plt.show()

#EDA 13
d.reset_index(inplace=True)
e=d[ d['Year'].isin(['MIN','MEDIAN','MEAN', 'MAX']) ]
f=pd.melt(e, id_vars='Year')
f.columns=[ 'paramcd', 'job', 'aval']
f['aval'] = f['aval'].astype(int)
f['avalu'] = 'USD'
f['paramtyp']='DERIVED'
f['srcdom'] = 'DATA JOBS'

#f.to_csv('C:/Users/USUARIO/projects/python/work/data/EDA1_Bargraphs_1.0.csv', sep = ',', index=True)


