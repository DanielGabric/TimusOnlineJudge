#smarter bottom-up DP solution than previous memoization top down solution 
N = input()
K = input()
#F = [[0 for i in range(0,K)] for i in range(0, N+1)]
G = [1]+[K-1]+[0 for i in range(0,N-1)]
for i in range(2,N+1):
    G[i]=(K-1)*(G[i-1]+G[i-2])
print G[N]
#dumb memory heavy DP solution
#for j in range(1,K):
#    F[0][j]=1
#for i in range(1,N+1):
#    for j in range(0,K):
#        for k in range(0,K):
#            if k==0 and j==0:
#                continue
#            F[i][j]+=F[i-1][k]
#print F[N][K-1]