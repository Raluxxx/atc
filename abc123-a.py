import sys
import subprocess
import re
import datetime
import os

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

A = [a,b,c,d,e]
S = sorted(A)

V = (S[4] - S[0])
if V <= k:
    print("Yay!")
else:
    print(":(")

        










