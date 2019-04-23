import sys
import subprocess
import re
import datetime
import os


s = input()
count = 0

for i in s:
    if i == 1:
        count = count + 1

print(count)



