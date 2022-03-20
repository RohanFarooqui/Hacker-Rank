## Question :

Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:

<div align="center">
    <img src="https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg">
</div>

where LAT_N is the northern latitude and LONG_W is the western longitude.

## Solution :

SELECT DISTINCT(CITY) from STATION WHERE CITY LIKE '%a' OR CITY LIKE '%e' OR CITY LIKE '%I' OR CITY LIKE '%O' OR CITY LIKE '%U';