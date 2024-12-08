--CREATE database work


/*
CREATE TABLE TDESC04 (
    country TEXT,
    job TEXT,
    param TEXT,
    aval VARCHAR,
    parameter TEXT
);
*/


--DROP TABLE data_jobs

CREATE TABLE data_jobs (
    level_0 TEXT,
    id INT,
    job	TEXT,
    salary	FLOAT,
    location	TEXT,
    via	TEXT,
    homeworking TEXT,	
    dtc	TEXT,
    rate	TEXT,
    company	TEXT,
    skills	TEXT,
    country	TEXT,
    dt	TEXT,
    month	INT,
    year	INT,
    co	TEXT,
    analyzefl TEXT
);

ALTER TABLE data_jobs
DROP level_0;



create table summaries as
select distinct country as Country, job as Job,count(id) as n,
                to_char(round(avg(salary)/1000),'FM$999,999,999') as Mean,
                to_char(round(stddev(salary)/1000),'FM$999,999,999') as Stddev,
                to_char(round(min(salary)/1000),'FM$999,999,999') as Min,
                to_char(round(max(salary)/1000),'FM$999,999,999') as Max                            
 from (select distinct id,country, job, salary from data_jobs )
                group by country, job 
order by mean,n desc;

-- 7598 non missing records
select distinct count(id) from data_jobs where salary is not null GROUP BY job;



select distinct  job as Job,count(id) as n,
                to_char(round(avg(salary)/1000),'FM$999,999,999') as Mean,
                to_char(round(stddev(salary)/1000),'FM$999,999,999') as Stddev,
                to_char(round(min(salary)/1000),'FM$999,999,999') as Min,
                to_char(round(max(salary)/1000),'FM$999,999,999') as Max                            
 from (select distinct id,country, job, salary from data_jobs )
                group by job 
order by mean,n desc;



select distinct  country ,count(id) as n,
                to_char(round(avg(salary)/1000),'FM$999,999,999') as Mean,
                to_char(round(stddev(salary)/1000),'FM$999,999,999') as Stddev,
                to_char(round(min(salary)/1000),'FM$999,999,999') as Min,
                to_char(round(max(salary)/1000),'FM$999,999,999') as Max                            
 from (select distinct id,country, job, salary from data_jobs )
                group by country 
order by mean,n desc;







