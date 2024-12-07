CREATE TABLE TDESC04 (
    country TEXT,
    job TEXT,
    param TEXT,
    aval VARCHAR,
    parameter TEXT
);

--DROP TABLE tdesc04

INSERT INTO tdesc04 (country, job, param, aval, parameter)
VALUES (
    'country:text',
    'job:text',
    'param:text',
    'aval:character varying',
    'parameter:text'
  );



COPY tdesc04(country, job, param, aval, parameter)
FROM 'C:/Users/USUARIO/projects/python/portfolio/work/data/TDESC04.csv' 
WITH (FORMAT csv, HEADER true, DELIMITER ',');


COPY TDESC04(country, job, param, aval, parameter)
FROM 'C:\Users\USUARIO\projects\python\portfolio\work\data\TDESC04.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',');




COPY TDESC04(country, job, param, aval, parameter)
FROM 'C:\\Users\\USUARIO\\projects\\python\\portfolio\\work\\data\\TDESC04.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',');