



from datetime import datetime
from plotnine import *
from plotnine.mapping.evaluation import reorder
import numpy as np
import matplotlib.pyplot as plt


import pandas as pd


a = pd.read_csv('data/Data_Jobs.csv')

a.drop([ 'level_0'], axis=1, inplace=True)
b = pd.read_csv('data/Data_Jobs_Subset.csv')
c = pd.merge(b, a, on=['index','Country', 'Job', 'Skills'], how='left').sort_values(by=['Country','Job', 'Skills'])


d= c[["index","Country","Job", "Skills", "Salary"]]
d = d.drop_duplicates().sort_values(by=["Country","Job", "Skills"], ascending=False)
a=d.copy()

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



#h = g[ (g['CO'] == 'PO' )  ]

h = g[ (g['n'] > 0 )  ]

#E3.0.1

p=(

    ggplot(h)
    + geom_jitter(aes(x="Skills", y="Salary", size= "n", color='Job'), alpha=0.5)
    + coord_flip()
    + facet_wrap('Country', nrow=1)
    + theme_gray()
    + scale_colour_manual(values = ("blue", "red", "green","black", "#661100", "yellow", "orange", "brown", "grey","purple","olive" ))


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



#3.0.2
p=(

    ggplot(h)
    + geom_jitter(aes(x="Skills", y="Salary", size= "n", color='Job'), alpha=0.5)
    + coord_flip()
    + facet_wrap('Country', nrow=1)
    + theme_gray()
    + scale_colour_manual(values = ("blue", "red", "green","black", "#661100", "yellow", "orange", "brown", "grey","purple","olive" ))


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
