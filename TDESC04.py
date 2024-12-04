





import pandas as pd
import datetime
import plotnine

import matplotlib.pyplot as plt
a=pd.read_csv('data/Data_Jobs.csv')
#a.set_index("index", inplace=True)
import numpy as np

a.drop([ 'level_0', 'Skills'], axis=1, inplace=True)
a.drop_duplicates(inplace = True)



def gettots(x):
 out = {}
 out['min'] = x.min()
 out['qr1'] = x.quantile(0.25)
 out['med'] = x.median()
 out['qr3'] = x.quantile(0.75)
 out['max'] = x.max()
 out['mean'] = x.mean()
 out['std'] = x.std()

 return pd.Series(out)

b=a.groupby(['Country', 'Job' ])['Salary'].apply(gettots)

b=b.unstack()
b['iqr'] = b['qr3'] -b['qr1']
b=b.apply(pd.to_numeric)/1000
b=b.round(1)

b=pd.DataFrame(b)
b=b.fillna(0)







b['col1'] = b['med'].astype(int).astype(str) + ' ('+ b['iqr'].astype(int).astype(str) + ')'
b['col2'] = b['mean'].astype(int).astype(str) + ' ('+ b['std'].astype(int).astype(str) + ')'

b.reset_index(inplace=True)



c=b.melt(id_vars =['Country', 'Job'], var_name='param', value_name='aval')
c['Parameter'] = c['param'].apply(str.upper)



d=a.pivot_table(values='Salary', columns='Job', index='Country', aggfunc='size')
d.reset_index(inplace=True)
e=d.melt(id_vars =['Country'], var_name='Job', value_name='aval')

#d= pd.concat([d,c], ignore_index=False)
e['param'] = 'n'
e['Parameter'] = 'N'

f = e[['Country', 'Job',  'aval','param', 'Parameter']]
g= pd.concat([c,f], ignore_index=False)


#c= c[c['aval'] != 0]

g.to_csv('C:/Users/USUARIO/projects/python/portfolio/work/data/TDESC04.csv', sep = ',', index=False)






