




from datetime import datetime
from plotnine import *
from plotnine.mapping.evaluation import reorder
import numpy as np
import matplotlib.pyplot as plt


import pandas as pd


f = pd.read_csv('C:/Users/USUARIO/projects/python/portfolio/work/data/Data_Jobs.csv')
g = f[ ['Job', 'Salary', 'Country'] ]
g.drop_duplicates(inplace = True)
g.columns=[ 'Job','Salary', 'Country']
print(g.head().to_string() + '\n this was g\n')

a = pd.read_csv('C:/Users/USUARIO/projects/python/portfolio/work/data/EDA1_Bargraphs_3.2.csv')

b = a[ a['paramtyp'].isnull() == False ] # overall statistic by job

print(b.head().to_string() +'\n this was b')

c = a[  a['paramtyp'].isnull()  ] # statistic by job and by country 

c = c[  c['paramcd'] == "MEAN"    ]
c= c[['job', 'aval', 'param']]

c.drop_duplicates(inplace = True)
c.columns=[ 'Job','Salary', 'Country']

print(c.head().to_string() +'this was c')


d =  a[ a['paramtyp']== 'MEAN COUNTRY AVG']
print(d.head().to_string() +'this was d')
# #EDA24#
# e =pd.merge(c, d, on=['Skills', 'Country'], how='left').sort_values(by=['Country','Job', 'Skills'])
g= pd.merge(g,c, on=['Country', 'Job'], how='left')
print(g)



##########

c = a[  a['paramtyp'].isnull()  ] # statistic by job and by country 

c = c[  c['paramcd'] == "N"    ]
c= c[['job', 'aval', 'param']]

c.drop_duplicates(inplace = True)
c.columns=[ 'Job','Salary', 'Country']

g= pd.merge(g,c, on=['Country', 'Job'], how='left')
print(g.to_string())
g.columns=['Job', 'Salary', 'Country', 'Overall_Salary', 'Overall_N']
# 2.1

p=(

    ggplot(g)
    + geom_point(aes(x="Job", y="Salary", fill="Overall_Salary", size="Overall_N"))
    + coord_flip()
    + facet_wrap('Country', ncol=5)
    + theme_gray()
    + labs(
         fill = "Country VS. Overall Mean",
         size = "Sample Size"
        )

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



# 2.0.2

p=(

    ggplot(g)
    + geom_jitter(aes(x="Job", y="Salary", fill="Overall_Salary", size="Overall_N"), alpha=0.5)
    + coord_flip()
    + facet_wrap('Country', ncol=5)
    + theme_gray()
    + labs(
         fill = "Country VS. Overall Mean",
         size = "Sample Size"
        )

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

# 2.0.3
# 
g=g[ g['Country'].isin(['Italy', 'Germany'] ) ].copy()

p=(

    ggplot(g)
    + geom_jitter(aes(x="Job", y="Salary", fill="Overall_Salary", size="Overall_N"), alpha=0.5)
    + coord_flip()
    + facet_wrap('Country', ncol=5)
    + theme_gray()
    + labs(
         fill = "Country VS. Overall Mean",
         size = "Sample Size"
        )

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