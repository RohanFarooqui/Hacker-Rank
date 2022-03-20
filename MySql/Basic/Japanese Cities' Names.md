## Question :

Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.

The CITY table is described as follows:

<div align="center">
    <img src="https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg">
</div>

## Solution :

SELECT `NAME` from CITY WHERE `COUNTRYCODE` = 'JPN';