
import pandas as pd
from datetime import datetime
from plotnine import *
from plotnine.mapping.evaluation import reorder
import numpy as np
import matplotlib.pyplot as plt

a = pd.read_csv('C:/Users/USUARIO/projects/python/basics/data/EDA1.csv')


####################################################################### Subsetting the data of interest Only Europe

c = pd.read_csv('C:/Users/USUARIO/projects/python/basics/data/europe_countries.csv')
d=pd.merge(a, c, on='Country', how='left')

# A preliminary plot was made for all european countries, there are many with high variability or scarse data
# Therefore only a subset of countries will be analyze

c=d[d['Analyze'] == 'Y'].copy()
country_list =c['Country'].tolist()

b= a[ a['Country'].isin(country_list) ].copy()


# We want to calculate dataset variables by groups
c=b.groupby(['Skills', 'Country']).size().reset_index(name='Skill_Country_Count')
print(b.info())
b =pd.merge(b, c, on=['Skills', 'Country'], how='left').sort_values(by=['Country','Job', 'Skills'])
print(b.info())

# We ant to calculate dataset variable means
c=b.groupby(['Country', 'Skills'])['Salary'].mean().reset_index(name='Country_Salary_Mean_Skill')
print('################################################################CCCCCCCCCCCCCCC ' + c.head().to_string())
b =pd.merge(b, c, on=['Skills', 'Country'], how='left').sort_values(by=['Country','Job', 'Skills'])
####################################################################### Exploratory Analysis

# We want to find top 50 skills
c=b.pivot_table(values='Salary', index='Skills', columns= 'Country', aggfunc='median')
topSkills=(b.groupby(['Skills'])['Salary'].mean().sort_values(ascending=False).head(50).index.tolist())

c= b[ b['Skills'].isin(topSkills) ].copy()

# We ant to calculate dataset variable means
#c=b.groupby(['Country', 'Skills'])['Salary'].mean().reset_index(name='Country_Salary_Mean_Skill')

############################################################################### Top 50 Skills ##########################################################
b = c.copy()
print(c.head(100).to_string())



#EDA22


c=b.pivot_table(values='Salary', columns='Country', index='Skills', aggfunc='median')
c.loc['Overall_Mean']= c.mean()
d= pd.concat([d,c], ignore_index=False)
print('########################## Median     ############################################ \n' + c.to_string())
c = c.drop('Overall_Mean')
plt.close('all')
c.plot(kind='bar')
#plt.show()


#EDA23
c=b.pivot_table(values='Salary', columns='Country', index='Skills', aggfunc='mean')
c.loc['Overall_Mean']= c.mean()
d= pd.concat([d,c], ignore_index=False)
print('########################## Mean     ############################################ \n' + c.to_string())
c = c.drop('Overall_Mean')
plt.close('all')
c.plot(kind='bar')
#plt.show()

plt.close('all')
# finding outliers per country

# #EDA24
p=(

    ggplot(b)
    + geom_jitter(aes(x="Job", y="Salary", size= "Country_Salary_Mean", fill='Country_Salary_Mean'), alpha=0.5)
    + coord_flip()
    + facet_wrap('Country', ncol=5)
    + theme_gray()

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

############################################################################### Top 100 Skills ##########################################################
a = pd.read_csv('C:/Users/USUARIO/projects/python/basics/data/EDA1.csv')
c = pd.read_csv('C:/Users/USUARIO/projects/python/basics/data/europe_countries.csv')
d=pd.merge(a, c, on='Country', how='left')
c=d[d['Analyze'] == 'Y'].copy()
country_list =c['Country'].tolist()

b= a[ a['Country'].isin(country_list) ].copy()

# We want to find top 50 skills
c=b.pivot_table(values='Salary', index='Skills', columns= 'Country', aggfunc='median')
topSkills=(b.groupby(['Skills'])['Salary'].mean().sort_values(ascending=False).head(100).index.tolist())

d= b[ b['Skills'].isin(topSkills) ].copy()
#df.dropna(subset=['column_name'], inplace=True)


print('#############################################################################################'+ c.head(100).to_string())
# We want to calculate dataset variables by groups
c=b.groupby(['Skills', 'Country']).size().reset_index(name='Skill_Country_Count')
print(b.info())
e =pd.merge(d, c, on=['Skills', 'Country'], how='left').sort_values(by=['Country','Job', 'Skills'])
print(b.info())
# We ant to calculate dataset variable means
c=b.groupby(['Country', 'Skills'])['Salary'].mean().reset_index(name='Country_Salary_Mean_Skill')
print('################################################################CCCCCCCCCCCCCCC ' + c.head().to_string())
f =pd.merge(e, c, on=['Skills', 'Country'], how='left').sort_values(by=['Country','Job', 'Skills'])
g=f[ f['Salary'] < 150000].copy()


#EDA25

p=(

    ggplot(g)
    + geom_jitter(aes(x="Skills", y="Salary", size= "Country_Salary_Mean_Skill", fill='Country_Salary_Mean_Skill'), alpha=0.5)
    + coord_flip()
    + facet_wrap('Country', nrow=1)
    + theme_gray()
    + scale_fill_gradient(low='black', high='orange')

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


#EDA26


Skills_List = g["Skills"].value_counts().index.tolist()[::-1]

p=(

    ggplot(g)
    + geom_point(aes(x="Skills", y="Salary", size= "Country_Salary_Mean_Skill", fill='Country_Salary_Mean_Skill'), alpha=0.5)
    + scale_x_discrete(limits= Skills_List)
    + coord_flip()
    + facet_wrap('Country', nrow=1)
    + theme_gray()
    + scale_fill_gradient(low='black', high='orange')

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


#EDA27
print(g.groupby(['Skills'])['Salary'].mean().sort_values(ascending=False).head(100).to_string())
topSkills=(g.groupby(['Skills'])['Salary'].mean().sort_values(ascending=True).head(100).index.tolist())


p=(

    ggplot(g)
    + geom_jitter(aes(x="Skills", y="Salary", size= "Country_Salary_Mean_Skill", fill='Country_Salary_Mean_Skill'), alpha=0.5)
    + scale_x_discrete(limits= topSkills)
    + coord_flip()
    + facet_wrap('Country', nrow=1)
    + theme_gray()
    + scale_fill_gradient(low='black', high='orange')

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

'''


'''



############################################################################### Top 30 Skills ##########################################################
a = pd.read_csv('C:/Users/USUARIO/projects/python/basics/data/EDA1.csv')
c = pd.read_csv('C:/Users/USUARIO/projects/python/basics/data/europe_countries.csv')
d=pd.merge(a, c, on='Country', how='left')
c=d[d['Analyze'] == 'Y'].copy()
country_list =c['Country'].tolist()

b= a[ a['Country'].isin(country_list) ].copy()

# We want to find top 50 skills
c=b.pivot_table(values='Salary', index='Skills', columns= 'Country', aggfunc='median')
topSkills=(b.groupby(['Skills'])['Salary'].mean().sort_values(ascending=False).head(30).index.tolist())

d= b[ b['Skills'].isin(topSkills) ].copy()

print('#############################################################################################'+ c.head(30).to_string())
# We want to calculate dataset variables by groups
c=b.groupby(['Skills', 'Country']).size().reset_index(name='Skill_Country_Count')
print(b.info())
e =pd.merge(d, c, on=['Skills', 'Country'], how='left').sort_values(by=['Country','Job', 'Skills'])
print(b.info())
# We ant to calculate dataset variable means
c=b.groupby(['Country', 'Skills'])['Salary'].mean().reset_index(name='Country_Salary_Mean_Skill')
print('################################################################CCCCCCCCCCCCCCC ' + c.head().to_string())
f =pd.merge(e, c, on=['Skills', 'Country'], how='left').sort_values(by=['Country','Job', 'Skills'])
g=f[ f['Salary'] < 150000].copy()
#EDA29

p=(

    ggplot(g)
    + geom_point(aes(x="Skills", y="Salary", size= "Country_Salary_Mean_Skill", fill='Country_Salary_Mean_Skill'), alpha=0.5)
    + coord_flip()
    + facet_wrap('Country', nrow=1)
    + theme_gray()
    + scale_fill_gradient(low='black', high='orange')

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


# EDA29
p=(

    ggplot(g)
    + geom_jitter(aes(x="Skills", y="Salary", size= "Country_Salary_Mean", fill='Country_Salary_Mean'), alpha=0.5)
    + scale_x_discrete(limits= Skills_List)
    + coord_flip()
    + facet_wrap('Job', nrow=1)
    + theme_gray()
    + scale_fill_gradient(low='black', high='orange')

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


#################################################### problems................................start here

############################################################################### Top 30 Skills ##########################################################
a = pd.read_csv('C:/Users/USUARIO/projects/python/basics/data/EDA1.csv')
c = pd.read_csv('C:/Users/USUARIO/projects/python/basics/data/europe_countries.csv')
d=pd.merge(a, c, on='Country', how='left')
c=d[d['Analyze'] == 'Y'].copy()
country_list =c['Country'].tolist()

b= a[ a['Country'].isin(country_list) ].copy()

# We want to find top 50 skills
c=b.pivot_table(values='Salary', index='Skills', columns= 'Country', aggfunc='median')
topSkills=(b.groupby(['Skills'])['Salary'].mean().sort_values(ascending=False).head(30).index.tolist())

d= b[ b['Skills'].isin(topSkills) ].copy()
d= b[ b['Skills'].isin(topSkills) ].copy()

print('#############################################################################################'+ c.head(30).to_string())
# We want to calculate dataset variables by groups
c=b.groupby(['Skills', 'Country']).size().reset_index(name='Skill_Country_Count')
print(b.info())
e =pd.merge(d, c, on=['Skills', 'Country'], how='left').sort_values(by=['Country','Job', 'Skills'])
print(b.info())
# We ant to calculate dataset variable means
c=b.groupby(['Country', 'Skills'])['Salary'].mean().reset_index(name='Country_Salary_Mean_Skill')
print('################################################################CCCCCCCCCCCCCCC ' + c.head().to_string())
f =pd.merge(e, c, on=['Skills', 'Country'], how='left').sort_values(by=['Country','Job', 'Skills'])
g=f[ f['Salary'] < 150000].copy()

# keep first duplicate row, there are not duplicates actually
#h = g.drop_duplicates().copy()



# EDA231
topSkills=(g.groupby(['Skills'])['Salary'].mean().sort_values(ascending=True).head(30).index.tolist())
#subset

h=g[ g['Skills'].isin(topSkills)].copy()

p=(

    ggplot(h)
    + geom_point(aes(x="Skills", y="Salary", size= "Country_Salary_Mean", fill='Country_Salary_Mean'), alpha=0.5)
    + coord_flip()
    + facet_wrap('Job', nrow=1)
    + theme_gray()
    + scale_fill_gradient(low='black', high='orange')

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

#EDA
p=(

    ggplot(h)
    + geom_point(aes(x="Skills", y="Salary", size= "Country_Salary_Mean", fill='Country_Salary_Mean'), alpha=0.5)
    + coord_flip()
    + facet_wrap('Job', nrow=1)
    + theme_gray()
    + scale_fill_gradient(low='black', high='orange')

)
h.to_csv('C:/Users/USUARIO/projects/python/basics/data/deleteH.csv', sep = ',', index=False)
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
'''

'''