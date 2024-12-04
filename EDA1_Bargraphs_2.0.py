import pandas as pd
import datetime
from plotnine import *
import numpy as np
import matplotlib.pyplot as plt


a = pd.read_csv('data/Data_jobs.csv')
b =a.copy()

# Determine order and create a categorical type

Job_List =b["Job"].value_counts().index.tolist()
Job_Cat = pd.Categorical(b["Job"], categories=Job_List)

# assign to a new column in the DataFrame
b= b.assign(Job_Cat=Job_Cat)


c=b.groupby(['Job']).size().reset_index(name='Job_Count')

d =pd.merge(b, c, on='Job', how='left')
Job_List = d["Job"].value_counts().index.tolist()[::-1]
c=c.sort_values(by='Job_Count', ascending=False)
print(c)

(
    ggplot(data=d)
    + geom_jitter(  aes( x ='Job' , y = 'Salary' , fill='Job_Count'  )  )
    + scale_x_discrete(limits=Job_List)
    + coord_flip()
    + labs(x='Jobs', y='Salary', title='')
    + scale_fill_gradient(low='#008C7A', high='#415B5E')
    + labs(fill= 'Count')
)

'''
0           Business Analyst        183
1             Cloud Engineer         85
2               Data Analyst       1258
4             Data Scientist       1167
5  Machine Learning Engineer        935
6        Senior Data Analyst        249
8      Senior Data Scientist        435
9          Software Engineer        389
'''
