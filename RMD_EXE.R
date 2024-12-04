



sink("RMD-EXE_VERBOSE.R.txt")


rmarkdown::render("TDESC02.Rmd", 
                  output_file = 'out/TDESC02.docx')
rmarkdown::render("TDESC02_PDF.Rmd", 
                  output_file = 'out/TDESC02_PDF.pdf')





rmarkdown::render("LDESC01.Rmd", 
                  output_file = 'out/LDESC01.docx')
rmarkdown::render("LDESC01.Rmd", 
                  output_file = 'out/LDESC01.pdf')

rmarkdown::render("LDESC02.Rmd", 
                  output_file = 'out/LDESC02.docx')
rmarkdown::render("LDESC02.Rmd", 
                  output_file = 'out/LDESC02.pdf')


rmarkdown::render("LDESC03.Rmd", 
                  output_file = 'out/LDESC03.docx')
rmarkdown::render("LDESC03.Rmd", 
                  output_file = 'out/LDESC03.pdf')


rmarkdown::render("TDESC04.Rmd", 
                  output_file = 'out/TDESC04.docx')
rmarkdown::render("TDESC04_PDF.Rmd", 
                  output_file = 'out/TDESC04_PDF.pdf')


rmarkdown::render("LDESC05.Rmd", 
                  output_file = 'out/LDESC05.docx')
rmarkdown::render("LDESC05.Rmd", 
                  output_file = 'out/LDESC05.pdf')

rmarkdown::render("LDESC06.Rmd", 
                  output_file = 'out/LDESC06.docx')
rmarkdown::render("LDESC06.Rmd", 
                  output_file = 'out/LDESC06.pdf')

rmarkdown::render("LDESC07.Rmd", 
                  output_file = 'out/LDESC07.docx')
rmarkdown::render("LDESC07.Rmd", 
                  output_file = 'out/LDESC07.pdf')


rmarkdown::render("LDESC08.Rmd", 
                  output_file = 'out/LDESC08.docx')
rmarkdown::render("LDESC08.Rmd", 
                  output_file = 'out/LDESC08.pdf')
Sys.time()
getwd()
sink()

