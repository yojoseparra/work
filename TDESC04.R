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




library(officer)
library(readxl)
library(flextable)
library(officer)
library(knitr)
library(sqldf)
library(reshape2)
library(dplyr)

use_df_printer()


set_flextable_defaults(
  border.color = "#AAAAAA", font.family = "Arial",
  font.size = 6, padding = 2,
  line_spacing=0.7,
  text.align='center',
  table.layout = 'autofit'
  
  
  
)

i = 6
z <- read_excel("data/titles.xls")
titlecd = toString(z[i,1])
title = toString(z[i,2])
docname = paste0(titlecd,'.docx')
footnote_jose= toString(z[i,3])
use_df_printer()
a = read.csv('data/TDESC04.csv')

# there are many reps in this dataset caused by reps in the original data i


b=a[a$Parameter %in% c('COL1','COL2','N'),c('Country','Job', 'Parameter','aval') ]

#labels
b[b$Parameter %in% c('COL1'),c('Parameter') ] <- 'Median (IQR)'
b[b$Parameter %in% c('COL2'),c('Parameter') ] <- 'Mean (SD)'


c = dcast( b , Country+Parameter~Job )





flextable(c)%>% 
  add_footer_lines( paste('Note:',footnote_jose) )%>% 
  add_header_lines(paste('Complete Cases Set') )%>% 
  add_header_lines(paste(titlecd, title) )








#```

################################ HERE THE RMD DOC ENDS                 ##########################################
################################ This is done to have an output in txt ##########################################
options(max.print=1000000)
#getwd()


sink(file = paste0('out/', titlecd, '.log' ) , append = TRUE)

kable(c)


savehistory(file = paste0('out/', titlecd, '_verbose.log' ) )

timestamp(stamp = date(),
          prefix = "##------ ", suffix = " ------##",
          quiet = FALSE)
Sys.timezone()
Author

sink()
#################################################################

