N=input()
dp = [0]+[1]+[1]+[2]+[0]*(N-3)
for i in range(4,N+1):
    dp[i]=dp[i-1]+dp[i-3]+1
print dp[N]