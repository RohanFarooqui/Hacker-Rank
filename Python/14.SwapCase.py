'''
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
Input Format

A single line containing a string S .

Constraints

0 < len(s) <= 1000

Output Format

Print the modified string .

Sample Input 0

HackerRank.com presents "Pythonist 2".
Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".


'''

def swap_case(x):
    y=""
    for i in x:
        if(i.isupper()):
            a=i.lower()
            y= y+a
        else:
            a=i.upper()
            y = y+a
    return y

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
