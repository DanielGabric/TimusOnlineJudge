cache={}
def rec(N,K,lastDigit=0):
    sums=0
    if N==0:
        return 1
    h = str(N)+str(K)+str(lastDigit)
    if h in cache:
        return cache[h]
    if lastDigit != 0:
        sums+=rec(N-1,K,0)
    for i in range(1,K):
        sums+=rec(N-1,K,i)
    cache[h]=sums
    return sums
N=0
K=0
N=input()
K = input()
print rec(N,K)