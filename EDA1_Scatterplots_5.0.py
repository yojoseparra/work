



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

a = d.copy()
# We want to calculate dataset variables by groups#
c=a.groupby(['Country', 'Skills']).size().reset_index(name='n')
e =pd.merge(a, c, on=['Country', 'Skills'], how='left').sort_values(by=['Country', 'Skills'])

def gettots(x):
 out = {}
 out['mean'] = x.mean()
 return pd.Series(out)


f=a.groupby(['Country', 'Skills'])['Salary'].apply(gettots)
f=f.unstack()
f.reset_index(inplace=True)

g =pd.merge(e, f, on=['Country', 'Skills'], how='left').sort_values(by=[ 'mean','Skills', 'Country'], ascending=False)


h=g[['Skills', 'Country', 'n', 'mean', 'Job']].copy()


h.reset_index(inplace=True)
h=h.drop('index', axis=1)
i=h.drop_duplicates()
i =h[h['n'] > 0 ]


# We assign a letter to each skill to plot easily

allskills= i['Skills'].drop_duplicates().tolist()
k = pd.DataFrame(allskills, columns = [ 'Skills'])
k.reset_index(inplace=True)
k["index"] = k["index"] +1
def col_num_to_char(col):
    char = ''
    div = col
    while div:
        div, mod = divmod(div - 1, 26)
        char = chr(mod + 65) + char
    return char

k["alpha"] =  k["index"].apply(col_num_to_char)
#k.to_csv('data/EDA1_Scaterplots_5.0_letters.csv', sep = ',', index=False)
m = pd.merge(i,k,on=["Skills"], how="left")


p=(

    ggplot(m)
    + geom_text(aes(x="Skills", y="mean", color='Job', label='alpha') , size=16)
    + coord_flip()
    + facet_wrap('Country', nrow=3)
    + theme_gray()
    + theme(axis_text_x=element_text(rotation=90, hjust=1))
    + scale_colour_manual(values = ( "red","#661100", "green","black", "blue", "yellow", "orange", "brown", "grey","purple","olive" ))


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
#m.to_csv('C:/Users/USUARIO/projects/python/portfolio/work/data/EDA2_Scaterplots_5.0.csv', sep = ',', index=False)