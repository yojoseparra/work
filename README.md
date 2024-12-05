# Overview

Welcome to my analysis of the European job market (in 15 european countries) with the most IT Job opportunities in data analyst roles in 2023. This project was created to identifythe job trends to better prepare for a job application in the IT sector as data analyst. It delves into the top-paying and in-demand skills to help find optimal job opportunities for data analysts in Europe.

The data sourced from Luke Barousse, which provides a foundation for my analysis, containing detailed information on job titles, salaries, locations, and essential skills. Through a series of Python scripts. Luke teaches python through this dataset. 

Despite my project is based on Luke's data, it differs from his substantially as I'm motivated by other research questions and another slice of the data. I use another type of code and I use another software as well (RStudio + Python). Additionally, I do not blend text with code and I present outputs in Word, CSV or PDF. This is more the approach that I use with my clients as CSV can be normally opened in Excel where the client has the chance to interact with data by filter and looking at data if needed. Graphs are big format and they are not embed in text. Word files can be easily formatted if needed and can be copied and pasted in the final report. Most important outputs come along with the code that generated them and with the data along with other formats too: all files are named equally. Dus outputs and plots match the name of files that generated them. This might be simple practice, but you can be amazed how little is done on this aspect out there.

This analysis exercise is just an example. I am exemplifying here how to find data trends by plotting or tabulating data. I offer here a metodology on how to present an analysis to a client, not how to make a report. Formatting and grammar are not the main objective of this exercise. This is not an example on how to write a good assay nor a propedeutic piece of material to learn programming in Python. For this reason outputs might look not properly formatted or graphs might appear unfinished. This is normal as we explore the data, we focus less on the final product and more on finding trends. Only the final package is cleand and delivered, but this is not a final package. 

# How to Access Data or Outputs

Tables are better displayed in Microsoft Word ( /out folder) and graphs are made in big format (/plot folder). 

This is the top folder structure:

- **data**: this is a data folder. All comma separated files (.csv) are stored. this format opens easily with excel. All outputs and graphs come from this data. 
- **docs**: contains documents and this folder might not be of interest for this project. 
- **out**: It contains the tabular outputs presented in PDF and Word.
- **plot**: this is the output graphs folder. It contains only plots.

All documents hereunder can be directly accessed in this folders. Notice that I preffer having a look at data in the .CSVs or Word format, this this reason I added these documents here. PDFs are just for preview purposes and I discourage reading directly from them as rendering might be of low quality.

# Exploratory Data Analysis (EDA) of IT Jobs in EU in 2023

## Research Questions Regarding IT Data Jobs

Below are the questions I want to answer in my project:

1. What are the skills most in demand and how well are they paid?
2. What set of skills relate to each Job title?
3. How well do jobs and skills pay for Data Analysts in each european country?
4. What are the optimal skills for data analysts to learn? (High Demand AND High Paying) 

## Tools Used

For my deep dive into the data analyst job market, I harnessed the power of several key tools:

- **Python:** The backbone of my analysis, allowing me to analyze the data and find critical insights.I also used the following Python libraries:
    - **Pandas Library:** This was used to analyze the data. 
    - **Matplotlib Library:** I visualized the data.
    - **Plotnine Library:** Helped me create more advanced visuals using layered plots. 
- **Jupyter Notebooks:** The tool I used to run my Python scripts which let me easily include my notes and analysis.
- **Visual Studio Code:** My go-to for executing my Python scripts using conda.
- **Git & GitHub:** Essential for version control and sharing my Python code and analysis, ensuring collaboration and project tracking.
- **R Studio:** Essential to use RMD, Knitr, md and pandoc to render outputs in other formats easily using libraries to present outputs in word format.

Notice that it is not the interest of going through code snippets here, therefore, no code is display. but each output has a code file with the same name.

## Data 

Origin of the data is unknown. All we know is that it is available online https://huggingface.co/datasets/lukebarousse/data_jobs

## Data Imputation and missing data

I do not impute data, thus I'm assumming here missing at random. The dataset for europe is not that big and it has missing data. This can be missing not at random, as companies that require data analysts and pay lower than average might not publish any salary offer. The result might be that the means and medians calculated here are biased upwards, or in other words, that salary means and medians might look higher than in reality.

Scarce data from Europe makes plots unreliable. You will se very often 'n' in outputs, as we account for the amount of data by category to draw reasonable conclusions. There are outliers that can shift statistics as well. No outliers were removed as it is not clear that these are real outliers or just simple real data. 

### Variables

The most important variables are 'Country', 'Job', 'Skills' and 'Salary'. Salary is a numeric variable of yearly salary represented in USD, and can be given in any outputs as a 'mean', 'median', 'std', 'qrt' ... etc. It indicates the statistic of salary for a particular category.

Salary of 100 K is the same as 100.000 USD. Notice that the notation of thousands is '.' instead of european ',' thousands symbol is represented by a point instead of a comma.

## Exploratory Data Analysis

### EU IT Job posts (N=1488 job vacancies in 2023).


To focus my analysis on the EU job market, I apply filters to the dataset, narrowing down to roles based in the Eurozone. Only 15 countries had enough data up to a total of 1488 usable posts with salary information.

[TDESC02](/out/TDESC02.log)

TDESC02 table shows the total counts of job availabilities by country in 2023. Only these countries are displayed as they were those whose data was available.  

Values are presented in '000s. Table can be accessed in word, CSV or PDF format. TDESC02 is organized from left to right to show the most important countries and roles in terms of counts of job vacancies. Thus, for instance Germany accounted for about the 17% of total vacancies in europe. Other important countries were France (16%), Poland (13%), Spain (10%). The table is also organize by important Jobs, as it starts from Data Analyst (23%), Data Engineer (22%) and Data Scientist (18%) down to Cloud Engineeer (1%). 


## A 1.000 m high view  

The *first conclussion* can be that the most important jobs are Data Analyst,	Data Engineer,	Data Scientist in terms of jobs available as they acount roughly for the 60% of jobs available.

But before we enter into further detail, lets take a look at overall means. I did not want to give a number at this stage, but just derive those numbers directly from a simple unlabeled plot. [Min](/plot/EDA1%20Bargraphs%201.0%20MIN.png).

This first plot is the result of calculating the Minimum salary by job type regardless the country. We will see that salary offers accross countries may differ, but this is the first approach to have a rough estimate of an overall descriptive statistic. This estimate might not be precise but might be unbiased respect to the one calculated from the data. Let me explain you what I mean by that:

the plot of the 'Min' shows that an horizontal line can be safely done on top of the bars and that an overall average can be 46K dollars (46.000 USD).

Following the same logic it can be said that for other statistics we have the median of 110K, mean of  110K and max of 190K. This can be seeing in [Median](plot/EDA1%20Bargraphs%201.1%20Median.png), [Max](plot/EDA1%20Bargraphs%201.3%20Max.png). 

Notice these statistics can change for Senior Data engineers and Senior Data Scientists. 

The second conclusion can the be summarized in two fold. First, Seniority has advantages in terms of salary. Second of all , that salaries for data analysts are averaging regardless the country, about 110K USD/year. This is an important conclusion, as we see that there is not such a big difference of salary respect to the job title.










Basic statistics of salary by IT role are presented in [LDESC03](/out/LDESC03.log). The table is organized ascending according to the statistic values. For instance, means and medians are increasing in magnitude. The conclusion is then that the Jobs at the bottom are better paid. Business analyst jobs offer a mean of 80K whereas a Machine Learning Engineer may be paid 120K in average [EDA1 Scaterplots 4.0](/plot/EDA1%20Scaterpots%204.0.png) shows a plot of the mean yearly salary respect to the 'n' number of job vacancies by job category. 

I want to talk a bit about this scaterplot. It is very interesting, open it in a big forma, as the trends can be subtile and hidden in colors or scattered in the plot. Let us see. The vertical axis represents the counts of available vacancies by job ('n'), and the x axis indicates the yearly salary axis going from 46K up to about 250K. The size of the bubbles indicate the size of the salary. The bigger the salary, the bigger the bubble. Colors represent the types of Jobs. For instance, Data Analysts are in green color. Notice how Data analysts (green) are diametrally oposed to the Data engineers (black) and Data Scientists (dark red). This is an interesting insight. It looks like Data analyst are highly required as well as Data engineers, but Data Analysts are paid less good.


Notice all graphs have a dataset you can access to check particular values. This graph was derived from the [EDA1_Heatmap_3.0.1](/data/EDA1_Heatmap_3.0.1.csv). The data is available in the out folder [LDESC03](/out/LDESC03.log). This is the Listing of Salary statistics by IT Job. Data Engineers, Machine Learning Engineers and Senior professionals have salaries with means around 120K. This can serve as a conclusion for this chapter. 


In any case, We will see that Job titles are arbitrary as requested skills vary not only accross country, but also within the Job titles themselves. We will see that a Data Analyst in Belgium is not the same Data Analyst elsewhere. 




## Analysis by country

Most of analysis will be made by country. As it was already said something about the total jobs available by country, check again [TDESC02](/out/TDESC02.log) to check the counts of jobs available and [TDESC02](/out/TDESC02.log) to see any of the statistics. 

TDESC02 Shows the most important countries (Germany, France, Poland, Spain and Portugal) that acount for about the 60% of the total data. the same can be said about Data Analyst, Data Engineer, Data Scientist and Machine learning Jobs, that account roughly for the 75% of the total data. 

This table is very important as it shows the representativeness of each country in the overall estimations. 

Since the estimates of means among others are now being calculated by job type and by country, we might en up in confusion. Let'us have an overall sense by plotting a bit. 

For now let us say that countries pay very differently. One example can be Germany compared to Italy in terms of yearly salary. In this respect [EDA1 Scaterplots 2.0.3](/plot/EDA1%20Scaterpots%202.0.3.png) shows both countries one next to the other. Italy pays less to data analysts in general and the job availability is scarce. The plot presents in color the country salary against the overall mean. Yellow tones are more desired as it means that the country pays higher than the average. This is the case for Germany for instance, This is not the case fo Italy. A plot with all countries can be seeing at [EDA 1 Scatterplots 2.0.2](/plot/EDA1%20Scaterpots%202.0.2.png). Germany, France, Poland, Portugal and Spain pay better in general.

The complete summary is presented in [TDESC02](/out/TDESC02.log)  and data is available in the data folder see [EDA1_Bargraphs_3.2](/data/EDA1_Bargraphs_3.2.csv). This data file can be opened in excel. It is a comma separated file. Once opened in excel, filtering is possible. this way more insights can be derived. 

An important conclusion from this data is that countries like Spain and Portugal, once laggards and economically in shock, now show signs of economic recovery, at least for data analysts in general.

To make a more deep analysis about salary by countries and types of IT Jobs, use the [TDESC04](/out/LDESC04.log) output as this table has a complette overview by country and by Job type. Units are in '000 to fit in the canvas. The data of this table is also available in a CSV file here [TDESC04.csv](/data/TDESC04.csv). Drawing here a high level conclusion excluding Machine Learning Jobs, Software Engieneers and Senior Job positions that are very well paid, we have: Data Engineers (DEE) and Data scientists (DSC) that follow in the ranking. Most of job oportunities in 2023 came from Germany (DEE 150K, DSC 130K), Poland (DEE 140K, DSC140K) and Portugal (DEE 130K, DSC 160K). Data Analysts are the lowest paid with an average easily around 90K accross countries. Italy pays around 50K/year to these professionals.

A quick overview of the TDESC04 can be done by looking at the [EDA1 Scaterplot 4.0.1 ](/plot/EDA1%20Scaterpots%204.0.1.png), as it displays data by country and by IT Job oportunity. 'n' represents the total of jobs available within the country. Notice that the number of jobs available are the biggest in France, Germany, Poland, Portugal and Spain. These are casually the countries where DEEs and DSCs are better paid. In all of them  Data Analysts are less paid compared to any other professional. Data scientists (DSC) are in diametral oposition to Data Analysts as they receive higher salaries in average. Table [TDESC04.csv](/data/TDESC04.csv) contains all specific data. Additional Plot [here](/plot/EDA1%20Scaterpots%204.0.1.png), or [here](/plot/EDA1%20Scaterpots%204.0.2.png)

The most requested professional is the Data Engineer across all countries. These professionals are very well paid, with salaries reaching easily 130K/year in average.
Should you then become a Data engineer? think twice, not so easy. we will see why once we check the skills required. these professionals are in high demand, because of their skills. 



## Analysis by Skills

Let us recap a bit about the first conclusions reached hereup. Germany (17%), France (16%), Poland (13%), Spain (10%) accounted for about 60% of the total vacancies in Europe. In terms of Jobs, Data Analyst (23%), Data Engineer (22%) and Data Scientist (18%) accounted for roughly the 60% of the total vacancies. It was said that the average salary for IT professionals here analyzes was about 110K/year with an overall Minium salary of 46K and max of 190K. It was said that Data analyst are highly required as well as Data engineers, but Data Analysts are paid less good.

A high level conclusion excluding Machine Learning Jobs, Software Engieneers and Senior Job positions that are very well paid, we said thant Data Engineers (DEE) and Data scientists (DSC) that follow in the ranking. Most of job oportunities in 2023 came from Germany (DEE 150K, DSC 130K), Poland (DEE 140K, DSC140K) and Portugal (DEE 130K, DSC 160K). Data Analysts are the lowest paid with an average easily around 90K accross countries. Italy paid around 50K/year to these professionals.Data scientists (DSC) were in diametral oposition to Data Analysts as they received higher salaries in average in 2023.

Skills may or may not be related with a particular Job. Let us assume there is no relationship between type of IT data job and the skill required. This is safe as the counts for jobs available in Belgium are notoriously higher for Business Analysts than for other IT professionals. This may be explained because in Belgium it is expected that the Data Analyst knows more about different IT topics than for instance the same Data analyst in Germany. Let's take a look at Belgium alone [EDA 1 Scaterplots 3.0.1](/plot/EDA1%20Scaterpots%203.0.1.png) shows the skills required for a Business Analyst (in blue) in Belgium. The set of skills overlap quite often with those from a Data Scientists (black). What is interesting is that Business Analysts are notoriously lower paid than those Data Scientists. Further research that is not done here would answer the question about the industries that employ those professionals. 

The conclusion here is that Job titles are a set of skills that do not match across countries in Europe. This idea is clearer in [EDA 1 Scaterplots 3.0.4](/plot/EDA1%20Scaterpots%203.0.4.png). Notice that a Data Engineer in Sweden looks more like a Data Scientist in  Germany, and, in France, a Data Engineer must know a lot more than any other country. 'n' represents the amount of jobs available, it represents the size of the bubbles. Big bubbles are therefore more reliable data. 

To conclude, the []  Data Engineers are expected to know a lot more than Data Scientists, and jet, they are paid in average the same. If you want to be very well paid, then become a Data Engineer. If you want to be challenged in your job then become a Data Engineer in Belgium of France. If you want to have a high salary while having a less challenging job then becomming a Data Scientist might be of interest for you. [EDA1 Scaterplots 3.0.5](/plot/EDA1%20Scaterpots%203.0.5.png) Shows salaries averages in the x-axis (in red) bubbles closer to the right indicates higher paid jobs. Notice that Data scientists (red) earn in average more than Data Engineers and they are required mostly Python, SQL and Tableau. Data Engineers require more than 30 skills in contrast. 

### The boomer of the Data Analyst

Another interesting trend to close this chapter is interchangability of a Data Analyst and a Data Scientist in the workplace. To explore this trend only data was taken with counts within categories higher than 15 records see [EDA1 Scaterplots 3.0.13](/plot/EDA1%20Scaterpots%203.0.13.png). this was done to have a higher view of the data for Data Analysts and Data Scientists. Consider this like a sum out the data. By doing this the skill set was reduced to  Excel, Python SQL and Tableau. These 2 IT Job categories clustered nicely in these skills set. Thus, as Data Analyst, better to change the CV to one of Data Scientist, which is more or less the same and it is better paid. Recruiters will prefer posting that job as a Data Analyst job in ordr to save between 30K-40K a year (see [LDESC03](/out/LDESC03.log)).


## Analysis by Skills in a selected subset

Moving forward. The analysis of salary according type of skill was done without taking into account the type of IT job reported. By doing this clusters of skills can be found  for big earners. With this purpose in mind, tables [LDESC05 - LDESC07](/out/) were made, and based on this table a subset of skills was composed ([LDESC08](/out/LDESC08.log) is the shortest). These skills are the highest paid. Lets take a look at the [LDESC07](/out/LDESC07.log). This table presents the Skill ranking respect to salary categories as follows. Yearly salary from 60K - 90K  is grouped in one category (T6_9). This is done up to 240K-270K (T24_27), which is the last salary range. Further, skills data is separated in these categories and counted by category. For example the AWS category in the first row. AWS represents the job vacancies that IT professionals must know if they want to be in the highes tier of payment. in the range of a yearly salary between 60K-90K there is not a single job offering, meaning that these professionals may command a better payment. There were 43 vacancies for professionals where AWS was required for a gross salary of 120.000 - 150.000 USD among the 15 countries here analyzed. 

Based on this table, the most popular skills in job availability in the IT data analysis sector are AWS, Spark, Airflow, Snowflake and so forth. The table is arranged descending following the T12_T15 salary category which is the most important category that convines data availability with strong yearly salary. 

### Skills and Jobs
A subset was necesary as there are many skills available, see the [EDA1 Heatmap 2.0.1](/plot/EDA1%20Heatmap%202.0.1.png) in this respect. It is difficult to conclude anything from this plot. Any other plots were rendered for this reason [EDA1 Heatmap 2.0.2](/plot/EDA1%20Heatmap%202.0.2.png) Shows how most of vacancies focus on AWS, Python, Snowflake, Spark, SQL and Tableau. 

[EDA2 Heatmap 2.0.1](/plot/EDA1%20Heatmap%202.0.1.png) was made with the data subset including only the skills that were more relevant for salaries in the upper half. It shows how the skills and top jobs relate. The blue color indicates the average salary for that particular Job and skill. Interpreting for instance the Business analyst Job. It can be seeing that a lot of different skills are asked for this role, but there is none that remains constant accross the job descriptions. Redshift and AWS are skills that are better paid for this role. 

The top row is for Software engineer. Notice that this is very open category with very different skills requirement. Notice that Cloud Engineer is a very exclusive type of IT professional. Most of job descriptions reauest Databricks; Looker and Snowflake mainly. The cheapest category looks to be that of data analyst. different skills required but none well paid. 

To wrap up, There is this plot [EDA2 Scaterplots 5.0](/plot/EDA2%20Scaterpots%205.0.png) that can be seing along with the dataset [EDA2 Scaterplots 5.0](/data/EDA2_Scaterplots_5.0.csv). It presents the highest paid skills by different countries. a letter is assigned to each skill and letters are plot over the country canvas. In the data it can be seeing that Tensorflow (A), Bigquery (B), Git (C) and so forth are plotted onto the plot canvas. AWS (X) was one of these skills that paid well and appeared in many vacancies. If 'X' is followed accross the countries it can be seeing that It lays normally in the upper level. Despite this graph is interesting to see the distribution of skills across salary values, it is not interesting to define skill clusters by job type. 

The most important dataset in this research is the [LDESC08](/data/LDESC08.csv). As it presents the job availability count by IT Job. The variable country is not included. The reason is that otherwise the data becomes too detailed, besides, in general it can be said that there are skills that are highly paid regardless the country. The amount of data is not big enough to go in this detail. [LDESC08](/out/LDESC08.log) is the output comming from the [LDESC08](/data/LDESC08.csv) data. The same logic applies here as [LDESC07](/out/LDESC07.log). Columns represent the same categories, but additionally, the Job type is added. All records are ordered by the count of jobs available by category. The most important column is that one for T15_18 or in the category of 150K-180K USD/year. Best paid job is that of Data Engineer, then it is Data Scientist. Third is Machine Lerning Engineer. 

## Conclusion

Summarizing the mean salary for an IT Job was  110K in 2023. With an overall Minium salary of 46K and max of 190K.

Germany (17%), France (16%), Poland (13%), Spain (10%) accounted for about 60% of the total vacancies in Europe. In terms of Jobs, Data Analyst (23%), Data Engineer (22%) and Data Scientist (18%) accounted for roughly the 60% of the total vacancies. There is undoubtelly a country effect but not the one we would expect. Portugal is among the high payers and Italy is the worst. A Data Analyst is paid around 50K/year.

In the IT Jobs market Training is very relevant for a high salary. One skill alone might not move a needdle as the title itself. Professionals that profiled themselves as Data Engineers were highly regarded because they were expected to dominate many skills (about 40). Their Salaries ranged from 90K-180K. Data Engineers (DEE) and Data scientists (DSC) are highly rewarded. Notice that a Data Engineer may be hired just by a subset of its skills, but research on this aspect goes beyond our purpose here.

Most of job oportunities in 2023 came from Germany (DEE 150K, DSC 130K), Poland (DEE 140K, DSC140K) and Portugal (DEE 130K, DSC 160K). Being a senior has just advantages as the skill set required is smaller and the pay is higher, but there were no many vacancies for Senior Data Analysts or Senior Data Engineers. Business Analysts (82K) and Data analyst(90K) are highly required as well. They are not required to dominate particular skills like other IT professionals, but it comes with a lower wage. Data Analyst and Business Analyst job descriptions involve such a very wide group of disparate skills that at the end, they do not look like to be specialized. 

Conclusion of the conclusion. Are you recruiter looking for an IT professional? go to Italy to hunt for Data Analysts. Are you looking for a IT job but you do not have the hot title experience? profile yourselve as a Data Scientist and go to Portugal or Poland.   


[Testing](out/LDESC02.txt)


## Further Analysis

  There was not evidence of specialization in jobs like Data Analyst or Business Analyst. These jobs are paid less maybe because of the overall perception of lack of specialization. I do believe that many Business Analyst professionals are specialized, but in reality, those may need to rebrand themselves if higher salary is what they want. This is a coplex topic that might prove to be interesting in further research. I suppose recruiters in traditional companies are looking for Data Analysts, Banks and Finance for Business Analysts and IT companies for Data Scientists. In reality I can dare to say that job content may be very similar, but this is tought for further digging.

  There is not a clear distinction about skills respect to Job title. This may offer oportunities to the new job applicant. Nevertheless, further research need to be done to identify the 'Job Title' a particular sector is acostummed to. Business Analyst is a very poorly paid generic title, but heavily used in Banks and insurances. It might be interesting to explore the reception of newcomer 'Data Engineers' or 'Data Scientists' by hiring departments after aplicants rebrand themselves and ask for higher payement. 









