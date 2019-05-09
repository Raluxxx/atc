import sys
import subprocess
import re
import datetime
import os

A = []
A[0] = int(input())
A[1] = int(input())
A[2] = int(input())
A[3] = int(input())
A[4] = int(input())
k = int(input())

S = A.sorted()

V = (S[4] - S[0])
if V <= k:
    print("Yay!")
else:
    print(":(")
    
        










