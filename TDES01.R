# -------------------------------------
# Script: 
  Author= "YoJoseParra" 
# Purpose: 
# Notes:
# -------------------------------------
#################################### These next 8 lines delete history,  #########################################
clearhistory <- function() {write("", file=".blank"); loadhistory(".blank");unlink(".blank")}; clearhistory()
##################################################################################################################

##HERE THE RMD DOC STARTS. Unquote to make a markdown file after code completion #################################
# ---
# author: "Jose Parra"
# date: ""
# output:
#   pdf_document: default
# word_document:
#   reference_docx: doc_styles_vert.docx
# ---
# 
# ```{r, message=FALSE, warning=FALSE, echo=FALSE}


---
  author: "Jose Parra"
date: "07NOV2024"
output: 
  word_document:
  reference_docx: doc_styles.docx

---
  
  ```{r, message=FALSE, warning=FALSE, echo=FALSE}
# this is a code to work with python and r toguether
library(officer)
#library(ggplot2)
library(crosstable)
library(readxl)
library(reticulate)
library(knitr)
use_python("C:/Users/USUARIO/joseconda/envs/portfolio/python.exe")

z <- read_excel("data/titles.xls")
titlecd = toString(z[1,1])
title = toString(z[1,2])
docname = paste0(titlecd,'.docx')
footnote_jose= toString(z[1,3])

a = read.csv('data/Data_Jobs.csv')




a = r.a
import pandas as pd
import datetime
import plotnine
import numpy as np
import matplotlib.pyplot as plt
#a = pd.read_csv('data/Data_jobs.csv')
# Bargraphs .3.1 MIN
c=a.pivot_table(values='Salary', columns='Job', index='Country', aggfunc='min')



```









#```

################################ HERE THE RMD DOC ENDS                 ##########################################
################################ This is done to have an output in txt ##########################################
options(max.print=1000000)
#getwd()


sink(file = paste0('out/', titlecd, '.log' ) , append = TRUE)

kable(b)


savehistory(file = paste0('out/', titlecd, '_verbose.log' ) )

timestamp(stamp = date(),
          prefix = "##------ ", suffix = " ------##",
          quiet = FALSE)
Sys.timezone()
Author

sink()
#################################################################

