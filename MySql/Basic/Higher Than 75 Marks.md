## Question :

Query the Name of any student in STUDENTS who scored higher than  Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.

Input Format

The STUDENTS table is described as follows:

<div align="center">
    <img src="https://s3.amazonaws.com/hr-challenge-images/12896/1443815243-94b941f556-1.png">
</div>

The Name column only contains uppercase (A-Z) and lowercase (a-z) letters.

Sample Input

<div align="center">
    <img src="https://s3.amazonaws.com/hr-challenge-images/12896/1443815209-cf4b260993-2.png">
</div>

Sample Output

Ashley
Julia
Belvet
Explanation

Only Ashley, Julia, and Belvet have Marks > 75 . If you look at the last three characters of each of their names, there are no duplicates and 'ley' < 'lia' < 'vet'.



## Solution :

SELECT DISTINCT(CITY) 
from 
    STATION 
WHERE
    LEFT(CITY,1) NOT IN ('a','e','i','o','u')
and 
    LEFT(CITY,1) NOT IN ('A','E','I','O','U')
and
    RIGHT(CITY,1) NOT IN ('a','e','i','o','u')
 