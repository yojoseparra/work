# Overview (Please read the complete REPORT in the docs folder) 

Welcome to my analysis of the data job market in 15 european countries with the most IT Job opportunities in data analyst roles in 2023. This project was created to identifythe job trends to better prepare for a job application in the IT sector as data analyst. It delves into the top-paying and in-demand skills to help find optimal job opportunities for data analysts in Europe.

The data sourced from [Luke Barousse](https://github.com/lukebarousse/Python_Data_Analytics_Course/tree/main) which provides a foundation for my analysis, containing detailed information on job titles, salaries, locations, and essential skills. Through a series of Python scripts. Luke teaches python through this dataset. 

Despite my project is based on Luke's data, it differs from his substantially as I'm motivate by other research questions and another slice of the data. I use another type of code and I use another software as well (RStudio + Python). Besides, I am exemplifying here how to find data trends by plotting or tabulating data. I offer here a metodology on how to understand data, not a way of programming or document/plot formatting. Therefore, results might look not properly formatted or graphs might appear unfinished. This is normal as we explore the data, we focus less on the final product and more on finding trends.


# The Questions

Below are the questions I want to answer in my project:

1. What are the skills most in demand and how well are they paid?
2. What set of skills relate to each Job title?
3. How well do jobs and skills pay for Data Analysts in each european country?
4. What are the optimal skills for data analysts to learn? (High Demand AND High Paying) 

# Tools I Used

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

# Data 

Origin of the data is unknown. All we know is that it is available online https://huggingface.co/datasets/lukebarousse/data_jobs

## Data Imputation and missing data

I do not impute data, thus I'm assumming here missing at random. The dataset for europe is not that big and it has missing data. This can be missing not at random, as companies that require data analysts and pay lower than average might not publish any salary offer. The result might be that the means and medians calculated here are biased upwards, in other words, that the means, and medians might look higher than in reality data analysist are earning in average, for instance. 

Scarce data for europe makes plots unreliable. You will se very often 'n' in outputs, as we account for the amount of data by category to draw reasonable conclusions. There are outliers that can shift statistics as well. No outliers were removed as it is not clear that this are real outliers or just simple real data. 

## Variables

The most important variables are 'Country', 'Job', 'Skills' and 'Salary'. Salary is a numeric variable of yearly salary represented in USD, and can be given in any outputs as a 'mean', 'median', 'std', 'qrt' ... etc. It indicates the statistic of salary for a particular category.

Salary of 100 K is the same as 100.000 USD. Notice that the notation of thousands is '.' instead of european ',' thousands symbol is represented by a point instead of comma.

# Exploratory Data Analysis
## Filter EU Jobs (N=1488 job vacancies in 2023)


To focus my analysis on the EU. job market, I apply filters to the dataset, narrowing down to roles based in the Eurozone, but only 15 countries have enough data.

[TDESC02](/out/TDESC02.html)

TDESC02 table shows the total counts of job availabilities by country in 2023. Only these countries are displayed as they were those whose data was available.  

Values are presented in '000s. Table can be accessed in word or HTML format. The table is organized from left to right to show the most important countries and roles in terms of counts of job vacancies. Thus, for instance Germany accounted for about the 17% of total vacancies in europe. Other important countries were France (16%), Poland (13%), Spain (10%). The table is also organize by important Jobs, as it starts from Data Analyst (23%), Data Engineer (22%) and Data Scientist (18%) down to Cloud Engineeer (1%). 


# A 1.000 m high view  
The *first conclussion* can be that the most important jobs are Data Analyst,	Data Engineer,	Data Scientist in terms of jobs available as they acount roughly for the 60% of jobs available.

But before we enter into further detail, lets take a look at overall means. I did not want to give a number at this stage, but just derive those numbers directly from a simple unlabeled plot. 


[Min](/plot/EDA1%20Bargraphs%201.0%20MIN.png)

This first plot is the result of calculating the Minimum salary by job type regardless the country. We will see that salary offers accross countries may differ, but this is the first approach to have a rough estimate of an overall descriptive statistic. This estimate might not be precise but might be unbiased respect to the one calculated from the data. Let me explain you what I mean by that:

the plot of the 'Min' shows that an horizontal line can be safely done on top of the bars and that an overall average can be 46K dollars (46.000 USD).

Following the same logic it can be said that for other statistics we have the median of 110K, mean of  110K and max of 190K. This can be seeing in [Median](plot/EDA1%20Bargraphs%201.1%20Median.png), [Max](plot/EDA1%20Bargraphs%201.3%20Max.png). 

Notice these statistics can change for Senior Data engineers and Senior Data Scientists. 

The second conclusion can the be summarized in two fold. First, Seniority has advantages in terms of salary. Second of all , that salaries for data analysts are averaging regardless the country, about 110K USD/year. This is an important conclusion, as we see that there is not such a big difference of salary respect to the job title.

Basic statistics of salary by IT role are presented in
[LDESC03](/out/LDESC03.html). The table is organized ascending according to the statistic values. For instance, means and medians are increasing in magnitude. The conclusion is then that the Jobs at the bottom are better paid. Business analyst jobs offer a mean of 80K whereas a Machine Learning Engineer may be paid 120K in average [EDA1 Scaterplots 4.0](/plot/EDA1%20Scaterpots%204.0.png) shows a plot of the mean yearly salary respect to the 'n' number of job vacancies by job category. 

I want to talk a bit about this scaterplot. It is very interesting, open it in a big forma, as the trends can be subtile and hidden in colors or scattered in the plot. Let us see. The vertical axis represents the counts of available vacancies by job ('n'), and the x axis indicates the yearly salary axis going from 46K up to about 250K. The size of the bubbles indicate the size of the salary. The bigger the salary, the bigger the bubble. Colors represent the types of Jobs. For instance, Data Analysts are in green color. Notice how Data analysts (green) are diametrally oposed to the Data engineers (black) and Data Scientists (dark red). This is an interesting insight. It looks like Data analyst are highly required as well as Data engineers, but Data Analysts are paid less good.


Notice all graphs have a dataset you can access to check particular values. This graph was derived from the [EDA1_Heatmap_3.0.1](/data/EDA1_Heatmap_3.0.1.csv). The data is available in the out folder [LDESC03](/out/LDESC03.html). This is the Listing of Salary statistics by IT Job. Data Engineers, Machine Learning Engineers and Senior professionals have salaries with means around 120K. This can serve as a conclusion for this chapter. 

In any case, We will see that Job titles are arbitrary as requested skills vary not only accross country, but also within the Job titles themselves. We will see that a Data Analyst in Belgium is not the same Data Analyst elsewhere. 



# Conclusion

Summarizing the mean salary for an IT Job was  110K in 2023. With an overall Minium salary of 46K and max of 190K.

Germany (17%), France (16%), Poland (13%), Spain (10%) accounted for about 60% of the total vacancies in Europe. In terms of Jobs, Data Analyst (23%), Data Engineer (22%) and Data Scientist (18%) accounted for roughly the 60% of the total vacancies. There is undoubtelly a country effect but not the one we would expect. Portugal is among the high payers and Italy is the worst. A Data Analyst is paid around 50K/year.

In the IT Jobs market Training is very relevant for a high salary. One skill alone might not move a needdle as the title itself. Professionals that profiled themselves as Data Engineers were highly regarded because they were expected to dominate many skills (about 40). Their Salaries ranged from 90K-180K. Data Engineers (DEE) and Data scientists (DSC) are highly rewarded. Notice that a Data Engineer may be hired just by a subset of its skills, but research on this aspect goes beyond our purpose here.

Most of job oportunities in 2023 came from Germany (DEE 150K, DSC 130K), Poland (DEE 140K, DSC140K) and Portugal (DEE 130K, DSC 160K). Being a senior has just advantages as the skill set required is smaller and the pay is higher, but there were no many vacancies for Senior Data Analysts or Senior Data Engineers. Business Analysts (82K) and Data analyst(90K) are highly required as well. They are not required to dominate particular skills like other IT professionals, but it comes with a lower wage. Data Analyst and Business Analyst job descriptions involve such a very wide group of disparate skills that at the end, they do not look like to be specialized. 

Conclusion of the conclusion. Are you recruiter looking for an IT professional? go to Italy to hunt for Data Analysts. Are you looking for a IT job but you do not have the hot title experience? profile yourselve as a Data Scientist and go to Portugal or Poland.   


# Further Analysis

  There was not evidence of specialization in jobs like Data Analyst or Business Analyst. These jobs are paid less maybe because of the overall perception of lack of specialization. I do believe that many Business are specialized, but in reality, those specialized Business Analysts may need to rebrand themselves. This is a coplex topic that might prove to be interesting, I suppose recruiters in traditional companies are looking for Data Analysts, Banks and Finance for Business Analysts and IT companies for Data Scientists. In reality I can dare to say that job content may be very similar, but this is feed for further digging.

  There is not a clear distinction of skills respect to Job title, this may offer oportunities to the new job applicant. Nevertheless, further research need to be done to identify what a particular sector is acostummed to. Business Analyst is a very poorly paid generic title, but heavily used in Banks and insurances. It might be interesting to explore the reception of newcomers by hiring departments after application rebranding. 












