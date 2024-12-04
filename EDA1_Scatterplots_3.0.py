


from datetime import datetime
from plotnine import *
from plotnine.mapping.evaluation import reorder
import numpy as np
import matplotlib.pyplot as plt


import pandas as pd


a = pd.read_csv('C:/Users/USUARIO/projects/python/portfolio/work/data/Data_Jobs.csv')

a.drop([ 'level_0'], axis=1, inplace=True)
"""
# We want to find top 50 skills
c=a.pivot_table(values='Salary', index='Country', columns= 'Job', aggfunc='mean')
topSkills=(b.groupby(['Skills'])['Salary'].mean().sort_values(ascending=False).head(100).index.tolist())

d= b[ b['Skills'].isin(topSkills) ].copy()
#df.dropna(subset=['column_name'], inplace=True)

"""

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

h = g[ (g['n'] > 5 )  ]
noskills =["windows", "vba", "unreal", "ssis", "sql server"
          , "sap", "ruby", "react","powerpoint", "perl"
          , "numpy", "nltk", "matplotlib", "matlab"
          , "kotlin", "keras", "jira", "flow", "elasticsearch"
          , "cassandra"]

h = h[~h['Skills'].isin(noskills)]
#E3.2

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

#E3.3

noskills =["windows", "vba", "unreal", "ssis", "sql server", "sap", "ruby", "react","powerpoint", "perl", "numpy", "nltk", "matplotlib", "matlab" , "kotlin", "keras", "jira", "flow", "elasticsearch", "cassandra"]
nojobs =["Business Analyst", "Machine Learning Engineer", "Sofware Engineer", "Data Analyst"]
h = h[~h['Job'].isin(nojobs)]
h = h[~h['Skills'].isin(noskills)]

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

#E3.4

noskills =["windows", "vba", "unreal", "ssis", "sql server", "sap", "ruby", "react","powerpoint", "perl", "numpy", "nltk", "matplotlib", "matlab" , "kotlin", "keras", "jira", "flow", "elasticsearch", "cassandra"]
nojobs =["Business Analyst", "Machine Learning Engineer", "Sofware Engineer", "Data Analyst", "Software Engineer", "Senior Data Analyst"]
h = h[~h['Job'].isin(nojobs)]
h = h[~h['Skills'].isin(noskills)]

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



#E3.5

noskills =["windows", "vba", "unreal", "ssis", "sql server", "sap", "ruby", "react","powerpoint", "perl", "numpy", "nltk", "matplotlib", "matlab" , "kotlin", "keras", "jira", "flow", "elasticsearch", "cassandra"]
nojobs =["Business Analyst", "Machine Learning Engineer", "Sofware Engineer", "Data Analyst", "Software Engineer", "Senior Data Analyst"]
h = h[~h['Job'].isin(nojobs)]
h = h[~h['Skills'].isin(noskills)]

p=(

    ggplot(h)
    + geom_jitter(aes(x="Skills", y="Salary", size= "mean", color='Job'), alpha=0.5)
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
#E3.7
h = g.copy()
noskills =["windows", "vba", "unreal", "ssis", "sql server", "sap", "ruby", "react","powerpoint", "perl", "numpy", "nltk", "matplotlib", "matlab" , "kotlin", "keras", "jira", "flow", "elasticsearch", "cassandra"]
yesjobs =["Business Analyst", "Machine Learning Engineer", "Sofware Engineer", "Data Analyst", "Software Engineer", "Senior Data Analyst"]
h = h[h['Job'].isin(yesjobs)]
h = h[~h['Skills'].isin(noskills)]
h = h[h['n'] > 3]
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

#E3.7
h = g.copy()
noskills =["windows", "vba", "unreal", "ssis", "sql server", "sap", "ruby", "react","powerpoint", "perl", "numpy", "nltk", "matplotlib", "matlab" , "kotlin", "keras", "jira", "flow", "elasticsearch", "cassandra"]
yesjobs =["Business Analyst", "Machine Learning Engineer", "Sofware Engineer", "Data Analyst", "Software Engineer", "Senior Data Analyst"]
h = h[h['Job'].isin(yesjobs)]
h = h[~h['Skills'].isin(noskills)]
h = h[h['n'] > 3]
p=(

    ggplot(h)
    + geom_jitter(aes(x="Skills", y="Salary", size= "mean", color='Job'), alpha=0.5)
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

#E3.8
h = g.copy()
noskills =["windows", "vba", "unreal", "ssis", "sql server", "sap", "ruby", "react","powerpoint", "perl", "numpy", "nltk", "matplotlib", "matlab" , "kotlin", "keras", "jira", "flow", "elasticsearch", "cassandra"]
yesjobs =["Data Analyst", "Machine Learning Engineer", "Data Engineer"]
h = h[h['Job'].isin(yesjobs)]
h = h[~h['Skills'].isin(noskills)]

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

#E3.9
h = g.copy()
noskills =["windows", "vba", "unreal", "ssis", "sql server", "sap", "ruby", "react","powerpoint", "perl", "numpy", "nltk", "matplotlib", "matlab" , "kotlin", "keras", "jira", "flow", "elasticsearch", "cassandra"]
yesjobs =["Data Analyst", "Data Engineer"]
h = h[h['Job'].isin(yesjobs)]
h = h[~h['Skills'].isin(noskills)]
h = h[h['n'] > 2]
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

#E3.11
h = g.copy()
noskills =["windows", "vba", "unreal", "ssis", "sql server", "sap", "ruby", "react","powerpoint", "perl", "numpy", "nltk", "matplotlib", "matlab" , "kotlin", "keras", "jira", "flow", "elasticsearch", "cassandra"]
yesjobs =["Data Analyst", "Data Scientist"]
h = h[h['Job'].isin(yesjobs)]
h = h[~h['Skills'].isin(noskills)]
h = h[h['n'] > 2]
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


#E3.12
h = g.copy()
noskills =["windows", "vba", "unreal", "ssis", "sql server", "sap", "ruby", "react","powerpoint", "perl", "numpy", "nltk", "matplotlib", "matlab" , "kotlin", "keras", "jira", "flow", "elasticsearch", "cassandra"]
yesjobs =["Data Analyst", "Data Scientist"]
h = h[h['Job'].isin(yesjobs)]
h = h[~h['Skills'].isin(noskills)]
h = h[h['n'] > 10]
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