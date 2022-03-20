## Question :

Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.

The CITY table is described as follows:

<div align="center">
    <img src="https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg">
</div>

## Solution :

SELECT `NAME` from CITY WHERE `POPULATION` > 120000 and `COUNTRYCODE` = 'USA';