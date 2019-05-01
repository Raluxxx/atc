import sys
import subprocess
import re
import datetime
import os

N,A,B = map(int,input().split())
ans = 0


for i in range(N+1):
    if A <= sum(int(k) for k in str(i)) <= B:
        ans += i

print(ans)
