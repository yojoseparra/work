# These first 8 lines delete history, 

clearhistory <- function() {
  write("", file=".blank")
  loadhistory(".blank")
  unlink(".blank")
}
clearhistory()

###############################HERE THE RMD DOC STARTS ################# 




# ---
#   author: "Jose Parra"
# date: "11NOV2024"
# output:
#   pdf_document: default
# word_document:
#   reference_docx: doc_styles_vert.docx
# ---
# 
# ```{r, message=FALSE, warning=FALSE, echo=FALSE}



library(readxl)
library(knitr)
library(officer)
#library(ggplot2)
library(crosstable)

library(flextable)
library(officer)
library(dplyr)

z <- read_excel("data/titles.xls")
titlecd = toString(z[3,1])
title = toString(z[3,2])
docname = paste0(titlecd,'.docx')





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


#```

################################ HERE THE RMD DOC ENDS ###################


################################ DELETE, this is done to have an output in txt #############################
options(max.print=1000000)
#getwd()


sink(file = paste0('out/', titlecd, '.log' ) , append = TRUE)

kable(b)


savehistory(file = paste0('out/', titlecd, '_verbose.log' ) )

timestamp(stamp = date(),
          prefix = "##------ ", suffix = " ------##",
          quiet = FALSE)
Sys.timezone()


sink()
#################################################################







