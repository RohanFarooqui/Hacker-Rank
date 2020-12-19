'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

2 <= n <= 10
-100 <= A[i] <= 100

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5

Sample Output 0

5
Explanation 0

Given list is [2,3,6,6,5] . The maximum score is , second maximum is . Hence, we print  5 as the runner-up score.'''


def fun(x):
    count = 0
    a= max(x)
    for i in x:
        if(i == a):
            count = count + 1
    for i in range(0,count):
          x.remove(a)
    print(max(x))
        






if __name__ == '__main__':
    l=[]
    n = int(input())
    arr = map(int, input().split())
    for i in arr:
        l.append(i)
    fun(l)
        
