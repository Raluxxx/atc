S = input()

if(S[0] == 0):
    Z = int(S[1])
else:
    Z = S[0] + S[1]
    X = int(Z)

if(S[2] == 0):
    K = int(S[3])
else:
    K = S[2] + S[3]
    Y = int(K)

if(1 <= X <= 12):
    if(1 <= Y <= 12):
        print("AMBIGUOUS")
    else:
        print("MMYY")
else:
    if(1 <= Y <= 12):
        print("YYMM")
    else:
        print("NA")