



sink("RMD-EXE_VERBOSE.R.txt")


rmarkdown::render("TDESC02.Rmd", 
                  output_file = 'out/TDESC02.docx')
rmarkdown::render("TDESC02.Rmd", 
                  output_file = 'out/TDESC02.html')

rmarkdown::render("LDESC01.Rmd", 
                  output_file = 'out/LDESC01.docx')
rmarkdown::render("LDESC01.Rmd", 
                  output_file = 'out/LDESC01.html')

rmarkdown::render("LDESC02.Rmd", 
                  output_file = 'out/LDESC02.docx')
rmarkdown::render("LDESC02.Rmd", 
                  output_file = 'out/LDESC02.html')


rmarkdown::render("LDESC03.Rmd", 
                  output_file = 'out/LDESC03.docx')
rmarkdown::render("LDESC03.Rmd", 
                  output_file = 'out/LDESC03.html')


rmarkdown::render("TDESC04.Rmd", 
                  output_file = 'out/TDESC04.docx')
rmarkdown::render("TDESC04.Rmd", 
                  output_file = 'out/TDESC04.html')


rmarkdown::render("LDESC05.Rmd", 
                  output_file = 'out/LDESC05.docx')
rmarkdown::render("LDESC05.Rmd", 
                  output_file = 'out/LDESC05.html')

rmarkdown::render("LDESC06.Rmd", 
                  output_file = 'out/LDESC06.docx')
rmarkdown::render("LDESC06.Rmd", 
                  output_file = 'out/LDESC06.html')

rmarkdown::render("LDESC07.Rmd", 
                  output_file = 'out/LDESC07.docx')
rmarkdown::render("LDESC07.Rmd", 
                  output_file = 'out/LDESC07.html')


rmarkdown::render("LDESC08.Rmd", 
                  output_file = 'out/LDESC08.docx')
rmarkdown::render("LDESC08.Rmd", 
                  output_file = 'out/LDESC08.html')
Sys.time()
getwd()
sink()

