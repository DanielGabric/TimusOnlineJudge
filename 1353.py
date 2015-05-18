F = [[0 for i in range(82)] for i in range(10)]
F[0][0]=1
for i in range(1,10):
    for s in range(1,82):
        for k in range(0,10):
            if s >=k:
                F[i][s]+=F[i-1][s-k]
sums=0
L = input()
for i in range(1,10):
    sums+=F[i][L]
if L == 1: sums+=1
print sums