n = int(input())
a = []
for i in range(1,n+1):
    b, c = input().split()
    a.append((b, -1*int(c), i))
 
a.sort()
print(a)


for i in a:
    print(i[2])