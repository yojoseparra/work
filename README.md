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

All documents hereunder can be directly accessed in this folders. Notice that I preffer having a look at data in the .CSVs or Word format, this this reason I added these documents here.

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

Origin of the data comes from datanerd.tech[datanerd.tech](https://datanerd.tech/), and it is available online [data](https://huggingface.co/datasets/lukebarousse/data_jobs). Datanerd app is an application that searches jobs posting dayly comming from google search results.

## Data Imputation and missing data

I do not impute data, thus I'm assumming here missing at random. The dataset for europe is not that big and it has missing data. This can be missing not at random, as companies that require data analysts and pay lower than average might not publish any salary offer. The result might be that the means and medians calculated here are biased upwards, or in other words, that salary means and medians might look higher than in reality.

Scarce data from Europe makes plots unreliable. You will se very often 'n' in outputs, as we account for the amount of data by category to draw reasonable conclusions. There are outliers that can shift statistics as well. No outliers were removed as it is not clear that these are real outliers or just simple real data. 

### Variables

The most important variables are 'Country', 'Job', 'Skills' and 'Salary'. Salary is a numeric variable of yearly salary represented in USD, and can be given in any outputs as a 'mean', 'median', 'std', 'qrt' ... etc. It indicates the statistic of salary for a particular category.

Salary of 100 K is the same as 100.000 USD. Notice that the notation of thousands is '.' instead of european ',' thousands symbol is represented by a point instead of a comma.

## Exploratory Data Analysis

In total we have 1488 not missing records. The following table presents the results after using Postgres SQL to query basic statistics in '000s:

*Table 1. Descriptive statistics by Job type for a total of 1488 no missing records*

| job                       | n   | mean  | stddev | min  | max   |
|---------------------------|-----|-------|--------|------|-------|
| Software Engineer         | 73  | $105  | $47    | $44  | $211  |
| Cloud Engineer            | 19  | $107  | $50    | $58  | $228  |
| Senior Data Analyst       | 68  | $109  | $24    | $51  | $200  |
| Data Scientist            | 262 | $115  | $41    | $44  | $198  |
| Machine Learning Engineer | 167 | $119  | $47    | $44  | $232  |
| Data Engineer             | 325 | $121  | $35    | $46  | $256  |
| Senior Data Engineer      | 94  | $131  | $33    | $46  | $182  |
| Senior Data Scientist     | 87  | $138  | $41    | $46  | $231  |
| Business Analyst          | 50  | $86   | $30    | $31  | $191  |
| Data Analyst              | 343 | $95   | $35    | $44  | $206  |

Table 1. Shows the distribution of salaries accross different jobs in a decreasing manner from highly paid to lower paid. Data analysts are the lowest paid among the group. the total Job count is important as job categories with less counts may be less representative. 


### EU IT Job posts (N=1488 job vacancies in 2023).


To focus this analysis on the EU job market, I apply filters to the dataset, narrowing down to roles based in the Eurozone. Only 15 countries had enough data up to a total of 1488 usable posts with salary information. Table [TDESC02](/out/TDESC02.log) shows the distribution of job vacancies for different jobs and by country.

*Table TDESC02. Total counts of job availabilities by country in 2023 in '000s*
|Row   |Country     |Data Analyst |Data Engineer |Data Scientist |Machine Learning Engineer |Senior Data Engineer |Senior Data Scientist |Software Engineer |Senior Data Analyst |Business Analyst |Cloud Engineer |Total       |
|:--|:-----------|:------------|:-------------|:--------------|:-------------------------|:--------------------|:---------------------|:-----------------|:-------------------|:----------------|:--------------|:-----------|
|5  |Germany     |48( 19% )    |39( 15% )     |41( 16% )      |39( 15% )                 |26( 10% )            |21( 8% )              |10( 4% )          |15( 6% )            |11( 4% )         |7( 3% )        |257 (17%)   |
|4  |France      |50( 21% )    |62( 26% )     |57( 24% )      |17( 7% )                  |15( 6% )             |9( 4% )               |11( 5% )          |12( 5% )            |3( 1% )          |1( 0.4% )      |237 (16%)   |
|11 |Poland      |43( 22% )    |46( 23% )     |29( 14% )      |23( 12% )                 |9( 4% )              |12( 6% )              |15( 8% )          |9( 4% )             |8( 4% )          |6( 3% )        |200 (13%)   |
|14 |Spain       |30( 21% )    |35( 24% )     |20( 14% )      |16( 11% )                 |11( 8% )             |7( 5% )               |8( 6% )           |9( 6% )             |5( 3% )          |3( 2% )        |144 (10%)   |
|12 |Portugal    |37( 28% )    |30( 23% )     |22( 17% )      |14( 11% )                 |5( 4% )              |11( 8% )              |5( 4% )           |4( 3% )             |3( 2% )          |0( 0% )        |131 (9%)    |
|10 |Netherlands |20( 23% )    |23( 26% )     |17( 20% )      |12( 14% )                 |5( 6% )              |3( 3% )               |3( 3% )           |1( 1% )             |3( 3% )          |0( 0% )        |87 (6%)     |
|6  |Greece      |16( 20% )    |24( 29% )     |12( 15% )      |14( 17% )                 |1( 1% )              |6( 7% )               |6( 7% )           |0( 0% )             |3( 4% )          |0( 0% )        |82 (6%)     |
|7  |Hungary     |18( 29% )    |13( 21% )     |13( 21% )      |5( 8% )                   |3( 5% )              |3( 5% )               |4( 6% )           |2( 3% )             |0( 0% )          |1( 2% )        |62 (4%)     |
|1  |Belgium     |20( 35% )    |11( 19% )     |8( 14% )       |7( 12% )                  |1( 2% )              |3( 5% )               |2( 4% )           |0( 0% )             |5( 9% )          |0( 0% )        |57 (4%)     |
|8  |Ireland     |19( 36% )    |9( 17% )      |6( 11% )       |5( 9% )                   |6( 11% )             |4( 8% )               |1( 2% )           |3( 6% )             |0( 0% )          |0( 0% )        |53 (4%)     |
|9  |Italy       |11( 23% )    |12( 26% )     |12( 26% )      |3( 6% )                   |0( 0% )              |3( 6% )               |2( 4% )           |3( 6% )             |1( 2% )          |0( 0% )        |47 (3%)     |
|15 |Sweden      |9( 19% )     |8( 17% )      |7( 15% )       |3( 6% )                   |6( 13% )             |3( 6% )               |1( 2% )           |3( 6% )             |7( 15% )         |0( 0% )        |47 (3%)     |
|13 |Romania     |12( 30% )    |6( 15% )      |7( 18% )       |3( 8% )                   |2( 5% )              |0( 0% )               |4( 10% )          |4( 10% )            |1( 2% )          |1( 2% )        |40 (3%)     |
|3  |Finland     |5( 19% )     |5( 19% )      |4( 15% )       |4( 15% )                  |2( 8% )              |2( 8% )               |1( 4% )           |3( 12% )            |0( 0% )          |0( 0% )        |26 (2%)     |
|2  |Denmark     |5( 28% )     |2( 11% )      |7( 39% )       |2( 11% )                  |2( 11% )             |0( 0% )               |0( 0% )           |0( 0% )             |0( 0% )          |0( 0% )        |18 (1%)     |
|16 |Total       |343 (23%)    |325 (22%)     |262 (18%)      |167 (11%)                 |94 (6%)              |87 (6%)               |73 (5%)           |68 (5%)             |50 (3%)          |19 (1%)        |1488 (100%) |


This table can be accessed in word, CSV or Word format. TDESC02 is organized from left to right to show the most important countries and roles in terms of counts of job vacancies. Thus, for instance Germany accounted for about the 17% of total vacancies in europe. Other important countries were France (16%), Poland (13%), Spain (10%). The table is also organize by important Jobs, as it starts from Data Analyst (23%), Data Engineer (22%) and Data Scientist (18%) down to Cloud Engineeer (1%). 


## A 1.000 m high view  

The *first conclussion* can be that the most important jobs are Data Analyst,	Data Engineer,	Data Scientist in terms of jobs available as they acount roughly for the 60% of jobs available.

But before we enter into further detail, lets take a look at overall means. I did not want to give a number at this stage, but just derive those numbers directly from a simple unlabeled plot. [Min](/plot/EDA1%20Bargraphs%201.0%20MIN.png).

This first plot is the result of calculating the Minimum salary by job type regardless the country. We will see that salary offers accross countries may differ, but this is the first approach to have a rough estimate of an overall descriptive statistic. This estimate might not be precise but might be unbiased respect to the one calculated from the data. Let me explain you what I mean by that:

the plot of the 'Min' shows that an horizontal line can be safely done on top of the bars and that an overall average can be 46K dollars (46.000 USD).

Following the same logic it can be said that for other statistics we have the median of 110K, mean of  110K and max of 190K. This can be seeing in [Median](plot/EDA1%20Bargraphs%201.1%20Median.png), [Max](plot/EDA1%20Bargraphs%201.3%20Max.png). 

*Figure 1. Median of Jobs by Country*
![Median](/plot/EDA1%20Bargraphs%203.2%20MEDIAN.png)



Notice these statistics can change for Senior Data engineers and Senior Data Scientists. 

The second conclusion can the be summarized in two fold. First, Seniority has advantages in terms of salary. Second of all , that salaries for data analysts are averaging regardless the country, about 110K USD/year. This is an important conclusion, as we see that there is not such a big difference of salary respect to the job title.


Basic statistics of salary by IT role are presented in [LDESC03](/out/LDESC03.log). The table is organized ascending according to the statistic values. For instance, means and medians are increasing in magnitude. The conclusion is then that the Jobs at the bottom are better paid. Business analyst jobs offer a mean of 80K whereas a Machine Learning Engineer may be paid 120K in average [EDA1 Scaterplots 4.0](/plot/EDA1%20Scaterpots%204.0.png) shows a plot of the mean yearly salary respect to the 'n' number of job vacancies by job category. 

I want to talk a bit about this scaterplot. It is very interesting, open it in a big forma, as the trends can be subtile and hidden in colors or scattered in the plot. Let us see. The vertical axis represents the counts of available vacancies by job ('n'), and the x axis indicates the yearly salary axis going from 46K up to about 250K. The size of the bubbles indicate the size of the salary. The bigger the salary, the bigger the bubble. Colors represent the types of Jobs. For instance, Data Analysts are in green color. Notice how Data analysts (green) are diametrally oposed to the Data engineers (black) and Data Scientists (dark red). This is an interesting insight. It looks like Data analyst are highly required as well as Data engineers, but Data Analysts are paid less good.


Notice all graphs have a dataset you can access to check particular values. This graph was derived from the [EDA1_Heatmap_3.0.1](/data/EDA1_Heatmap_3.0.1.csv). The data is available in the out folder [LDESC03](/out/LDESC03.log). This is the Listing of Salary statistics by IT Job. Data Engineers, Machine Learning Engineers and Senior professionals have salaries with means around 120K. This can serve as a conclusion for this chapter. 


In any case, We will see that Job titles are arbitrary as requested skills vary not only accross country, but also within the Job titles themselves. We will see that a Data Analyst in Belgium is not the same Data Analyst elsewhere. 




## Analysis by country

Most of analysis will be made by country. As it was already said something about the total jobs available by country, check again [TDESC02](/out/TDESC02.log) to check the counts of jobs available and [TDESC02](/out/TDESC02.log) to see any of the statistics. Hereunder a quick summary.

  *Table 2. Descriptive statistics by country*
| country     | n   | mean  | stddev | min  | max   |
|-------------|-----|-------|--------|------|-------|
| Greece      | 82  | $105  | $38    | $46  | $206  |
| Romania     | 40  | $105  | $45    | $44  | $200  |
| Hungary     | 62  | $107  | $39    | $51  | $191  |
| France      | 237 | $108  | $41    | $44  | $256  |
| Poland      | 200 | $110  | $39    | $44  | $228  |
| Spain       | 144 | $111  | $40    | $44  | $232  |
| Denmark     | 18  | $114  | $36    | $58  | $171  |
| Finland     | 26  | $115  | $33    | $74  | $191  |
| Germany     | 257 | $119  | $45    | $31  | $231  |
| Netherlands | 87  | $119  | $38    | $55  | $232  |
| Portugal    | 131 | $120  | $38    | $53  | $195  |
| Sweden      | 47  | $124  | $42    | $44  | $256  |
| Ireland     | 53  | $125  | $40    | $44  | $200  |
| Italy       | 47  | $96   | $31    | $44  | $162  |
| Belgium     | 57  | $99   | $37    | $46  | $170  |

Table 2. Presents descriptive statistics by country. Italy pays among the lowest with a mean of about 100.000 USD/year.  Among the highest country average payers are Ireland, Germany and Portugal. In the same fashion, TDESC02 Shows the most important countries (Germany, France, Poland, Spain and Portugal) that acount for about the 60% of the total data. the same can be said about Data Analyst, Data Engineer, Data Scientist and Machine learning Jobs, that account roughly for the 75% of the total data. TDESC02 shows the representativeness of each country in the overall estimations. 

Since the estimates of means among others are now being calculated by job type and by country, we might en up in confusion. Let'us have an overall sense by plotting a bit. 

For now let us say that countries pay very differently. One example can be Germany compared to Italy in terms of yearly salary. In this respect [EDA1 Scaterplots 2.0.3](/plot/EDA1%20Scaterpots%202.0.3.png) shows both countries one next to the other. Italy pays less to data analysts in general and the job availability is scarce. The plot presents in color the country salary against the overall mean. Yellow tones are more desired as it means that the country pays higher than the average. This is the case for Germany for instance, This is not the case fo Italy. A plot with all countries can be seeing at [EDA 1 Scatterplots 2.0.2](/plot/EDA1%20Scaterpots%202.0.2.png). Germany, France, Poland, Portugal and Spain pay better in general.

*Figure 2.EDA1 Scatterplots 2.0.2 sample selected countries. X-axis in USD/year*

![EDA1 Scaterpots 2.0.2 sample](/plot/EDA1%20Scaterpots%202.0.2%20sample.PNG)

The complete summary is presented in [TDESC02](/out/TDESC02.log)  and data is available in the data folder see [EDA1_Bargraphs_3.2](/data/EDA1_Bargraphs_3.2.csv). This data file can be opened in excel. It is a comma separated file. Once opened in excel, filtering is possible. this way more insights can be derived. 

An important conclusion from this data is that countries like Spain and Portugal, once laggards and economically in shock, now show signs of economic recovery, at least for data analysts in general.

To make a more deep analysis about salary by countries and types of IT Jobs, use the [TDESC04](/out/LDESC04.log) output as this table has a complette overview by country and by Job type. Units are in '000 to fit in the canvas. The data of this table is also available in a CSV file here [TDESC04.csv](/data/TDESC04.csv). Drawing here a high level conclusion excluding Machine Learning Jobs, Software Engieneers and Senior Job positions that are very well paid, we have: Data Engineers (DEE) and Data scientists (DSC) that follow in the ranking. Most of job oportunities in 2023 came from Germany (DEE 150K, DSC 130K), Poland (DEE 140K, DSC140K) and Portugal (DEE 130K, DSC 160K). Data Analysts are the lowest paid with an average easily around 90K accross countries. Italy pays around 50K/year to these professionals.


*Table 3. TDESC04 output of the descriptive statistics by country and Job. Units in '000s*

|Country     |Parameter    |Business Analyst |Cloud Engineer |Data Analyst |Data Engineer |Data Scientist |Machine Learning Engineer |Senior Data Analyst |Senior Data Engineer |Senior Data Scientist |Software Engineer |
|:-----------|:------------|:----------------|:--------------|:------------|:-------------|:--------------|:-------------------------|:-------------------|:--------------------|:---------------------|:-----------------|
|Belgium     |Mean (SD)    |85 (9)           |NA             |99 (46)      |110 (30)      |122 (43)       |86 (11)                   |NA                  |91 (0)               |80 (19)               |60 (20)           |
|Belgium     |Median (IQR) |91 (16)          |NA             |80 (69)      |101 (34)      |127 (71)       |91 (16)                   |NA                  |91 (0)               |91 (16)               |60 (14)           |
|Belgium     |N            |5.0              |               |20.0         |11.0          |8.0            |7.0                       |                    |1.0                  |3.0                   |2.0               |
|Denmark     |Mean (SD)    |NA               |NA             |81 (14)      |125 (36)      |116 (38)       |139 (44)                  |NA                  |151 (0)              |NA                    |NA                |
|Denmark     |Median (IQR) |NA               |NA             |91 (16)      |125 (26)      |112 (43)       |139 (31)                  |NA                  |151 (0)              |NA                    |NA                |
|Denmark     |N            |                 |               |5.0          |2.0           |7.0            |2.0                       |                    |2.0                  |                      |                  |
|Finland     |Mean (SD)    |NA               |NA             |111 (40)     |96 (4)        |120 (32)       |149 (43)                  |110 (6)             |103 (6)              |126 (50)              |77 (0)            |
|Finland     |Median (IQR) |NA               |NA             |108 (53)     |99 (7)        |118 (28)       |158 (44)                  |114 (5)             |103 (4)              |126 (35)              |77 (0)            |
|Finland     |N            |                 |               |5.0          |5.0           |4.0            |4.0                       |3.0                 |2.0                  |2.0                   |1.0               |
|France      |Mean (SD)    |83 (35)          |109 (0)        |84 (34)      |119 (34)      |102 (41)       |93 (37)                   |107 (25)            |139 (25)             |146 (31)              |131 (62)          |
|France      |Median (IQR) |91 (35)          |109 (0)        |71 (59)      |101 (52)      |90 (72)        |83 (49)                   |114 (22)            |151 (0)              |162 (0)               |146 (105)         |
|France      |N            |3.0              |1.0            |50.0         |62.0          |57.0           |17.0                      |12.0                |15.0                 |9.0                   |11.0              |
|Germany     |Mean (SD)    |81 (27)          |123 (56)       |104 (41)     |134 (40)      |120 (47)       |117 (53)                  |102 (19)            |131 (30)             |153 (34)              |93 (44)           |
|Germany     |Median (IQR) |91 (30)          |91 (57)        |106 (38)     |151 (51)      |135 (90)       |91 (81)                   |114 (27)            |151 (60)             |162 (10)              |87 (33)           |
|Germany     |N            |11.0             |7.0            |48.0         |39.0          |41.0           |39.0                      |15.0                |26.0                 |21.0                  |10.0              |
|Greece      |Mean (SD)    |68 (5)           |NA             |115 (41)     |100 (33)      |100 (31)       |119 (37)                  |NA                  |46 (0)               |117 (54)              |93 (39)           |
|Greece      |Median (IQR) |64 (5)           |NA             |102 (51)     |99 (31)       |92 (19)        |104 (63)                  |NA                  |46 (0)               |91 (66)               |83 (48)           |
|Greece      |N            |3.0              |               |16.0         |24.0          |12.0           |14.0                      |                    |1.0                  |6.0                   |6.0               |
|Hungary     |Mean (SD)    |NA               |91 (0)         |90 (32)      |136 (21)      |100 (38)       |112 (63)                  |90 (2)              |151 (0)              |115 (40)              |73 (17)           |
|Hungary     |Median (IQR) |NA               |91 (0)         |83 (44)      |151 (14)      |91 (36)        |83 (112)                  |90 (1)              |151 (0)              |91 (35)               |70 (27)           |
|Hungary     |N            |                 |1.0            |18.0         |13.0          |13.0           |5.0                       |2.0                 |3.0                  |3.0                   |4.0               |
|Ireland     |Mean (SD)    |NA               |NA             |106 (40)     |133 (27)      |114 (45)       |139 (44)                  |132 (63)            |143 (25)             |162 (11)              |91 (0)            |
|Ireland     |Median (IQR) |NA               |NA             |101 (31)     |151 (51)      |105 (60)       |171 (61)                  |121 (62)            |151 (0)              |166 (12)              |91 (0)            |
|Ireland     |N            |                 |               |19.0         |9.0           |6.0            |5.0                       |3.0                 |6.0                  |4.0                   |1.0               |
|Italy       |Mean (SD)    |44 (0)           |NA             |76 (27)      |115 (26)      |99 (38)        |91 (16)                   |106 (13)            |NA                   |85 (19)               |96 (16)           |
|Italy       |Median (IQR) |44 (0)           |NA             |54 (51)      |100 (40)      |91 (56)        |91 (16)                   |114 (11)            |NA                   |75 (17)               |96 (11)           |
|Italy       |N            |1.0              |               |11.0         |12.0          |12.0           |3.0                       |3.0                 |                     |3.0                   |2.0               |
|Netherlands |Mean (SD)    |88 (22)          |NA             |101 (34)     |110 (25)      |139 (32)       |130 (54)                  |114 (0)             |141 (28)             |129 (47)              |113 (69)          |
|Netherlands |Median (IQR) |91 (21)          |NA             |96 (38)      |100 (18)      |162 (53)       |126 (89)                  |114 (0)             |151 (0)              |151 (43)              |91 (66)           |
|Netherlands |N            |3.0              |               |20.0         |23.0          |17.0           |12.0                      |1.0                 |5.0                  |3.0                   |3.0               |
|Poland      |Mean (SD)    |90 (30)          |104 (61)       |90 (30)      |121 (41)      |124 (40)       |115 (39)                  |110 (12)            |102 (41)             |136 (33)              |95 (22)           |
|Poland      |Median (IQR) |89 (14)          |86 (15)        |91 (55)      |137 (58)      |135 (70)       |91 (53)                   |114 (0)             |91 (62)              |162 (68)              |91 (0)            |
|Poland      |N            |8.0              |6.0            |43.0         |46.0          |29.0           |23.0                      |9.0                 |9.0                  |12.0                  |15.0              |
|Portugal    |Mean (SD)    |72 (12)          |NA             |96 (31)      |125 (27)      |136 (34)       |145 (46)                  |114 (0)             |122 (45)             |129 (39)              |121 (38)          |
|Portugal    |Median (IQR) |75 (12)          |NA             |91 (39)      |129 (52)      |157 (49)       |171 (82)                  |114 (0)             |151 (60)             |151 (58)              |97 (69)           |
|Portugal    |N            |3.0              |               |37.0         |30.0          |22.0           |14.0                      |4.0                 |5.0                  |11.0                  |5.0               |
|Romania     |Mean (SD)    |83 (0)           |58 (0)         |76 (25)      |106 (36)      |112 (37)       |144 (45)                  |129 (48)            |121 (42)             |NA                    |133 (79)          |
|Romania     |Median (IQR) |83 (0)           |58 (0)         |75 (40)      |100 (29)      |124 (60)       |171 (39)                  |114 (27)            |121 (30)             |NA                    |144 (122)         |
|Romania     |N            |1.0              |1.0            |12.0         |6.0           |7.0            |3.0                       |4.0                 |2.0                  |                      |4.0               |
|Spain       |Mean (SD)    |114 (58)         |93 (35)        |94 (24)      |120 (35)      |96 (33)        |116 (51)                  |110 (8)             |127 (36)             |143 (60)              |106 (58)          |
|Spain       |Median (IQR) |89 (96)          |91 (35)        |94 (31)      |137 (60)      |90 (23)        |104 (72)                  |114 (0)             |151 (60)             |162 (50)              |79 (90)           |
|Spain       |N            |5.0              |3.0            |30.0         |35.0          |20.0           |16.0                      |9.0                 |11.0                 |7.0                   |8.0               |
|Sweden      |Mean (SD)    |85 (25)          |NA             |100 (22)     |136 (58)      |137 (34)       |133 (45)                  |93 (36)             |151 (0)              |175 (22)              |161 (0)           |
|Sweden      |Median (IQR) |91 (14)          |NA             |108 (21)     |137 (53)      |162 (47)       |145 (43)                  |114 (31)            |151 (0)              |175 (22)              |161 (0)           |
|Sweden      |N            |7.0              |               |9.0          |8.0           |7.0            |3.0                       |3.0                 |6.0                  |3.0                   |1.0               |


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

*Figure 3.EDA1 Scatterplots 3.0.13 sample selected countries. X-axis in USD/year. Data Analysts in blue and Data Scientists in red*

![EDA1 Scatterplots 3.0.13](/plot/EDA1%20Scaterpots%203.0.13%20sample.PNG)

## Analysis by Skills in a selected subset

Moving forward. The analysis of salary according type of skill was done without taking into account the type of IT job reported. By doing this clusters of skills can be found  for big earners. With this purpose in mind, tables [LDESC05 - LDESC07](/out/) were made, and based on this table a subset of skills was composed ([LDESC08](/out/LDESC08.log) is the shortest). These skills are the highest paid. Lets take a look at the [LDESC07](/out/LDESC07.log). 

*Table 4. LDESC08 output with selected rows of the original output with descriptive statistics by country and Job. Units in '000s*

|Skills        | T6_9| T9_12| T12_15| T15_18| T18_21| T21_24| T24_27|
|:-------------|----:|-----:|------:|------:|------:|------:|------:|
|aws           |   NA|    41|     43|      7|     NA|     NA|     NA|
|spark         |   NA|    38|     38|      4|     NA|     NA|     NA|
|airflow       |   NA|    17|     36|      2|     NA|     NA|     NA|
|snowflake     |    1|    15|     34|      1|     NA|     NA|     NA|
|python        |   NA|    82|     33|     NA|     NA|     NA|     NA|
|looker        |    1|    18|     29|      1|     NA|     NA|     NA|
|databricks    |    7|    19|     28|     NA|     NA|     NA|     NA|
|sql           |   NA|    83|     26|     NA|     NA|     NA|     NA|
|go            |    8|    31|     26|     NA|     NA|     NA|     NA|
|pandas        |    1|    15|     25|      1|     NA|     NA|     NA|
|azure         |   NA|    64|     24|     NA|     NA|     NA|     NA|
|gcp           |   NA|    25|     23|      6|     NA|     NA|     NA|
|redshift      |    1|    10|     20|      5|     NA|     NA|     NA|
|java          |   NA|    43|     19|      1|     NA|     NA|     NA|
|bigquery      |    2|    15|     19|      1|      1|     NA|     NA|
|kafka         |   12|    12|     18|      7|     NA|     NA|     NA|
|pyspark       |   NA|    10|     18|      2|     NA|     NA|     NA|
|oracle        |   14|    14|     17|      1|     NA|     NA|     NA|
|docker        |    1|    39|     16|      2|     NA|     NA|     NA|
|scala         |   NA|    33|     16|     NA|     NA|     NA|     NA|
|git           |    5|    29|     16|      3|     NA|     NA|     NA|
|pytorch       |   NA|    21|     16|      3|     NA|     NA|     NA|
|tensorflow    |   NA|    17|     15|      5|      1|     NA|     NA|
|kubernetes    |    9|    24|     14|      3|     NA|     NA|     NA|
|numpy         |   NA|    11|     14|      7|     NA|     NA|     NA|
|terraform     |    5|    19|     13|      1|     NA|     NA|     NA|
|postgresql    |    3|     5|     13|      4|     NA|     NA|     NA|
|hadoop        |    4|    20|     12|      5|     NA|     NA|     NA|
|scikit-learn  |    6|     6|     12|      4|     NA|     NA|     NA|
|mysql         |    5|     2|     12|      2|     NA|     NA|     NA|
|tableau       |    4|    54|     11|     NA|     NA|     NA|     NA|
|jira          |    5|    15|     11|      1|     NA|     NA|     NA|
|sql server    |    4|    13|     10|      2|     NA|     NA|     NA|
|gdpr          |    4|    13|     10|      2|     NA|     NA|     NA|
|c++           |   NA|    17|      9|     NA|      1|      1|     NA|
|power bi      |   18|    36|      8|     NA|     NA|     NA|     NA|
|elasticsearch |    4|     6|      8|     NA|     NA|     NA|     NA|
|matlab        |   10|     2|      8|     NA|     NA|     NA|     NA|
|flow          |    4|    19|      7|      2|     NA|     NA|     NA|
|jenkins       |    9|    10|      7|      5|     NA|     NA|     NA|
|matplotlib    |    2|     9|      7|      2|      1|     NA|     NA|
|nosql         |    5|    26|      6|      8|     NA|     NA|     NA|
|jupyter       |    6|     7|      6|      2|     NA|     NA|     NA|
|sap           |   11|    24|      5|     NA|     NA|     NA|     NA|
|github        |    2|    18|      5|      5|      1|     NA|     NA|
|qlik          |    6|    17|      5|     NA|     NA|     NA|     NA|
|c#            |    4|    16|      5|      1|     NA|     NA|     NA|
|mongodb       |    3|    14|      4|     NA|      2|     NA|     NA|
|ssis          |    5|     6|      4|      2|     NA|     NA|     NA|
|confluence    |    5|     2|      4|      2|     NA|     NA|     NA|
|shell         |    8|     2|      4|      1|     NA|     NA|     NA|
|redis         |    2|     1|      4|     NA|     NA|     NA|     NA|
|r             |    2|    57|      3|     NA|     NA|     NA|     NA|
|excel         |   38|    16|      3|     NA|     NA|     NA|     NA|

This table presents the Skill ranking respect to salary categories as follows. Yearly salary from 60K - 90K  is grouped in one category (T6_9). This is done up to 240K-270K (T24_27), which is the last salary range. Further, skills data is separated in these categories and counted by category. For example the AWS category in the first row. AWS represents the job vacancies that IT professionals must know if they want to be in the highes tier of payment. in the range of a yearly salary between 60K-90K there is not a single job offering, meaning that these professionals may command a better payment. There were 43 vacancies for professionals where AWS was required for a gross salary of 120.000 - 150.000 USD among the 15 countries here analyzed. 

Based on this table, the most popular skills in job availability in the IT data analysis sector are AWS, Spark, Airflow, Snowflake and so forth. The table is arranged descending following the T12_T15 salary category which is the most important category that convines data availability with strong yearly salary. 

### Skills and Jobs
A subset was necesary as there are many skills available, see the [EDA1 Heatmap 2.0.1](/plot/EDA1%20Heatmap%202.0.1.png) in this respect. It is difficult to conclude anything from this plot. Any other plots were rendered for this reason [EDA1 Heatmap 2.0.2](/plot/EDA1%20Heatmap%202.0.2.png) Shows how most of vacancies focus on AWS, Python, Snowflake, Spark, SQL and Tableau. 

[EDA2 Heatmap 2.0.1](/plot/EDA1%20Heatmap%202.0.1.png) was made with the data subset including only the skills that were more relevant for salaries in the upper half. It shows how the skills and top jobs relate. The blue color indicates the average salary for that particular Job and skill. Interpreting for instance the Business analyst Job. It can be seeing that a lot of different skills are asked for this role, but there is none that remains constant accross the job descriptions. Redshift and AWS are skills that are better paid for this role. 

The top row is for Software engineer. Notice that this is very open category with very different skills requirement. Notice that Cloud Engineer is a very exclusive type of IT professional. Most of job descriptions reauest Databricks; Looker and Snowflake mainly. The cheapest category looks to be that of data analyst. different skills required but none well paid. 

To wrap up, There is this plot [EDA2 Scaterplots 5.0](/plot/EDA2%20Scaterpots%205.0.png) that can be seing along with the dataset [EDA2 Scaterplots 5.0](/data/EDA2_Scaterplots_5.0.csv). It presents the highest paid skills by different countries. a letter is assigned to each skill and letters are plot over the country canvas. In the data it can be seeing that Tensorflow (A), Bigquery (B), Git (C) and so forth are plotted onto the plot canvas. AWS (X) was one of these skills that paid well and appeared in many vacancies. If 'X' is followed accross the countries it can be seeing that It lays normally in the upper level. Despite this graph is interesting to see the distribution of skills across salary values, it is not interesting to define skill clusters by job type. 

*Table 5. LDESC08 output with selected rows of the original output with descriptive statistics by country and Job. Units in '000s*

|Skills       | T6_9| T9_12| T12_15| T15_18| T18_21| T21_24| T24_27|Job                       |
|:------------|----:|-----:|------:|------:|------:|------:|------:|:-------------------------|
|sql          |    9|    78|     27|     71|      1|     NA|     NA|Data Engineer             |
|python       |    7|    88|     21|     68|      1|      1|      1|Data Engineer             |
|aws          |    3|    55|     21|     39|     NA|     NA|      1|Data Engineer             |
|python       |   26|    34|     21|     58|      7|     NA|     NA|Data Scientist            |
|spark        |    6|    50|     19|     57|     NA|      3|      2|Data Engineer             |
|airflow      |    1|    19|     14|     24|      1|     NA|      1|Data Engineer             |
|sql          |   17|    27|     12|     40|      6|     NA|     NA|Data Scientist            |
|azure        |    5|    46|     11|     26|      1|     NA|      1|Data Engineer             |
|git          |    2|    25|      9|      8|     NA|     NA|     NA|Data Engineer             |
|snowflake    |   NA|     9|      9|     15|     NA|     NA|      1|Data Engineer             |
|bigquery     |   NA|     8|      9|     12|     NA|     NA|     NA|Data Engineer             |
|scala        |    1|    27|      8|     24|     NA|     NA|     NA|Data Engineer             |
|gcp          |    3|    23|      8|     17|     NA|     NA|     NA|Data Engineer             |
|docker       |    2|    23|      8|     12|     NA|     NA|     NA|Data Engineer             |
|kubernetes   |    1|    18|      7|      7|      1|     NA|      1|Data Engineer             |
|pyspark      |   NA|     8|      7|      9|      1|     NA|     NA|Data Engineer             |
|azure        |    6|     5|      7|     14|      1|     NA|     NA|Data Scientist            |
|aws          |    4|     3|      6|     17|      3|     NA|     NA|Data Scientist            |
|sql          |   28|    98|      5|     12|     NA|     NA|     NA|Data Analyst              |
|java         |    3|    35|      5|     31|     NA|     NA|     NA|Data Engineer             |
|hadoop       |    3|    19|      5|     19|     NA|     NA|      1|Data Engineer             |
|tableau      |    6|     8|      5|     18|      2|     NA|     NA|Data Scientist            |
|spark        |    6|     6|      5|     20|      2|     NA|     NA|Data Scientist            |
|pandas       |    6|     1|      5|     12|      1|     NA|     NA|Data Scientist            |
|databricks   |   NA|    24|      4|     10|      1|     NA|     NA|Data Engineer             |
|tableau      |    4|     8|      4|     12|     NA|     NA|     NA|Data Engineer             |
|oracle       |   NA|     8|      4|      7|     NA|     NA|     NA|Data Engineer             |
|go           |    1|     6|      4|      7|     NA|     NA|      1|Data Engineer             |
|scikit-learn |    5|     5|      4|     10|      1|     NA|     NA|Data Scientist            |
|gcp          |    1|     1|      4|      4|      1|     NA|     NA|Data Scientist            |
|python       |   20|    70|      3|     11|     NA|      2|     NA|Data Analyst              |
|kafka        |    3|    25|      3|     27|     NA|     NA|     NA|Data Engineer             |
|looker       |    2|    20|      3|      1|     NA|     NA|     NA|Data Analyst              |
|tableau      |   NA|    18|      3|     NA|     NA|     NA|     NA|Senior Data Analyst       |
|terraform    |    3|    12|      3|     16|     NA|     NA|     NA|Data Engineer             |
|mysql        |   NA|     6|      3|      8|     NA|     NA|     NA|Data Engineer             |
|jira         |   NA|     4|      3|      4|     NA|     NA|     NA|Data Engineer             |
|numpy        |    3|     2|      3|      8|      1|     NA|     NA|Data Scientist            |
|databricks   |    3|     2|      3|      3|      1|     NA|     NA|Data Scientist            |
|docker       |    2|     2|      3|      7|     NA|     NA|     NA|Data Scientist            |
|pandas       |   NA|     2|      3|     NA|     NA|     NA|     NA|Data Engineer             |
|postgresql   |   NA|    11|      2|      8|     NA|     NA|     NA|Data Engineer             |
|python       |    6|    10|      2|      5|     NA|      3|     NA|Software Engineer         |
|redshift     |    1|    10|      2|     10|     NA|     NA|     NA|Data Engineer             |
|go           |   NA|     8|      2|     NA|     NA|     NA|     NA|Senior Data Analyst       |
|tensorflow   |    7|     6|      2|     13|      1|     NA|     NA|Data Scientist            |
|looker       |   NA|     6|      2|      4|     NA|     NA|     NA|Data Engineer             |
|bigquery     |   NA|     6|      2|      2|     NA|     NA|     NA|Data Analyst              |
|pytorch      |    7|     5|      2|     10|      1|     NA|     NA|Data Scientist            |
|git          |    5|     3|      2|      8|      2|     NA|     NA|Data Scientist            |
|hadoop       |    1|     3|      2|     11|      1|     NA|     NA|Data Scientist            |
|tableau      |   15|    55|      1|      3|     NA|     NA|     NA|Data Analyst              |
|python       |   14|    42|      1|     41|     10|      1|      3|Machine Learning Engineer |
|sql          |   NA|    38|      1|      1|     NA|     NA|     NA|Senior Data Analyst       |
|aws          |    8|    20|      1|     18|      2|      1|      2|Machine Learning Engineer |
|python       |   NA|    18|      1|      1|     NA|      1|     NA|Senior Data Analyst       |
|tensorflow   |    7|    16|      1|     16|      6|     NA|     NA|Machine Learning Engineer |
|azure        |    6|    12|      1|      7|      1|     NA|      1|Machine Learning Engineer |
|scikit-learn |    2|    11|      1|      3|      3|     NA|     NA|Machine Learning Engineer |
|python       |    4|    10|      1|     38|      3|     NA|      1|Senior Data Scientist     |
|kubernetes   |    6|    10|      1|     10|      3|     NA|     NA|Machine Learning Engineer |
|sql          |    3|     6|      1|     35|      2|     NA|     NA|Senior Data Scientist     |
|pytorch      |    7|    19|     NA|     14|      5|     NA|     NA|Machine Learning Engineer |
|spark        |    4|    18|     NA|      8|      7|     NA|      1|Machine Learning Engineer |
|spark        |    6|    16|     NA|      5|      1|      3|     NA|Data Analyst              |
|azure        |    5|    16|     NA|     13|      1|     NA|     NA|Data Analyst              |
|looker       |   NA|    16|     NA|     NA|     NA|     NA|     NA|Senior Data Analyst       |
|aws          |   NA|    15|     NA|     31|      1|     NA|     NA|Senior Data Engineer      |
|docker       |    5|    14|     NA|     13|      1|     NA|     NA|Machine Learning Engineer |
|sql          |    9|    12|     NA|      1|      1|     NA|     NA|Business Analyst          |
|python       |    1|    12|     NA|     41|      1|     NA|     NA|Senior Data Engineer      |
|sql          |    2|    10|     NA|     39|     NA|     NA|     NA|Senior Data Engineer      |
|git          |    1|     9|     NA|      5|      1|     NA|     NA|Machine Learning Engineer |
|spark        |   NA|     9|     NA|     26|     NA|     NA|     NA|Senior Data Engineer      |
|airflow      |    2|     9|     NA|      2|     NA|     NA|     NA|Data Analyst              |
|tableau      |    5|     9|     NA|      1|     NA|     NA|     NA|Business Analyst          |
|pandas       |    2|     9|     NA|     NA|     NA|     NA|     NA|Data Analyst              |
|airflow      |    2|     8|     NA|      4|      2|     NA|      1|Machine Learning Engineer |
|git          |    3|     8|     NA|      1|     NA|      1|     NA|Data Analyst              |
|snowflake    |   NA|     8|     NA|     18|     NA|     NA|     NA|Senior Data Engineer      |
|java         |    1|     8|     NA|     10|     NA|     NA|     NA|Senior Data Engineer      |
|kubernetes   |   NA|     8|     NA|      8|     NA|     NA|     NA|Senior Data Engineer      |
|gcp          |    3|     8|     NA|      6|     NA|     NA|     NA|Data Analyst              |
|snowflake    |    2|     8|     NA|      4|     NA|     NA|     NA|Data Analyst              |
|databricks   |    3|     8|     NA|      4|     NA|     NA|     NA|Data Analyst              |
|python       |    2|     7|     NA|     NA|     NA|      1|     NA|Cloud Engineer            |
|python       |    4|     7|     NA|      1|      1|     NA|     NA|Business Analyst          |
|azure        |   NA|     7|     NA|     25|      1|     NA|     NA|Senior Data Engineer      |
|aws          |    4|     7|     NA|      7|      1|     NA|     NA|Data Analyst              |
|terraform    |   NA|     7|     NA|      6|     NA|     NA|     NA|Senior Data Engineer      |
|java         |    4|     6|     NA|      7|      1|     NA|      2|Machine Learning Engineer |
|sql          |    4|     6|     NA|     14|      5|     NA|      1|Machine Learning Engineer |
|kubernetes   |    4|     6|     NA|     NA|     NA|      1|     NA|Software Engineer         |
|kafka        |   NA|     6|     NA|     17|     NA|     NA|     NA|Senior Data Engineer      |
|go           |   NA|     6|     NA|     10|     NA|     NA|     NA|Senior Data Engineer      |
|docker       |   NA|     6|     NA|      8|     NA|     NA|     NA|Senior Data Engineer      |
|pyspark      |    1|     4|     NA|      2|      2|     NA|     NA|Data Scientist            |
|kafka        |   NA|     4|     NA|      4|      2|     NA|     NA|Machine Learning Engineer |
|airflow      |   NA|     4|     NA|     24|     NA|     NA|     NA|Senior Data Engineer      |
|gcp          |   NA|     4|     NA|     14|     NA|     NA|     NA|Senior Data Engineer      |
|databricks   |   NA|     4|     NA|     11|     NA|     NA|     NA|Senior Data Engineer      |
|scala        |   NA|     4|     NA|     10|     NA|     NA|     NA|Senior Data Engineer      |
|azure        |    2|     2|     NA|      7|     NA|     NA|      1|Senior Data Scientist     |
|aws          |    2|     2|     NA|     14|     NA|     NA|      1|Senior Data Scientist     |
|spark        |   NA|     2|     NA|     17|      2|     NA|     NA|Senior Data Scientist     |
|airflow      |    1|     2|     NA|     15|     NA|     NA|     NA|Senior Data Scientist     |
|snowflake    |   NA|     2|     NA|     12|     NA|     NA|     NA|Senior Data Scientist     |
|git          |   NA|     2|     NA|      8|     NA|     NA|     NA|Senior Data Engineer      |
|tableau      |   NA|     2|     NA|      7|     NA|     NA|     NA|Senior Data Engineer      |
|snowflake    |   NA|     1|     NA|      2|      1|     NA|     NA|Machine Learning Engineer |
|redshift     |    1|     1|     NA|      3|      1|     NA|     NA|Data Scientist            |
|pyspark      |   NA|     1|     NA|      2|      1|     NA|     NA|Machine Learning Engineer |
|jira         |    2|     1|     NA|     NA|      1|     NA|     NA|Data Scientist            |
|redshift     |   NA|     1|     NA|     12|     NA|     NA|     NA|Senior Data Engineer      |
|bigquery     |   NA|     1|     NA|     12|     NA|     NA|     NA|Senior Data Engineer      |
|tableau      |    1|     1|     NA|     11|     NA|     NA|     NA|Senior Data Scientist     |
|looker       |   NA|    NA|     NA|     10|     NA|     NA|     NA|Senior Data Scientist     |
|git          |   NA|    NA|     NA|      8|     NA|     NA|     NA|Senior Data Scientist  

The most important dataset in this research is the [LDESC08](/data/LDESC08.csv). As it presents the job availability count by IT Job. The variable country is not included. The reason is that otherwise the data becomes too detailed, besides, in general it can be said that there are skills that are highly paid regardless the country. The amount of data is not big enough to go in this detail. [LDESC08](/out/LDESC08.log) is the output comming from the [LDESC08](/data/LDESC08.csv) data. The same logic applies here as [LDESC07](/out/LDESC07.log). Columns represent the same categories, but additionally, the Job type is added. All records are ordered by the count of jobs available by category. The most important column is that one for T15_18 or in the category of 150K-180K USD/year. Best paid job is that of Data Engineer, then it is Data Scientist. Third is Machine Lerning Engineer. 

## Conclusion

Summarizing the mean salary for an IT Job was  110K in 2023. With an overall Minium salary of 46K and max of 190K.

Germany (17%), France (16%), Poland (13%), Spain (10%) accounted for about 60% of the total vacancies in Europe. In terms of Jobs, Data Analyst (23%), Data Engineer (22%) and Data Scientist (18%) accounted for roughly the 60% of the total vacancies. There is undoubtelly a country effect but not the one we would expect. Portugal is among the high payers and Italy is the worst. A Data Analyst is paid around 50K/year.

In the IT Jobs market Training is very relevant for a high salary. One skill alone might not move a needdle as the title itself. Professionals that profiled themselves as Data Engineers were highly regarded because they were expected to dominate many skills (about 40). Their Salaries ranged from 90K-180K. Data Engineers (DEE) and Data scientists (DSC) are highly rewarded. Notice that a Data Engineer may be hired just by a subset of its skills, but research on this aspect goes beyond our purpose here.

Most of job oportunities in 2023 came from Germany (DEE 150K, DSC 130K), Poland (DEE 140K, DSC140K) and Portugal (DEE 130K, DSC 160K). Being a senior has just advantages as the skill set required is smaller and the pay is higher, but there were no many vacancies for Senior Data Analysts or Senior Data Engineers. Business Analysts (82K) and Data analyst(90K) are highly required as well. They are not required to dominate particular skills like other IT professionals, but it comes with a lower wage. Data Analyst and Business Analyst job descriptions involve such a very wide group of disparate skills that at the end, they do not look like to be specialized. 

Conclusion of the conclusion. Are you recruiter looking for an IT professional? go to Italy to hunt for Data Analysts. Are you looking for a IT job but you do not have the hot title experience? profile yourselve as a Data Scientist and go to Portugal or Poland.   


## Further Analysis

  There was not evidence of specialization in jobs like Data Analyst or Business Analyst. These jobs are paid less maybe because of the overall perception of lack of specialization. I do believe that many Business Analyst professionals are specialized, but in reality, those may need to rebrand themselves if higher salary is what they want. This is a coplex topic that might prove to be interesting in further research. I suppose recruiters in traditional companies are looking for Data Analysts, Banks and Finance for Business Analysts and IT companies for Data Scientists. In reality I can dare to say that job content may be very similar, but this is tought for further digging.

  There is not a clear distinction about skills respect to Job title. This may offer oportunities to the new job applicant. Nevertheless, further research need to be done to identify the 'Job Title' a particular sector is acostummed to. Business Analyst is a very poorly paid generic title, but heavily used in Banks and insurances. It might be interesting to explore the reception of newcomer 'Data Engineers' or 'Data Scientists' by hiring departments after aplicants rebrand themselves and ask for higher payement. 









