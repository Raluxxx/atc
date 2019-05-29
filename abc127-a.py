A = list(map(int, input().split())) 
r = A[0]
D = A[1]
f = A[2]
 
 
count = 0
ans = 0
 
for i in range(10):
    f = (r*f) - D 
    count = count + 1
    print(f)
    if(count == 10):
        break