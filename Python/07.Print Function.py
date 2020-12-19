'''
Read an integer N.

Without using any string methods, try to print the following: 123....N


Note that "..." represents the values in between.

Input Format

The first line contains an integer .

Output Format

Output the answer as explained in the task.

Sample Input 0

3
Sample Output 0

123

'''
def fun(x):
    y=x+1
    for i in range(1,y):
        print(i,end="")


if __name__ == '__main__':
    n = int(input())
    fun(n)



def fun(x):
    y=x+1
    for i in range(1,y):
        print(i,end="")


if __name__ == '__main__':
    n = int(input())
    fun(n)

