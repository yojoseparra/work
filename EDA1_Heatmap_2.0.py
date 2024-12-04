



from datetime import datetime
from plotnine import *
from plotnine.mapping.evaluation import reorder
import numpy as np
import matplotlib.pyplot as plt


import pandas as pd


a = pd.read_csv('data/Data_Jobs.csv')

a.drop([ 'level_0'], axis=1, inplace=True)

# We want to calculate dataset variables by groups
c=a.groupby(['Country', 'Job', 'Skills']).size().reset_index(name='n')

e =pd.merge(a, c, on=['Country', 'Job', 'Skills'], how='left').sort_values(by=['Country','Job', 'Skills'])



def gettots(x):
 out = {}
 out['mean'] = x.mean()
 return pd.Series(out)


f=a.groupby(['Country', 'Job', 'Skills'])['Salary'].apply(gettots)
f=f.unstack()
f.reset_index(inplace=True)

g =pd.merge(e, f, on=['Country', 'Job', 'Skills'], how='left').sort_values(by=['Country','Job', 'Skills'])


h = g[ (g['n'] >0 )  ]
noskills =["windows", "vba", "unreal", "ssis", "sql server"
          , "sap", "ruby", "react","powerpoint", "perl"
          , "numpy", "nltk", "matplotlib", "matlab"
          , "kotlin", "keras", "jira", "flow", "elasticsearch"
          , "cassandra", "zoom", ]

h = h[~h['Skills'].isin(noskills)]
#yesjobs =["Business Analyst",  "Senior Data Analyst", "Senior Data Scientist"]
#h = h[h['Job'].isin(yesjobs)]
p=(

    ggplot(h,aes(x="Skills", y="Job", fill= "Salary") )
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
)


h = g[ (g['n'] >4 ) & (g['n'] <9 )  ]
noskills =["windows", "vba", "unreal", "ssis", "sql server"
          , "sap", "ruby", "react","powerpoint", "perl"
          , "numpy", "nltk", "matplotlib", "matlab"
          , "kotlin", "keras", "jira", "flow", "elasticsearch"
          , "cassandra", "zoom", ]

h = h[~h['Skills'].isin(noskills)]
yesjobs =["Business Analyst","Data Analyst","Data Engineer","Data Scientist","Machine Learning Engineer","Senior Data Engineer","Senior Data Scientist","Software Engineer"]
#yesjobs =["Business Analyst","Data Analyst","Data Scientist","Senior Data Engineer","Senior Data Scientist","Software Engineer"]
h = h[h['Job'].isin(yesjobs)]
#yesjobs =["Business Analyst",  "Senior Data Analyst", "Senior Data Scientist"]
#h = h[h['Job'].isin(yesjobs)]
# 2.0.2
p=(

    ggplot(h,aes(x="Skills", y="Job", fill= "n") )
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


