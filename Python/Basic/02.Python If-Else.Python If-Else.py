
import math
import os
import random
import re
import sys

def fun(x):
    if((x>=2) and (x<=5) and (x%2==0)):
        print("Not Weird")
    elif((x>=6) and (x<=20) and (x%2==0)):
        print("Weird")
    elif((x>20) and(x%2==0)):
        print("Not Weird")
    else:
        print("Weird")


if __name__ == '__main__':
    n = int(input())
    fun(n)