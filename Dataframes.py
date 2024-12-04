# this is comming mostly from lukebarousse course online
# lukebarousse
# https://github.com/lukebarousse/Python_Data_Analytics_Course/tree/main
# Python_Data_Analytics_Course

import pandas as pd
import xlrd
import openpyxl

import os
from datetime import datetime

from pandas.io.clipboard import paste
import sqldf
cwd=os.getcwd()
print(cwd)
wd = 'C:/Users/USUARIO/projects/python/basics/data/OPQ32 PROFIEL 04NOV2024 SHL.xlsx'
print(wd)




d = pd.read_excel( wd)
d.sample(10)
id(d)


print(type(d))
print(d.head())
d.info()
############################# DF ID #############################
df = pd.DataFrame(d)
df1 = df.copy()
print(' ID of df is: ', id(d), 'ID of DF1 is: ', id(df1), 'Are they Equal?: ', id(d) == id(df1) )
print(df.dtypes)

df['dt'] = pd.to_datetime(df['Datum'])
print(df.dtypes)

# The first dt has relation with the variable dt within the dataset
df['month'] = df.dt.dt.month
print(df.dtypes)
print(df.head())


############################# ILOC #############################
e = df.copy()
print(e)
#This is to print all the data and to avoid three points ...
'''
Before
    Jose  Sien  Anja  Alejandro  ...  Parameter         Gebied         dt month
0      6     3     6          6  ...   Relaties        Invloed 2024-11-04    11
1      6     3     5          5  ...   Relaties        Invloed 2024-11-04    11
2      9     6    10          9  ...   Relaties        Invloed 2024-11-04    11
3      9     9     7          8  ...   Relaties  Sociabiliteit 2024-11-04    11
4      5     4     8          8  ...   Relaties  Sociabiliteit 2024-11-04    11
5      4     8     5          8  ...   Relaties  Sociabiliteit 2024-11-04    11
'''
print(e.to_string())

print(e.iloc[0:10, 0:10].to_string())
print(e.iloc[0:10, 0:15].to_string())
'''
   Jose  Sien  Anja  Alejandro                    Item  Tekst Bedrijf         Datum Parameter         Gebied         dt  month
0     6     3     6          6             Overtuigend  OPQ32     SHL   2024-11-04   Relaties        Invloed 2024-11-04     11
1     6     3     5          5           Leidinggevend  OPQ33     SHL   2024-11-04   Relaties        Invloed 2024-11-04     11
2     9     6    10          9                  Direct  OPQ34     SHL   2024-11-04   Relaties        Invloed 2024-11-04     11
3     9     9     7          8  Onafhankelijk Hndelend  OPQ35     SHL   2024-11-04   Relaties  Sociabiliteit 2024-11-04     11
4     5     4     8          8               Extravert  OPQ36     SHL   2024-11-04   Relaties  Sociabiliteit 2024-11-04     11
5     4     8     5          8      Gesteld op contact  OPQ37     SHL   2024-11-04   Relaties  Sociabiliteit 2024-11-04     11
6     7     6     9          7           Zelfverzekerd  OPQ38     SHL   2024-11-04   Relaties       Empathie 2024-11-04     11
7     4     6     8          8              bescheiden  OPQ39     SHL   2024-11-04   Relaties       Empathie 2024-11-04     11
8     6     7     6          9            Democratisch  OPQ40     SHL   2024-11-04   Relaties       Empathie 2024-11-04     11
9     4     4     5          7                Zorgzaan  OPQ41     SHL   2024-11-04   Relaties       Empathie 2024-11-04     11

'''
# We want to eliminate NA data from the column Jose
print(e.loc[:, 'Jose':'Gebied'].dropna(subset='Jose').to_string())

''' Not all rows I passed here just for sake of ilustration 
    Jose  Sien  Anja  Alejandro                     Item  Tekst Bedrijf         Datum  Parameter         Gebied
0      6     3     6          6              Overtuigend  OPQ32     SHL   2024-11-04    Relaties        Invloed
1      6     3     5          5            Leidinggevend  OPQ33     SHL   2024-11-04    Relaties        Invloed
2      9     6    10          9                   Direct  OPQ34     SHL   2024-11-04    Relaties        Invloed
.
.
.

'''
import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt

'''
# Loading Data
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

print(df['job_country'].unique())
d = df[ df['job_country'] =='Belgium'].copy()
# Data Cleanup
d['job_posted_date'] = pd.to_datetime(d['job_posted_date'])

d.to_csv('C:/Users/USUARIO/projects/python/basics/data/data_jobs_be.csv', sep = '\t')
'''


dt = pd.read_csv('C:/Users/USUARIO/projects/python/basics/data/data_jobs_be.csv', sep = '\t')
d= dt.copy()
print(d.info())
d['dt'] = pd.to_datetime(d['job_posted_date'])
print(d.info())
d['month'] = d['dt'].dt.strftime('%B')
print(d.head().to_string())

e= d.pivot_table(index='month', columns= 'job_title_short', aggfunc= 'size')

#print(e.to_string())

'''

job_title_short  Business Analyst  Cloud Engineer  Data Analyst  Data Engineer  Data Scientist  Machine Learning Engineer  Senior Data Analyst  Senior Data Engineer  Senior Data Scientist  Software Engineer
month                                                                                                                                                                                                         
April                         103              20           360            318             163                         11                   26                    32                     22                 77
August                         93              20           354            245             157                         26                    6                    32                     21                 53
December                       93              15           211            185             134                         11                   17                    17                     15                 63
February                       67              15           263            247             123                         16                   12                    20                     16                 28
January                       128              24           451            481             288                         21                   32                    48                     47                 72
July                           82              16           310            252             167                         20                   19                    36                     27                 60
June                           52               6           322            299             178                         12                   12                    21                     24                 20
March                          90              14           333            359             186                         24                   13                    30                     27                 37
May                            51               3           297            244             131                         21                   19                    15                     23                 29
November                      110              33           292            193             143                         17                   18                    24                     25                 63
October                       117              31           342            235             163                         21                   21                    27                      7                101
September                     123              22           272            215             163                         14                    9                    23                     15                 59

'''

############################# DATE FORMATS #############################
e.reset_index(inplace=True)
e['monthn'] =pd.to_datetime(e['month'], format='%B')


'''
job_title_short      month  Business Analyst  Cloud Engineer  Data Analyst  Data Engineer  Data Scientist  Machine Learning Engineer  Senior Data Analyst  Senior Data Engineer  Senior Data Scientist  Software Engineer     monthn
0                    April               103              20           360            318             163                         11                   26                    32                     22                 77 1900-04-01
1                   August                93              20           354            245             157                         26                    6                    32                     21                 53 1900-08-01
2                 December                93              15           211            185             134                         11                   17                    17                     15                 63 1900-12-01
3                 February                67              15           263            247             123                         16                   12                    20                     16                 28 1900-02-01
4                  January               128              24           451            481             288                         21                   32                    48                     47                 72 1900-01-01
5                     July                82              16           310            252             167                         20                   19                    36                     27                 60 1900-07-01
6                     June                52               6           322            299             178                         12                   12                    21                     24                 20 1900-06-01
7                    March                90              14           333            359             186                         24                   13                    30                     27                 37 1900-03-01
8                      May                51               3           297            244             131                         21                   19                    15                     23                 29 1900-05-01
9                 November               110              33           292            193             143                         17                   18                    24                     25                 63 1900-11-01
10                 October               117              31           342            235             163                         21                   21                    27                      7                101 1900-10-01
11               September               123              22           272            215             163                         14                    9                    23                     15                 59 1900-09-01

Process finished with exit code 0'''

e['monthn'] =pd.to_datetime(e['month'], format='%B').dt.month
#print(e.to_string())
e.sort_values('monthn', inplace=True)

e.set_index('month', inplace=True)
e.drop(columns=['monthn'], inplace=True)
'''
job_title_short      month  Business Analyst  Cloud Engineer  Data Analyst  Data Engineer  Data Scientist  Machine Learning Engineer  Senior Data Analyst  Senior Data Engineer  Senior Data Scientist  Software Engineer  monthn
4                  January               128              24           451            481             288                         21                   32                    48                     47                 72       1
3                 February                67              15           263            247             123                         16                   12                    20                     16                 28       2
7                    March                90              14           333            359             186                         24                   13                    30                     27                 37       3
0                    April               103              20           360            318             163                         11                   26                    32                     22                 77       4
8                      May                51               3           297            244             131                         21                   19                    15                     23                 29       5
6                     June                52               6           322            299             178                         12                   12                    21                     24                 20       6
5                     July                82              16           310            252             167                         20                   19                    36                     27                 60       7
1                   August                93              20           354            245             157                         26                    6                    32                     21                 53       8
11               September               123              22           272            215             163                         14                    9                    23                     15                 59       9
10                 October               117              31           342            235             163                         21                   21                    27                      7                101      10
9                 November               110              33           292            193             143                         17                   18                    24                     25                 63      11
2                 December                93              15           211            185             134                         11                   17                    17                     15                 63      12


'''

# sort
#print(e.to_string())
e.plot(kind='line')


############################# FILTERING #############################
# Looking for the top 3 jobs
top3counts=d['job_title_short'].value_counts().head(3)
top3counts =top3counts.index.tolist()
print(top3counts)
# ['Data Analyst', 'Data Engineer', 'Data Scientist']


ee= e[top3counts].plot(kind='line')
plt.title('Monthly Job Posting for Top Data Jobs in BE')
plt.xlabel('2023')
plt.ylabel('Job Count')
plt.legend()
#plt.show()
ee.clear()


h = pd.read_csv('data/software_csv.csv', index_col='month')
i= h.copy()
i.drop(columns=['monthn'], inplace=True)
print(i.info())
print(i.to_string())

j= e.merge(i, on= 'month')

print(j.to_string())

top5 = (
    j.sum()
    .sort_values(ascending=False)
    .head()
    .index
    .to_list()
)
print(top5)

############################# PLOT #############################
j[top5].plot(kind='line')
plt.title('Monthly Job Posting for Top Data Jobs in BE')
plt.xlabel('2023')
plt.ylabel('Job Count')
plt.ylim(0,20000)
plt.legend()
#plt.show()

# We want to concatenate two different datasets


k = pd.read_csv('data/job_postings_jan.csv', index_col=0)
l = pd.read_csv('data/job_postings_feb.csv', index_col=0)
m = pd.concat([k,l], ignore_index=True)
print(m.to_string())

#simmulating data to create 12 files one for each month

d= dt.copy()
print(d.info())
d['dt'] = pd.to_datetime(d['job_posted_date'])
print(d.info())
d['month'] = d['dt'].dt.strftime('%b')
print(d.head().to_string())

'''
We want to create something like the following dictionary, one name variable which is the string and the value a dataset with the same name
dic_months ={
    'Jan': df_jan,
    'Feb' : df_feb ,
    'Mar' : df_mar ,
    'Apr' : df_apr ,
    'May' : df_may ,
    'Jun' : df_jun ,
    'Jul' : df_jul ,
    'Aug' : df_aug ,
    'Sep' : df_sep ,
    'Oct' : df_oct ,
    'Nov' : df_nov ,
    'Dec' : df_dec

}


'''


months = d['month'].unique()
dict_months = {month: d[d['month'] == month ] for month in months }
print(dict_months)

'''
{'Jan':        Unnamed: 0    job_title_short  ...                  dt month
0              20     Data Scientist  ... 2023-01-31 13:53:38   Jan
2             131      Data Engineer  ... 2023-01-28 13:48:30   Jan
10            453   Business Analyst  ... 2023-01-07 13:17:54   Jan
18            987  Software Engineer  ... 2023-01-20 14:16:36   Jan
27           1553       Data Analyst  ... 2023-01-24 13:26:09   Jan
...           ...                ...  ...                 ...   ...
12073      785388      Data Engineer  ... 2023-01-02 06:42:10   Jan
12074      785424   Business Analyst  ... 2023-01-02 06:42:00   Jan
12075      785460     Data Scientist  ... 2023-01-10 06:23:56   Jan
12076      785505       Data Analyst  ... 2023-01-27 06:29:52   Jan
12077      785518      Data Engineer  ... 2023-01-10 06:24:10   Jan

[1592 rows x 20 columns], 'May':        Unnamed: 0       job_title_short  ...                  dt month
1             120  Senior Data Engineer  ... 2023-05-04 13:23:35   May
42           2572         Data Engineer  ... 2023-05-31 14:03:40   May
48           2778   Senior Data Analyst  ... 2023-05-10 13:44:09   May
50           2847          Data Analyst  ... 2023-05-04 13:23:14   May
128          6576          Data Analyst  ... 2023-05-29 13:29:38   May
...           ...                   ...  ...                 ...   ...
11905      772129     Software Engineer  ... 2023-05-03 01:22:43   May
12011      780948     Software Engineer  ... 2023-05-10 07:52:51   May
12019      781203         Data Engineer  ... 2023-05-11 06:44:23   May
12039      782441        Data Scientist  ... 2023-05-16 07:31:42   May
12067      784899         Data Engineer  ... 2023-05-07 06:37:45   May


'''
# in the case we want only the first quarter data
n=pd.concat([dict_months['Jan'], dict_months['Feb'] , dict_months['Mar'] ], ignore_index=True)
print(n)
n['month'].value_counts().plot(kind='bar')
plt.title('Monthly Job Posting for Top Data Jobs in BE')
plt.xlabel('2023')
plt.ylabel('Job Count')
plt.ylim(0,3000)
plt.legend()
#plt.show()


n.to_excel('data/quarter1.xlsx')


############################# APPLY TO A COLUMN #############################
dt = pd.read_csv('C:/Users/USUARIO/projects/python/basics/data/data_jobs_be.csv', sep = '\t')
d= dt.copy()
print(d.info())
d['dt'] = pd.to_datetime(d['job_posted_date'])
print(d.info())
d['month'] = d['dt'].dt.strftime('%B')
print(d.head().to_string())

#There are missing values and the idea is to impute with the mean
print(d['salary_year_avg'])

#this take only the rows of the variable with NO missing values
print(d[ pd.notna( d['salary_year_avg'] ) ].to_string())

#this will take only the variable at the end with no missing values
# d[ pd.notna( d['salary_year_avg'] ) ]['salary_year_avg']
o= d[ pd.notna( d['salary_year_avg'] ) ].copy()
# We forecast the next salary based on an inflation of 3%
def projected_salary(salary):
    return salary*1.03

o['salary_next_year_avg']= o['salary_year_avg'].apply(projected_salary)

print(o[ ['salary_next_year_avg', 'salary_year_avg'] ])

#Using an anonymous function instead does the same as before
o['salary_next_year_avg']= o['salary_year_avg'].apply(lambda salary:salary*1.03)

print(o[ ['salary_next_year_avg', 'salary_year_avg'] ])


# all the previous steps actually not needed; the same is achieve hereunder

o['salary_next_year_avg']= o['salary_year_avg']*1.03

print(o[ ['salary_next_year_avg', 'salary_year_avg'] ])

############################# STRING TO LIST #############################
import pandas as pd
import ast

dt = pd.read_csv('C:/Users/USUARIO/projects/python/basics/data/data_jobs_be.csv', sep = '\t')
d= dt.copy()
print(d.info())

# we want to make a list for each entry of the job skills, the idea is to transform each entry from string
# to a list, and then to apply a function to each list
type(d['job_skills'][0])

'''
d['job_skills'][0]
"['r', 'python', 'sql', 'pandas', 'numpy', 'scikit-learn', 'matplotlib', 'hadoop', 'spark']"
type(d['job_skills'][0])
<class 'str'>
'''

type(ast.literal_eval(d['job_skills'][0]))

'''
type(ast.literal_eval(d['job_skills'][0]))
<class 'list'>

'''

def string2list(skill_string):
    if pd.notna(skill_string):
        return ast.literal_eval(skill_string)

d['job_skills1'] = d['job_skills'].apply(string2list)

print(d.head().to_string())

##################################### LAMBDA FUNCTION  #####################################


d['job_skills1'] = d['job_skills'].apply(
    lambda skill_string:
        ast.literal_eval(skill_string)
        if pd.notna(skill_string)
        else skill_string
                                            )


print(d.head().to_string())


############################ APPLY ##############################################################
'''
   Unnamed: 0       job_title_short                           job_title       job_location               job_via job_schedule_type  job_work_from_home search_location      job_posted_date  job_no_degree_mention  job_health_insurance job_country salary_rate  salary_year_avg  salary_hour_avg      company_name                                                                                  job_skills                                                                                                                                                                  job_type_skills                                                               job_skills1
0          20        Data Scientist                      Data Scientist  Zaventem, Belgium    via BeBee Belgique         Full-time               False         Belgium  2023-01-31 13:53:38                  False                 False     Belgium         NaN              NaN              NaN          Devoteam  ['r', 'python', 'sql', 'pandas', 'numpy', 'scikit-learn', 'matplotlib', 'hadoop', 'spark']                                                       {'libraries': ['pandas', 'numpy', 'scikit-learn', 'matplotlib', 'hadoop', 'spark'], 'programming': ['r', 'python', 'sql']}  [r, python, sql, pandas, numpy, scikit-learn, matplotlib, hadoop, spark]
1         120  Senior Data Engineer          Senior Azure Data Engineer   Antwerp, Belgium    via BeBee Belgique         Full-time               False         Belgium  2023-05-04 13:23:35                   True                 False     Belgium         NaN              NaN              NaN            Entico                             ['python', 'azure', 'databricks', 'spark', 'jupyter', 'docker']                                                            {'cloud': ['azure', 'databricks'], 'libraries': ['spark', 'jupyter'], 'other': ['docker'], 'programming': ['python']}                       [python, azure, databricks, spark, jupyter, docker]
2         131         Data Engineer                 Cloud Data Engineer  Mechelen, Belgium  via LinkedIn Belgium         Full-time               False         Belgium  2023-01-28 13:48:30                  False                 False     Belgium         NaN              NaN              NaN           Telenet     ['sql', 'cassandra', 'aws', 'hadoop', 'spark', 'kafka', 'word', 'docker', 'kubernetes']  {'analyst_tools': ['word'], 'cloud': ['aws'], 'databases': ['cassandra'], 'libraries': ['hadoop', 'spark', 'kafka'], 'other': ['docker', 'kubernetes'], 'programming': ['sql']}     [sql, cassandra, aws, hadoop, spark, kafka, word, docker, kubernetes]
3         148          Data Analyst                Tableau BI Developer  Brussels, Belgium     via BR Proud Jobs        Contractor               False         Belgium  2023-03-02 13:14:19                   True                 False     Belgium         NaN              NaN              NaN  Apollo Solutions                                                                ['python', 'sql', 'tableau']                                                                                                                 {'analyst_tools': ['tableau'], 'programming': ['python', 'sql']}                                                    [python, sql, tableau]
4         150   Senior Data Analyst  Senior Consultant Data & Analytics            Belgium          via LinkedIn         Full-time               False         Belgium  2023-12-09 13:44:56     

'''
# the objective this time is to forecast the costs of salaries for the next year.
# we assume an inflation of 3% in regular workers but we think that for seniors the increase is of 5%
# we will navigate through the job title to identify seniors
o= d[ pd.notna( d['salary_year_avg'] ) ].copy()
# We forecast the next salary based on an inflation of 3%
import re
def projected_salary(row_dataset):
    if 'Senior' in row_dataset['job_title_short']:
        return row_dataset['salary_year_avg']*1.05
    else:
        return 1.03*row_dataset['salary_year_avg']

o['salary_next_year_avg']= o.apply(projected_salary, axis=1)

print(o[ ['job_title_short','salary_next_year_avg', 'salary_year_avg'] ])
'''

                 job_title_short  salary_next_year_avg  salary_year_avg
5                 Data Scientist            162225.000         157500.0
519    Machine Learning Engineer             91773.000          89100.0
546                 Data Analyst             56637.640          54988.0
773                 Data Analyst            169950.000         165000.0
1004                Data Analyst            114510.250         111175.0
1011               Data Engineer            101250.545          98301.5
1495               Data Engineer             75087.000          72900.0
1497               Data Engineer             91773.000          89100.0
1718        Senior Data Engineer             93555.000          89100.0

'''

############################# EXPLODE FUNCTION ############################
data = {
    'job_title_short': ['Data Analyst', 'Data Scientist', 'Data Engineer'],
    'job_skills': [['excel', 'sql', 'python'], ['python', 'r'], ['aws', 'python', 'airflow']]
}

df_skills = pd.DataFrame(data)
print(df_skills)
'''
  job_title_short              job_skills
0    Data Analyst    [excel, sql, python]
1  Data Scientist             [python, r]
2   Data Engineer  [aws, python, airflow]

'''
df_exploded = df_skills.explode('job_skills')

print(df_exploded)
'''
  job_title_short job_skills
0    Data Analyst      excel
0    Data Analyst        sql
0    Data Analyst     python
1  Data Scientist     python
1  Data Scientist          r
2   Data Engineer        aws
2   Data Engineer     python
2   Data Engineer    airflow
'''



#using the job data
import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt

import ast
dt = pd.read_csv('C:/Users/USUARIO/projects/python/basics/data/data_jobs_be.csv', sep = '\t')
d= dt.copy()
p=d.copy()

p['job_skills1']=p['job_skills'].apply(lambda x: ast.literal_eval(x) if pd.notna(x)  else x )
print(p[ ['job_skills1','job_skills'] ].head().to_string())

'''
                                                                job_skills1                                                                                  job_skills
0  [r, python, sql, pandas, numpy, scikit-learn, matplotlib, hadoop, spark]  ['r', 'python', 'sql', 'pandas', 'numpy', 'scikit-learn', 'matplotlib', 'hadoop', 'spark']
1                       [python, azure, databricks, spark, jupyter, docker]                             ['python', 'azure', 'databricks', 'spark', 'jupyter', 'docker']
2     [sql, cassandra, aws, hadoop, spark, kafka, word, docker, kubernetes]     ['sql', 'cassandra', 'aws', 'hadoop', 'spark', 'kafka', 'word', 'docker', 'kubernetes']
3                                                    [python, sql, tableau]                                                                ['python', 'sql', 'tableau']
4                                                                   [excel]                                                                                   ['excel']

'''
print(p.info())
q=p.explode('job_skills1', ignore_index=True).copy()
print(q.info())
print(q[['job_skills1', 'job_skills', 'job_title_short']].head(3).to_string())


'''

  job_skills1                                                                                  job_skills job_title_short
0           r  ['r', 'python', 'sql', 'pandas', 'numpy', 'scikit-learn', 'matplotlib', 'hadoop', 'spark']  Data Scientist
1      python  ['r', 'python', 'sql', 'pandas', 'numpy', 'scikit-learn', 'matplotlib', 'hadoop', 'spark']  Data Scientist
2         sql  ['r', 'python', 'sql', 'pandas', 'numpy', 'scikit-learn', 'matplotlib', 'hadoop', 'spark']  Data Scientist
'''
plt.close('all')
qq = q['job_skills1'].value_counts().head(10).plot(kind='bar')
plt.title('Monthly Job Posting for Top Data Jobs in BE')
plt.xlabel('2023')
plt.ylabel('Job Count')
plt.ylim(0,5000)
plt.legend()
#plt.show()

r=q.groupby(['job_skills1', 'job_title_short']).size()
# this r report is a series format; the idea is to make a dataframe out of it
'''
job_skills1      job_title_short          
airflow          Business Analyst                2
                 Cloud Engineer                 10
                 Data Analyst                   15
                 Data Engineer                 269
                 Data Scientist                 35
                 Machine Learning Engineer      13
                 Senior Data Analyst             1
                 Senior Data Engineer           37
                 Senior Data Scientist          18
                 Software Engineer              16
alteryx          Business Analyst                5
                 Cloud Engineer                  1
                 Data Analyst                   37
                 Data Engineer                  45
                 Data Scientist                 17
                 Machine Learning Engineer       1
                 Senior Data Analyst            16
                 Senior Data Engineer            8
                 Senior Data Scientist           2
'''
r=q.groupby(['job_skills1', 'job_title_short']).size().reset_index(name='skill_count')
print(r)
'''

     job_skills1            job_title_short  skill_count
0        airflow           Business Analyst            2
1        airflow             Cloud Engineer           10
2        airflow               Data Analyst           15
3        airflow              Data Engineer          269
4        airflow             Data Scientist           35
...          ...                        ...          ...
1179        zoom               Data Analyst            6
1180        zoom              Data Engineer           13
1181        zoom             Data Scientist            1
1182        zoom  Machine Learning Engineer            1
1183        zoom          Software Engineer            1
'''
s=r.sort_values(by='skill_count', ascending =False)
print(s)

t = s[s['job_title_short'] == 'Data Analyst'].head(10)

print(t.info())
print(t.to_string())

'''
     job_skills1 job_title_short  skill_count
968          sql    Data Analyst         1519
254        excel    Data Analyst         1020
755       python    Data Analyst          993
710     power bi    Data Analyst          880
850          sas    Data Analyst          794
1038     tableau    Data Analyst          527
782            r    Data Analyst          463
840          sap    Data Analyst          458
67         azure    Data Analyst          436
1162        word    Data Analyst          209

'''
plt.close('all')
t.plot(kind='barh', y='skill_count', x='job_skills1')
plt.gca().invert_yaxis()
plt.legend().set_visible(False)
#plt.show()

# we are changing the ordering of the vertical axes ordering in the graph using pyplot.gca
# we identify the axis; then we change it

##################################### SERIES PLOT ##########################################
#using the job data
import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt

import ast
dt = pd.read_csv('C:/Users/USUARIO/projects/python/basics/data/data_jobs_be.csv', sep = '\t')
d= dt.copy()
d['dt'] = pd.to_datetime(d['job_posted_date'])
d['month'] = d['dt'].dt.strftime('%b')
d['monthn'] = d['dt'].dt.month

p= d[ d['job_title_short'] ==  'Data Analyst'].copy()

p['job_skills1']=p['job_skills'].apply(lambda x: ast.literal_eval(x) if pd.notna(x)  else x )
q=p.explode('job_skills1', ignore_index=True).copy()


#q.to_csv('C:/Users/USUARIO/projects/python/basics/data/delete.csv', sep = ',')


r=q.pivot_table(index='monthn', columns='job_skills1', aggfunc='size', fill_value=0)
#

# this adds a row of totals. It creates an index
r.loc['Total']= r.sum()
'''

job_skills  ['alteryx', 'tableau']  ['alteryx']  ...  ['word']  ['zoom']
monthn                                           ...                    
1                                0            1  ...         0         1
2                                0            0  ...         0         0
3                                0            1  ...         1         0
4                                0            0  ...         2         0
5                                0            0  ...         1         0
6                                0            0  ...         2         0
7                                0            0  ...         1         0
8                                0            0  ...         5         0
9                                0            0  ...         2         0
10                               0            0  ...         0         0
11                               2            1  ...         2         0
12                               0            0  ...         5         0
Total                            2            3  ...        21         1
'''
'''
monthn	['alteryx', 'tableau']	['alteryx']	['excel']	['express', 'excel', 'sap']
        1	0	1	20	0
        2	0	0	7	3
        3	0	1	13	0
        4	0	0	12	0
        5	0	0	21	0
        6	0	0	16	0
        7	0	0	25	0
        8	0	0	19	0
        9	0	0	11	0
        10	0	0	13	0
        11	2	1	11	0
        12	0	0	5	0
Total	    2	3	173	3

'''
# This locates the Total row and sort the total values descending
r.loc['Total'].sort_values(ascending=False)
# We want to know the idexes or column names for which the totals are the highest ordered descending.
# The idex for a total of 173 is 'excel'. here the index corresponds to the column name
'''
r.loc['Total'].sort_values(ascending=False)
job_skills
['excel']                                                                                                173
['sql', 'r', 'python', 'sas', 'sas', 'ssis', 'power bi']                                                 126
['sql', 'sas', 'sas', 'r', 'python', 'aws', 'azure', 'excel', 'power bi', 'tableau']                     120
['sql', 'c#', 'python', 'r', 'sql server', 'ssrs', 'power bi', 'excel', 'ssis', 'sharepoint', 'flow']    110
['sap']                                                                                                   94
                                                                                                        ... 
['microsoft teams']                                                                                        1
['linux']                                                                                                  1
['drupal']                                                                                                 1
['swift']                                                                                                  1

'''
plt.close('all')
s = r[  r.loc['Total'].sort_values(ascending=False).index].copy()
s = s.drop('Total')
s.iloc[:, :5].plot(kind='line')
plt.title('5 most common asked skills for a data analyst in BE')
plt.xlabel('')
plt.ylabel('Job Count')
plt.ylim(0,200)
plt.legend()
plt.show()


################################### DATA MANAGEMENT or the Plotnine dataset ######################################

a = pd.read_csv('C:/Users/USUARIO/projects/python/basics/data/data_jobs.csv')
a.info()
a.head()
a.tail()
a.info()
a.isnull()
print(a.head(10).to_string())
'''
RangeIndex: 120719 entries, 0 to 120718
Data columns (total 7 columns):
 #   Column           Non-Null Count   Dtype  
---  ------           --------------   -----  
 0   Unnamed: 0       120719 non-null  int64  
 1   job_title        120719 non-null  object 
 2   salary_year_avg  120719 non-null  float64
 3   dt               120719 non-null  object 
 4   month            120719 non-null  object 
 5   monthn           120719 non-null  int64  
 6   job_skills1      118886 non-null  object 
dtypes: float64(1), int64(2), object(4)
memory usage: 6.4+ MB
   Unnamed: 0            job_title  salary_year_avg  ... month monthn  job_skills1
0          28  CRM Data Specialist         109500.0  ...   Aug      8         gdpr
1          28  CRM Data Specialist         109500.0  ...   Aug      8        excel
2          77        Data Engineer         140000.0  ...   Jun      6      mongodb
3          77        Data Engineer         140000.0  ...   Jun      6      mongodb
4          77        Data Engineer         140000.0  ...   Jun      6       python
5          77        Data Engineer         140000.0  ...   Jun      6            r
6          77        Data Engineer         140000.0  ...   Jun      6          sql
7          77        Data Engineer         140000.0  ...   Jun      6        mysql
8          77        Data Engineer         140000.0  ...   Jun      6      mariadb
9          77        Data Engineer         140000.0  ...   Jun      6       oracle

[10 rows x 7 columns]

Process finished with exit code 0
'''


a.columns = ['Id','Job','Salary','Location', 'Via', 'Home', 'DTC', 'Rate', 'Company', 'DTC1','Month','Monthn','Skills', 'Country']
print(a.head(10).to_string())
"""
   Id                  Job    Salary                   dt Month  Monthn   Skills
0  28  CRM Data Specialist  109500.0  2023-08-01 13:37:57   Aug       8     gdpr
1  28  CRM Data Specialist  109500.0  2023-08-01 13:37:57   Aug       8    excel
2  77        Data Engineer  140000.0  2023-06-26 14:22:54   Jun       6  mongodb
3  77        Data Engineer  140000.0  2023-06-26 14:22:54   Jun       6  mongodb
4  77        Data Engineer  140000.0  2023-06-26 14:22:54   Jun       6   python
5  77        Data Engineer  140000.0  2023-06-26 14:22:54   Jun       6        r
6  77        Data Engineer  140000.0  2023-06-26 14:22:54   Jun       6      sql
7  77        Data Engineer  140000.0  2023-06-26 14:22:54   Jun       6    mysql
8  77        Data Engineer  140000.0  2023-06-26 14:22:54   Jun       6  mariadb
9  77        Data Engineer  140000.0  2023-06-26 14:22:54   Jun       6   oracle
"""
b=a.drop_duplicates()
b.info()
b=pd.DataFrame(b)


b['DT'] = pd.to_datetime(b['DTC'])
b['Year'] = b['DT'].dt.year
print(b.info())
# The first dt has relation with the variable dt within the dataset
c=b.groupby(['Job']).size().reset_index(name='Job_Count')
print(c)
'''
None
                         Job  Job_type
0           Business Analyst      2192
1             Cloud Engineer       319
2               Data Analyst     21102
3              Data Engineer     32457
4             Data Scientist     29945
5  Machine Learning Engineer      3123
6        Senior Data Analyst      4989
7       Senior Data Engineer     12885
8      Senior Data Scientist      8864
9          Software Engineer      2639
'''
d =pd.merge(b, c, on='Job', how='left')
e=b.groupby(['Job', 'Skills']).size().reset_index(name='Job_Skill_Count')
print(e)
f =pd.merge(d, e, on=['Job', 'Skills'], how='left').sort_values(by=['Job', 'Skills'])


#f.to_csv('C:/Users/USUARIO/projects/python/basics/data/Dataframes.csv', sep = ',', index=False)

