import sys
import subprocess
import re
import datetime
import os


A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0

for i in range(A+1):
    print(count)
    for j in range(B+1):
        print(count)
        for k in range(C+1):
            if (500*A+100*B+50*C)==X:
                count = count + 1

print(count)

            
            
