raw = raw_input().split()
N = int(raw[0])
K = int(raw[1])
DP = [2**i if i <= K else 0 for i in range(N+1)]
for i in range(K+1,N+1):
    DP[i]=2*DP[i-1]-1
    if i >= K+2:
        DP[i]-=DP[i-K-2]-1
print DP[N]