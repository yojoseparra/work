

from datetime import datetime
from plotnine import *
from plotnine.mapping.evaluation import reorder
import numpy as np
import matplotlib.pyplot as plt


import pandas as pd


a = pd.read_csv('data/Data_Jobs.csv')

a.drop([ 'level_0'], axis=1, inplace=True)
b = pd.read_csv('data/Data_Jobs_Subset.csv')
b = pd.merge(b, a, on=['index','Country', 'Job', 'Skills'], how='left').sort_values(by=['Country','Job', 'Skills'])



# We want to calculate dataset variables by groups
c=b.groupby(['Job', 'Country']).size().reset_index(name='Job_Country_Count')

b =pd.merge(b, c, on=['Job', 'Country'], how='left').sort_values(by=['Country','Job', 'Skills'])


# We ant to calculate dataset variable means
c=b.groupby(['Country', 'Job'])['Salary'].mean().reset_index(name='Country_Salary_Mean')

b =pd.merge(b, c, on=['Job', 'Country'], how='left').sort_values(by=['Country','Job', 'Skills'])



c=b.groupby(['Country', 'Job'])['Salary'].mean().reset_index(name='Salary')
d=b.groupby(['Country', 'Job']).size().reset_index(name='Job_Country_Count')
e =pd.merge(c,d, on=[ 'Country', 'Job'], how='left').sort_values(by=['Country','Job'])



(
    ggplot(b)
     + aes(y="Job", x="Salary", size="Job_Country_Count" , fill="Job_Country_Count")
    + geom_jitter(alpha=0.2)
    + geom_point(data=e, fill ='#A70267')
    + facet_wrap("Country", ncol=5)
    + scale_fill_gradient(low='#008C7A', high='#415B5E')
).draw(True)