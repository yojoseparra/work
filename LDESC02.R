
z <- read_excel("data/titles.xls")
titlecd = toString(z[3,1])
title = toString(z[3,2])
docname = paste0(titlecd,'.docx')

sink(file = paste0('out/', titlecd, '.txt' ) )
sink(append = TRUE, type="message")
options(max.print=1000000)

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


footnote_jose= toString(z[3,3])
use_df_printer()
a = read.csv("data/EDA1_Bargraphs_3.2.csv")

b=a[a$paramtyp =='',c('param', 'job','paramcd', 'aval', 'avalu')]
names(b) = c('Country', 'IT Job','Statistic', 'Value', 'Currency')

flextable(b)%>% 
  add_footer_lines( paste('Note:',footnote_jose) )%>% 
  add_header_lines(paste('Complete Cases Set') )%>% 
  add_header_lines(paste(titlecd, title) )%>% 
  line_spacing( space = 0.7, part = "all")


b
sink()





