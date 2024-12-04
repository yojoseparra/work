



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
c.loc['MIN COUNTRY AVG']= c.mean()

c['paramcd'] = 'MIN'

d=c.copy()
print(d.to_string())
c.info()

#EDA1 Bargraphs 3.2 Median
c=b.pivot_table(values='Salary', columns='Job', index='Country', aggfunc='median')
c.loc['MEDIAN COUNTRY AVG']= c.mean()
c['paramcd'] = 'MEDIAN'
d= pd.concat([d,c], ignore_index=False)
print(d.to_string())
c.info()



#EDA1 Bargraphs 3.2 Mean
c=b.pivot_table(values='Salary', columns='Job', index='Country', aggfunc='mean')
c.loc['MEAN COUNTRY AVG']= c.mean()
c['paramcd'] = 'MEAN'
d= pd.concat([d,c], ignore_index=False)

print(d.to_string())
c.info()


#EDA1 Bargraphs 3.3 Max+++
c=b.pivot_table(values='Salary', columns='Job', index='Country', aggfunc='max')
c.loc['MAX COUNTRY AVG']= c.mean()
c['paramcd'] = 'MAX'
d= pd.concat([d,c], ignore_index=False)

print(d.to_string())
c.info()



c=b.pivot_table(values='Salary', columns='Job', index='Country', aggfunc='std')
c.loc['STD COUNTRY AVG']= c.mean()
c['paramcd'] = 'STD'
d= pd.concat([d,c], ignore_index=False)

print(d.to_string())
c.info()



c=b.pivot_table(values='Salary', columns='Job', index='Country', aggfunc='count')
#c= c.replace(to_replace=np.nan, value=0)
c.loc['N OVERALL']= c.sum()
c['paramcd'] = 'N'


d= pd.concat([d,c], ignore_index=False)

print(d.to_string())
d.info()

#EDA 13
d.reset_index(inplace=True)
e=d.copy()
e.head()



f=pd.melt(e, id_vars=['Country','paramcd' ])

f=f.dropna()




f.columns=[ 'param','paramcd', 'job', 'aval']
f['aval'] = f['aval'].astype(int)

def nfl(x):
    if x == 'N':
        ''
    elif x== 'N OVERALL':
        ''
    else:
        'USD'

f['avalu'] =  f['param'].apply(nfl)
f['srcdom'] = 'DATA JOBS'


df = pd.DataFrame({'Type':list('ABBC'), 'Set':list('ZZXY')})
conditions = [
    (df['Set'] == 'Z') & (df['Type'] == 'A'),
    (df['Set'] == 'Z') & (df['Type'] == 'B'),
    (df['Type'] == 'B')]

f['paramtyp'] = np.where( (f['param'] == 'MIN COUNTRY AVG') | (f['param'] == 'MEAN COUNTRY AVG')  | (f['param'] == 'MEDIAN COUNTRY AVG')  | (f['param'] == 'MAX COUNTRY AVG')  | (f['param'] == 'STD COUNTRY AVG')   | (f['param'] == 'N OVERALL')    ,f['param'] ,     ""                  )

f['param'] = np.where( (f['param'] == 'MIN COUNTRY AVG') | (f['param'] == 'MEAN COUNTRY AVG')  | (f['param'] == 'MEDIAN COUNTRY AVG')  | (f['param'] == 'MAX COUNTRY AVG')  | (f['param'] == 'STD COUNTRY AVG')   | (f['param'] == 'N OVERALL')    ,  ""   ,   f['param']                )




f.to_csv('C:/Users/USUARIO/projects/python/portfolio/work/data/EDA1_Bargraphs_3.2.csv', sep = ',', index=False)






