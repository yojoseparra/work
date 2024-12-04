
import pandas as pd
from datetime import datetime
from plotnine import *
from plotnine.mapping.evaluation import reorder
import numpy as np
import matplotlib.pyplot as plt

a = pd.read_csv('data/Data_Jobs.csv')

skills =['aws'
,'spark'
,'airflow'
,'snowflake'
,'python'
,'looker'
,'databricks'
,'sql'
,'go'
,'pandas'
,'azure'
,'gcp'
,'redshift'
,'java'
,'bigquery'
,'kafka'
,'pyspark'
,'oracle'
,'docker'
,'scala'
,'git'
,'pytorch'
,'tensorflow'
,'kubernetes'
,'numpy'
,'terraform'
,'postgresql'
,'hadoop'
,'scikit-learn'
,'mysql'
,'tableau'
,'jira'
,'sql server'
'gdpr' ]


b=a[ a['Skills'].isin(skills) ]
#c= b[["index","Country","Job", "Skills"]]
#d = c.drop_duplicates().sort_values(by=["Country","Job", "Skills"], ascending=False)
j = b.copy()

# knowing how to cut categories
pd.qcut(j['Salary'], q=5,duplicates='drop')
'''
Categories (5, interval[float64, right]): [(43.999, 98.0] < (98.0, 110.0] < (110.0, 121.0] < (121.0, 133.0] < (133.0, 256.0]]
'''
l = pd.qcut(j['Salary'], q=10,duplicates='drop')


labels = ["{0} - {1}".format(i, i + 30) for i in range(30, 260, 30)]

j["Group"] = pd.cut(j['Salary'], bins=8, right=False, labels=labels)

k=j.groupby([ 'Skills', 'Job', 'Group']).size().reset_index(name='Total')

k = k[k["Total"] > 0 ]
m = k[ k['Total' ] >0].sort_values(by=['Group', 'Total', 'Skills','Job'], ascending=False)




n=m.loc[ m['Group'] ==  '60 - 90', [ 'Total', 'Skills', 'Job'] ]
o=m.loc[ m['Group'] ==  '90 - 120', [ 'Total', 'Skills', 'Job'] ]
p=m.loc[ m['Group'] ==  '120 - 150', [ 'Total', 'Skills', 'Job'] ]
q=m.loc[ m['Group'] ==  '150 - 180', [ 'Total', 'Skills', 'Job'] ]
r=m.loc[ m['Group'] ==  '180 - 210', [ 'Total', 'Skills', 'Job'] ]
s=m.loc[ m['Group'] ==  '210 - 240', [ 'Total', 'Skills', 'Job'] ]
t=m.loc[ m['Group'] ==  '240 - 270', [ 'Total', 'Skills', 'Job'] ]

u = pd.merge(m,n, on = [ 'Skills','Job'] , how='left')
u.rename(columns={'Total_x':'T_Group', 'Total_y':'T6_9'}, inplace=True)


u = pd.merge(u,o, on = [ 'Skills','Job'] , how='left')
u.rename(columns={'Total':'T9_12'}, inplace=True)


u = pd.merge(u,p, on = [ 'Skills','Job'] , how='left')
u.rename(columns={'Total':'T12_15'}, inplace=True)


u = pd.merge(u,q, on = [ 'Skills','Job'] , how='left')
u.rename(columns={'Total':'T15_18'}, inplace=True)

u = pd.merge(u,r, on = [ 'Skills','Job'] , how='left')
u.rename(columns={'Total':'T18_21'}, inplace=True)


u = pd.merge(u,s, on = [ 'Skills','Job'] , how='left')
u.rename(columns={'Total':'T21_24'}, inplace=True)


u = pd.merge(u,t, on = [ 'Skills','Job'] , how='left')
u.rename(columns={'Total':'T24_27'}, inplace=True)

v = u[ ['Skills',  'T6_9', 'T9_12', 'T12_15', 'T15_18', 'T18_21', 'T21_24', 'T24_27', 'Job'] ]
w = v.drop_duplicates().sort_values(by=['T12_15', 'T9_12'], ascending=False)


w.to_csv('data/LDESC08.csv', sep = ',', index=False)


