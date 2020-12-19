'''
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.

Input Format

A single line of input containing the full name, .

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, .

Sample Input

chris alan
Sample Output

Chris Alan
'''
import os

def solve(s):
    name   = s.split(" ")
    result = []
    for i in name:
        string = ""
        for j in range(0,len(i)):
            if(j == 0):
                string = string + str(i[j].upper())
                #string.append(str(i[j].upper()))
            else:
                string = string + str(i[j])
                #string.append(str(i[j]))
        result.append(string)
    return (' '.join(result))

        
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #s = input()

    #result = solve("rohan farooqui")
    #result = solve("rohan")
    result = solve("hello   world  lol")

    #fptr.write(result + '\n')

    #fptr.close()

