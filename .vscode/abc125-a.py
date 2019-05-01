import sys
import subprocess
import re
import datetime
import os


A,B,T = map(int,input().split())
count = T//A
ans = B*count

print(ans)

