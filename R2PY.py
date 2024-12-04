
# The objective is making calculations in R and to send the results to Python
#import os
# os.environ['R_HOME'] ='C:/Users/USUARIO/joseconda/envs/werk/Lib/R' 

import pandas as pd
import rpy.objects as robjects
from rpy2.robjects import pandas2ri
from rpy2.robjects.packages import importr



pandas2ri.activate()
utils = importr('utils')
dplyr= importr('dplyr')

robjects.r('data(iris)')

robjects.r('''
library(dplyr)
           iris_summary = iris %>%
           group_by(Species) %>%
           summarise(
            Avg_Sepal.Length = mean(Sepal.Length),
            Avg_Sepal.Width = mean(Sepal.Width)
           )
'''
)
'''




'''

#iris_summary = pandas2ri.rpy2py(robjects.r['iris_summary'])

#print(iris_summary)
#print(type(iris_summary))

use_condaenv(condaenv = "portfolio", conda = "auto", required = TRUE)

py_config()