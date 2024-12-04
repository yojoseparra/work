import pandas as pd
from datetime import datetime
from plotnine import *
from plotnine.mapping.evaluation import reorder
import numpy as np
import matplotlib.pyplot as plt

a = pd.read_csv('data/EDA1_Heatmap_3.0.1.csv')
a.reset_index(inplace=True)
h=a.drop('index', axis=1)

i=h.drop_duplicates()

j = i[ (i['n'] > 0 )  ]

#j.columns.tolist()
#skills=np.unique(, axis=0)
h=j.copy()

noskills =["windows", "vba", "unreal", "ssis", "sql server"
          , "sap", "ruby", "react","powerpoint", "perl"
          , "numpy", "nltk", "matplotlib", "matlab"
          , "kotlin", "keras", "jira", "flow", "elasticsearch"
          , "cassandra"]

#h = h[~h['Skills'].isin(noskills)]
# 4.0

p=(

    ggplot(h)
    + geom_jitter(aes(x="n", y="mean", size= "mean", color='Job'), alpha=0.5)
    + coord_flip()
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
# 4.1
p=(

    ggplot(h)
    + geom_jitter(aes(x="n", y="mean", size= "mean", color='Job'), alpha=0.5)
    + coord_flip()
    + facet_wrap('Country', nrow=3)
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

# 4.0.2
h = h[ (h['n'] < 10 )  ]
p=(

    ggplot(h)
    + geom_jitter(aes(x="n", y="mean", size= "mean", color='Job'), alpha=0.5)
    + coord_flip()
    + facet_wrap('Country', nrow=3)
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
