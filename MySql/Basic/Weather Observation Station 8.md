## Question :

Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:

<div align="center">
    <img src="https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg">
</div>

where LAT_N is the northern latitude and LONG_W is the western longitude.

## Solution :

SELECT DISTINCT(CITY) from STATION WHERE 

((CITY LIKE 'a%a') OR (CITY LIKE 'a%e') OR (CITY LIKE 'a%i') OR (CITY LIKE 'a%o') OR (CITY LIKE 'a%u'))
OR
((CITY LIKE 'e%a') OR (CITY LIKE 'e%e') OR (CITY LIKE 'e%i') OR (CITY LIKE 'e%o') OR (CITY LIKE 'e%u'))
OR
((CITY LIKE 'i%a') OR (CITY LIKE 'i%e') OR (CITY LIKE 'i%i') OR (CITY LIKE 'i%o') OR (CITY LIKE 'i%u'))
OR
((CITY LIKE 'o%a') OR (CITY LIKE 'o%e') OR (CITY LIKE 'o%i') OR (CITY LIKE 'o%o') OR (CITY LIKE 'o%u'))
OR
((CITY LIKE 'u%a') OR (CITY LIKE 'u%e') OR (CITY LIKE 'u%i') OR (CITY LIKE 'u%o') OR (CITY LIKE 'u%u'));