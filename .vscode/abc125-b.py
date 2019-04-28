import sys
import subprocess
import re
import datetime
import os

N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))
ans = 0

for i in range(N):
    if V[i]>C[i]:
        ans = ans + (V[i]-C[i])


print(ans)
        

