## Question :

Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:


<div align="center">
    <img src="https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg">
</div>

where LAT_N is the northern latitude and LONG_W is the western longitude.

## Solution :

SELECT DISTINCT(CITY) from STATION WHERE 

CITY NOT LIKE 'a%' AND 
CITY NOT LIKE 'e%' AND
CITY NOT LIKE 'i%' AND 
CITY NOT LIKE 'o%' AND
CITY NOT LIKE 'u%';