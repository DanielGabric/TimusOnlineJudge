F = [[0 for i in range(10)] for i in range(82)]
F[0][0]=1
#lengths of numbers from 1-9
for i in range(1,10):
    #sums from 1 to 81
    for s in range(1,82):
        #digits from 0-9
        for k in range(0,10):
            if s >=k:
                F[s][i]+=F[s-k][i-1]
L = input()
sums = sum(F[L])
if L == 1: sums+=1
print sums 