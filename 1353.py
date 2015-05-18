#solve using bottom-up Dynamic Programming
#solve from smaller sums then combine them
#to solve the bigger problem
F = [[0 for i in range(82)] for i in range(10)]
F[0][0]=1
#lengths of numbers from 1-9
for i in range(1,10):
    #sums from 1 to 81
    for s in range(1,82):
        #digits from 0-9
        for k in range(0,10):
            if s >=k:
                F[i][s]+=F[i-1][s-k]
sums=0
L = input()
for i in range(1,10):
    sums+=F[i][L]
if L == 1: sums+=1
print sums
