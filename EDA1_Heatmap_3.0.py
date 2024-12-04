
import pandas as pd
from datetime import datetime
from plotnine import *
from plotnine.mapping.evaluation import reorder
import numpy as np
import matplotlib.pyplot as plt



w = pd.read_csv('data/correlations.csv')

x=pd.melt(w, id_vars='Skills',value_vars= w.columns.difference(["Skills"])  ,ignore_index=True )
y=x.dropna()
print(y)

w=y[y['variable'] != 'Unnamed: 0'].copy()


a = pd.read_csv('C:/Users/USUARIO/projects/python/portfolio/work/data/Data_Jobs.csv')

a.drop([ 'level_0'], axis=1, inplace=True)
# We want to calculate dataset variables by groups#
c=a.groupby(['Country', 'Job', 'Skills']).size().reset_index(name='n')
e =pd.merge(a, c, on=['Country', 'Job', 'Skills'], how='left').sort_values(by=['Country','Job', 'Skills'])

def gettots(x):
 out = {}
 out['mean'] = x.mean()
 return pd.Series(out)


f=a.groupby(['Country', 'Job', 'Skills'])['Salary'].apply(gettots)
f=f.unstack()
f.reset_index(inplace=True)

g =pd.merge(e, f, on=['Country', 'Job', 'Skills'], how='left').sort_values(by=[ 'n','Skills', 'Country', 'Job'], ascending=False)


h=g[['Skills', 'Job', 'Country', 'n', 'mean']].copy()


h.reset_index(inplace=True)
h=h.drop('index', axis=1)
i=h.drop_duplicates()

#i.to_csv('data/EDA1_Heatmap_3.0.1.csv', sep = ',', index=False)


h= i[ i['n'] > 4]
noskills =["windows", "vba", "unreal", "ssis", "sql server"
          , "sap", "ruby", "react","powerpoint", "perl"
          , "numpy", "nltk", "matplotlib", "matlab"
          , "kotlin", "keras", "jira", "flow", "elasticsearch"
          , "cassandra"]

h = h[~h['Skills'].isin(noskills)]


p=(
    ggplot(h,aes(x="Job", y="Skills", fill= "n") )
    + geom_tile()
    + scale_fill_gradient( low = "#fdf6e3", high = "steelblue")
    + theme(axis_text_x=element_text(rotation=90, hjust=1))

)

(p + theme(
    panel_grid=element_line(color='gray'),
    panel_grid_major=element_line(size=0.5, alpha=1),
    panel_grid_major_x=element_line(linetype="dashed"),
    panel_grid_major_y=element_line(linetype="dashdot"),
    panel_grid_minor=element_line(alpha=0.25),
    panel_grid_minor_x=element_line(color='gray'),
    panel_grid_minor_y=element_line(color='gray'),
    panel_ontop=False,  # puts the points behind the grid
    )
).draw(True)
'''

'''




#g.to_csv('data/EDA1_Heatmap_3.0.2.csv', sep = ',', index=False)