'''
You are given a string  s and width  w.
Your task is to wrap the string into a paragraph of width w .

Input Format

The first line contains a string, .
The second line contains the width, .

Constraints

0 < len(s) < 100
0 < w < len (s)
Output Format

Print the text wrapped paragraph.

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''

import textwrap

def wrap(string, max_width):
    count = 0
    l=[]
    a=""
    for i in string:
        count = count + 1
        a= a+i
        if(count == (max_width)):
            count = 0
            l.append(a)
            a=""
    l.append(a)
        
    for i in range(0,len(l)-1):
        print(l[i])
    length = len(l)
    return l[length-1]
 

if __name__ == '__main__':
    #string, max_width = input(), int(input())
    result = wrap("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 4)
    print(result)    
