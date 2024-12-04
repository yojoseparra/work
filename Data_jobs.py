# Loading Data
# Importing Libraries
import pandas as pd
from datasets import load_dataset
import matplotlib.pyplot as plt
import ast


# Loading Data
b = load_dataset('lukebarousse/data_jobs')
c = b['train'].to_pandas()
d =c.copy()
d['index_original_rows'] = d.index



d['job_skills1']=d['job_skills'].apply(lambda x: ast.literal_eval(x) if pd.notna(x)  else x )

e=d.explode('job_skills1', ignore_index=True).copy()





# keeping selecter columns and rename
f=e[ ['index_original_rows','job_title_short'   , 'salary_year_avg','job_location', 'job_via',                'job_work_from_home', 'job_posted_date', 'salary_rate',     'company_name' ,'job_skills', 'job_skills1', 'job_country'] ].copy()

f.columns = ['index', 'Job',             'Salary'      ,'Location',        'Via',                'Home',                   'DTC'           , 'Rate',           'Company'     ,'job_skills','Skills'      , 'Country']

print(f.head(5).to_string())
# Creating Dates variables
g= f.copy()

g['DT'] = pd.to_datetime(g['DTC'])

g['Month'] = g['DT'].dt.strftime('%B')
g['Month'] = g['DT'].dt.strftime('%m')
g['Year'] = g['DT'].dt.year
g.reset_index(inplace=True)

print(g.head().to_string())

#this will take only the variable at the end with no missing values. we assume missing at random here
g.info()
h= g[ pd.notna( g['Salary'] ) ].copy()

# We forecast the next salary based on an inflation of 3%. This data is from 2023

h['Salary']= h['Salary'].apply(lambda salary:salary*1.03)
h.info()


# The first dt has relation with the variable dt within the dataset
# the a dataset is the data with the list of the european countries
import pandas as pd
from datasets import load_dataset

dataset = load_dataset('estadistico/europe_countries')
a = dataset['train'].to_pandas()

print(a.head().to_string())

# Selecting all european countries
i =pd.merge(h, a, on='Country', how='inner')
print("#####################################")
print(i.info())


j = i[i["Analyze"] == 'Y'].copy()
j.to_csv('data/Data_Jobs.csv', sep = ',', index=False)