import sys
#STUPID MEMOIZATION SOLUTION
cache={}
def rec(N,last,M):
    sums=0
    if N==M:
        return 1
    elif N>M:
        return 0
    h = str(N)+str(last)
    if h in cache :
        return cache[h] 
    for i in range(last+1,M-N+1):
        sums+=rec(N+i,i,M)
    cache[h]=sums
    return sums
#SMART DP SOLUTION-> KNAPSACK
dp = [[0 for i in range(501)] for i in range(501)]
dp[0][0]=1
for i in range(1,501):
    for j in range(0,501):
        if j <i:
            dp[i][j]=dp[i-1][j]
            continue

        dp[i][j]=dp[i-1][j]+dp[i-1][j-i]
for lines in sys.stdin:
    print dp[int(lines)][int(lines)]-1