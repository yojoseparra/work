

import pandas as pd
import datetime
import plotnine
import numpy as np
import matplotlib.pyplot as plt

a = pd.read_csv('data/Data_jobs.csv')

a.drop([ 'level_0', 'Skills'], axis=1, inplace=True)


b=a.copy()

b.drop_duplicates(inplace = True)



# Bargraphs .3.1 MIN
c=b.pivot_table(values='Salary', columns='Job', index='Country', aggfunc='min')
c.loc['MIN']= c.mean()
c['paramcd'] = 'MIN'

d=c.copy()

c = c.drop('MIN')
plt.close('all')
c.plot(kind='bar')

#EDA1 Bargraphs 3.2 Median
c=b.pivot_table(values='Salary', columns='Job', index='Country', aggfunc='median')
c.loc['MEDIAN']= c.mean()
c['paramcd'] = 'MEDIAN'
d= pd.concat([d,c], ignore_index=False)

c = c.drop('MEDIAN')
plt.close('all')
c.plot(kind='bar')

#EDA1 Bargraphs 3.2 Mean
c=b.pivot_table(values='Salary', columns='Job', index='Country', aggfunc='mean')
c.loc['MEAN']= c.mean()
c['paramcd'] = 'MEAN'
d= pd.concat([d,c], ignore_index=False)

c = c.drop('MEAN')
plt.close('all')
c.plot(kind='bar')
plt.show()

#EDA1 Bargraphs 3.3 Max+++
c=b.pivot_table(values='Salary', columns='Job', index='Country', aggfunc='max')
c.loc['MAX']= c.mean()
c['paramcd'] = 'MAX'
d= pd.concat([d,c], ignore_index=False)

c = c.drop('MAX')
plt.close('all')
c.plot(kind='bar')


c=b.pivot_table(values='Salary', columns='Job', index='Country', aggfunc='std')
c.loc['STD']= c.mean()
c['paramcd'] = 'STD'
d= pd.concat([d,c], ignore_index=False)

c = c.drop('STD')
plt.close('all')
c.plot(kind='bar')
#EDA 13
d.reset_index(inplace=True)
e=d.copy()

f=pd.melt(e, id_vars=['Country','paramcd' ])
f=f.dropna()

f.columns=[ 'country','paramcd', 'job', 'aval']
f['aval'] = f['aval'].astype(int)
f['avalu'] = 'USD'
f['srcdom'] = 'DATA JOBS'
f['paramtyp'] = np.where(f['country'].str.contains('MIN|MEAN|MEDIAN|MAX|STD'), 'DERIVED', '')
f['country'] = np.where(f['country'].str.contains('MIN|MEAN|MEDIAN|MAX|STD'),'' ,f['country'] )

g=f.copy()

print(g.head(100).to_string())
g = f.sort_values(['country', 'job', 'paramcd'])

g.to_csv('C:/Users/USUARIO/projects/python/portfolio/work/data/EDA1_Bargraphs_3.0.csv', sep = ',', index=False)




