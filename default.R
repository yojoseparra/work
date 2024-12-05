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

