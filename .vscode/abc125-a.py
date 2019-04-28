import sys
import subprocess
import re
import datetime
import os


A,B,T = map(int,input().split())
count = T/A
print(count)
ans = B*count

print(ans)

