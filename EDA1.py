
import pandas as pd
import datetime
import plotnine
import numpy as np
import matplotlib.pyplot as plt


a = pd.read_csv('data/Data_jobs.csv')
a.head()
####################################################################### Subsetting the data of interest Only Europe



# We try to reduce variability based on seniority in the Job creating categorical variable

b=a.copy()
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
####################################################################### Exploratory Analysis

# Display first few rows
print(b.head().to_string())

# Check the structure
print(b.info())

# Summary statistics
print(b.describe())


print(pd.DataFrame(b).describe().to_string())

print(b.groupby(['Country', 'Job'])['Salary'].describe())


# finding outliers per country
(
    ggplot(b)
    + geom_boxplot(aes(x="Job", y="Salary", fill= "Senior"))
    + coord_flip()
    + facet_wrap('Country', ncol=5)
    + scale_fill_gradient(low='#008C7A', high='#415B5E')
).draw(True)
# It looks like being senior do not really matters in terms of salary


c=b.pivot_table(values='Salary', columns='Country', index='Job', aggfunc='min')
c.loc['Overall_Mean']= c.mean()
d=c.copy()
print('########################## Min     ############################################ \n' + c.to_string())
c = c.drop('Overall_Mean')
plt.close('all')
c.plot(kind='bar')


c=b.pivot_table(values='Salary', columns='Country', index='Job', aggfunc='median')
c.loc['Overall_Mean']= c.mean()
d= pd.concat([d,c], ignore_index=False)
print('########################## Median     ############################################ \n' + c.to_string())
c = c.drop('Overall_Mean')
plt.close('all')
c.plot(kind='bar')



c=b.pivot_table(values='Salary', columns='Country', index='Job', aggfunc='mean')
c.loc['Overall_Mean']= c.mean()
d= pd.concat([d,c], ignore_index=False)
print('########################## Mean     ############################################ \n' + c.to_string())
c = c.drop('Overall_Mean')
plt.close('all')
c.plot(kind='bar')



c=b.pivot_table(values='Salary', columns='Country', index='Job', aggfunc='max')
c.loc['Overall_Mean']= c.mean()
d= pd.concat([d,c], ignore_index=False)
print('########################## Max     ############################################ \n' + c.to_string())
c = c.drop('Overall_Mean')
plt.close('all')
c.plot(kind='bar')

#EDA 13
#d.to_csv('C:/Users/USUARIO/projects/python/basics/data/EDA.csv', sep = ',', index=True)
e=d.loc[['Overall_Mean']]
print('########################## Min, Median, Mean, Max     ############################################ \n' + e.to_string())
e.plot(kind='bar')
#plt.show()

'''
########################## Min, Median, Mean, Max     ############################################ 
Country             Belgium        Finland         France       Germany       Greece        Ireland          Italy    Netherlands         Poland       Portugal        Romania          Spain         Sweden
Job                                                                                                                                                                                                         
Overall_Mean   63050.812500   86431.375000   60855.300000   58763.25000   57447.7500   81527.062500   68812.500000   77009.888889   58679.700000   71677.944444   65583.333333   59081.400000   90124.055556
Overall_Mean   97752.156250  117270.250000  112564.450000  118305.00000   82936.5000  130967.500000   84314.875000  104106.444444  108965.400000  120197.666667   85039.777778  106990.500000  129994.444444
Overall_Mean   91543.826287  113404.121522  113004.211189  114534.61633   90270.7848  126097.072476   88768.114904  115847.038635  107070.149701  116824.688950  100772.757783  111047.885677  124916.059492
Overall_Mean  113903.625000  131875.437500  165656.250000  181918.30000  146288.0000  160054.875000  111583.500000  162537.000000  165782.800000  148774.611111  138241.111111  172440.300000  157923.888889
'''

# We want to check where the data is mostly concentrated
c=b.pivot_table(values='Year', columns='Job', index='Country', aggfunc='size')
c.loc['Overall_Mean']= c.mean()
print('########################## Size     ############################################ \n' + c.to_string())
c = c.drop('Overall_Mean')
plt.close('all')
#c.plot(kind='bar')
#s.iloc[:, :5].plot(kind='line')
#plt.title('')
#plt.xlabel('')
#plt.ylabel('')
#plt.ylim(0,200)
#plt.legend()

'''
########################## Size     ############################################ 
Job          Business Analyst  Cloud Engineer  Data Analyst  Data Engineer  Data Scientist  Machine Learning Engineer  Senior Data Analyst  Senior Data Engineer  Senior Data Scientist  Software Engineer
Country                                                                                                                                                                                                   
Belgium                  24.0             NaN          85.0           67.0            68.0                       74.0                  NaN                   7.0                    3.0                6.0
Finland                   NaN             NaN          14.0           24.0            10.0                       20.0                 13.0                  19.0                   11.0               13.0
France                   17.0             3.0         188.0          438.0           239.0                       78.0                 52.0                 109.0                   44.0               51.0
Germany                  35.0            37.0         152.0          173.0           134.0                      143.0                 44.0                 147.0                  125.0               31.0
Greece                   14.0             NaN          56.0          195.0            60.0                      108.0                  NaN                   9.0                   30.0               49.0
Ireland                   NaN             NaN          85.0           70.0            29.0                       27.0                 13.0                  60.0                   29.0                2.0
Italy                     5.0             NaN          41.0          102.0            42.0                       14.0                 12.0                   NaN                    5.0               10.0
Netherlands              13.0             NaN          84.0          178.0            68.0                       58.0                  1.0                  46.0                    9.0               16.0
Poland                   26.0            30.0         175.0          315.0           150.0                      114.0                 29.0                  90.0                   76.0               81.0
Portugal                  6.0             NaN         106.0          206.0           110.0                       75.0                 16.0                  27.0                   38.0               30.0
Romania                   1.0             1.0          30.0           46.0            37.0                       21.0                 15.0                  27.0                    NaN               25.0
Spain                    18.0            13.0         113.0          226.0            83.0                      109.0                 34.0                  79.0                   28.0               42.0
Sweden                   19.0             NaN          34.0           67.0            33.0                       16.0                 10.0                  30.0                   12.0                1.0
Total                   178.0            84.0        1163.0         2107.0          1063.0                      857.0                239.0                 650.0                  410.0              357.0
'''
#EDA 13
print(b.head(3).to_string())
(
    ggplot(b)
     + aes(y="Job", x="Salary",size="Job_Country_Count", fill="Job_Count")
    + geom_jitter(alpha=0.2)
    + facet_wrap('Country', ncol=5)
    + scale_fill_gradient(low='#008C7A', high='#415B5E')
)
print(b.head(3).to_string())

c=b.groupby(['Country', 'Job'])['Salary'].mean().reset_index(name='Salary')
d=b.groupby(['Country', 'Job']).size().reset_index(name='Job_Country_Count')
e =pd.merge(c,d, on=[ 'Country', 'Job'], how='left').sort_values(by=['Country','Job'])

print('ccccccccccccccccccccccccccccccccc     \n ' + c.head(10).to_string() )
print('ccccccccccccccccccccccccccccccccccc       \n ' + d.head(10).to_string() )
print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee      \n ' + e.head(10).to_string() )

(
    ggplot(b)
     + aes(y="Job", x="Salary", size="Job_Country_Count" , fill="Job_Country_Count")
    + geom_jitter(alpha=0.2)
    + geom_point(data=e, fill ='#A70267')
    + facet_wrap("Country", ncol=5)
    + scale_fill_gradient(low='#008C7A', high='#415B5E')
).draw(True)
'''
Conclusions hereunder
'''

''' 60-90-150
Not all data was taken for countries in europe. the reason is that thee were counties 
with small counts of dat like Latvia, Slovenia....

Conclusions so far: Most of Job offerings are in Franace Poland Germany Portugal
Spain Neederlands and Belgium. Countries like Rumania  Sweden Hungary  Ireland Finland 
Denmark and Finland have less offerings. 

The Overall mean of salaries accross europe no matter the skills are about 60K. The overall
mean could be representative of most of countries for all types of jobs and skills. FI, IR,SW,PO
pays better and the MIN there can be roughly 80K.

The Median across countries and jobs are around 90K accross countries. Sweden has the highest
Median pay around 110K. The overall mean lies around the same as the mean.

The MAX is difficult to read. but I suppose it is around 150K. THere are countries that lag
in terms of salary MIN,MEDIAN and MAX.

In terms of most requested Job, it is Data Engineer, Data Science and Data Engineer.
Less reauested jobs are Cloud Egineer and Senior Data Analyst.


'''


print(b.head().to_string())
#b.to_csv('C:/Users/USUARIO/projects/python/basics/data/EDA1.csv', sep = ',', index=False)