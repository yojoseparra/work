import pandas as pd
import datetime
import plotnine
import numpy as np
import matplotlib.pyplot as plt

a = pd.read_csv('data/Data_jobs.csv')
b =a.copy()


b['Senior'] = np.where(b['Job'].str.contains('Senior|senior'), 1, 0)

# We want to calculate dataset variables by groups
c=b.groupby(['Job', 'Country']).size().reset_index(name='Job_Country_Count')
print(b.info())
b =pd.merge(b, c, on=['Job', 'Country'], how='left').sort_values(by=['Country','Job', 'Skills'])
print(b.info())

# We ant to calculate dataset variable means
c=b.groupby(['Country', 'Job'])['Salary'].mean().reset_index(name='Country_Salary_Mean')
print('################################################################CCCCCCCCCCCCCCC ' + c.to_string())
b =pd.merge(b, c, on=['Job', 'Country'], how='left').sort_values(by=['Country','Job', 'Skills'])



from plotnine import *
(
    ggplot(b)
    + geom_boxplot(aes(x="Job", y="Salary", fill= "Senior"))
    + coord_flip()
    + facet_wrap('Country', ncol=5)
    + scale_fill_gradient(low='#008C7A', high='#415B5E')
).draw(True)
