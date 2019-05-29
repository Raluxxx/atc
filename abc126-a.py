A = list(map(int, input().split()))
S = input()

C = A[1]
D = A[0]
ans = ""

B = S[C-1]

if(B == "A"):
    B = "a"
elif(B == "B"):
    B = "b"
else:
    B = "c"

for i in range(D):
    if (i == C-1 ):
        ans = ans + B
        continue
    ans = (ans + S[i]) 

print(ans)