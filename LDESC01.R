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
#library(ggplot2)
library(crosstable)
library(readxl)
library(flextable)
library(officer)
library(dplyr)
library(knitr)


use_df_printer()

set_flextable_defaults(
  border.color = "#AAAAAA", font.family = "Arial",
  font.size = 6, padding = 2,
  line_spacing=0.7,
  text.align='center',
  table.layout = 'autofit'
  
  
  
)



z <- read_excel("data/titles.xls")
titlecd = toString(z[2,1])
title = toString(z[2,2])
docname = paste0(titlecd,'.docx')
footnote_jose= toString(z[2,3])
use_df_printer()
a = read.csv("data/EDA1_Bargraphs_3.0.csv")

b=a[a$paramtyp =='',c('country', 'job','paramcd', 'aval', 'avalu')]
names(b) = c('Country', 'IT Job','Statistic', 'Value', 'Currency')

flextable(b)%>% 
  add_footer_lines( paste('Note:',footnote_jose) )%>% 
  add_header_lines(paste('Complete Cases Set') )%>% 
  add_header_lines(paste(titlecd, title) )%>% 
  line_spacing( space = 0.7, part = "all")









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

