
A = list(map(int, input().split()))

N = A[0]
K = A[1]
count = 0
ans[] = [1000000]

if(N > K):
    for i in range(K-1):
       for k in i:
         k = k*2
         count = count + 1
         if(k > K):
             ans[i] = (1/3) * (1/2)^count 
             break
else:
    for
    

