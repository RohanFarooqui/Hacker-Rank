## Question :

Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:

<div align="center">
    <img src="https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg">
</div>

where LAT_N is the northern latitude and LONG_W is the western longitude.

## Solution :

SELECT DISTINCT(CITY) from STATION WHERE
LEFT(CITY,1) NOT IN ('a','e','i','o','u')
OR 
RIGHT(CITY,1) NOT IN ('a','e','i','o','u')
 