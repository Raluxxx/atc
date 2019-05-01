import sys
import subprocess
import re
import datetime
import os

N = int(input())
A = list(map(int,input().split()))

A.sort(reverse=True)

Alice = 0
Bob = 0

for i in range(N):
    if i%2 == 0:
        Alice = Alice + A[i]
    else:
        Bob = Bob + A[i]

ans = (Alice - Bob)

print(ans)


