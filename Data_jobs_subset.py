
import pandas as pd
from datetime import datetime
from plotnine import *
from plotnine.mapping.evaluation import reorder
import numpy as np
import matplotlib.pyplot as plt

a = pd.read_csv('data/Data_Jobs.csv')

skills =['aws'
,'spark'
,'airflow'
,'snowflake'
,'python'
,'looker'
,'databricks'
,'sql'
,'go'
,'pandas'
,'azure'
,'gcp'
,'redshift'
,'java'
,'bigquery'
,'kafka'
,'pyspark'
,'oracle'
,'docker'
,'scala'
,'git'
,'pytorch'
,'tensorflow'
,'kubernetes'
,'numpy'
,'terraform'
,'postgresql'
,'hadoop'
,'scikit-learn'
,'mysql'
,'tableau'
,'jira'
,'sql server'
'gdpr' ]


b=a[ a['Skills'].isin(skills) ]
c= b[["index","Country","Job", "Skills"]]
d = c.drop_duplicates().sort_values(by=["Country","Job", "Skills"], ascending=False)


d.to_csv('data/Data_Jobs_Subset.csv', sep = ',', index=False)