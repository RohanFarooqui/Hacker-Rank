'''
Given the names and grades for each student in a Physics class
of N students, store them in a nested list and print the name(s)
of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade,
order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, , N the number of students.
The  2N subsequent lines describe each student over 2
lines; the first line contains a student's name,
and the second line contains their grade.

Constraints

2 <= N <= 5

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are
multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry
Explanation 0

There are 5 students in this class whose names and grades are assembled
to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and
Berry, so we order their names alphabetically and print each name on a new line.
















'''
def fun(x):
    j=[]
    k=[]
    final=[]
    count=0
    for i in range(0,len(x)):
      j.append(x[i][0])
      k.append(x[i][1])
    
    k.sort()
    a=min(k)
    for i in k:
        if(i == a):
            count = count + 1
    for i in range(0,count):
          k.remove(a)

    
    b=min(k)
    for i in x:
        if(i[1] == b):
            final.append(i[0])
    final.sort()
    
    for i in final:
        print(i)


if __name__ == '__main__':
    l=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
    fun(l)


#fun([['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]])

#fun([['Harsh',5],['Beria',20],['Varun',20],['Kakunami',19],['Vikas',19]])
