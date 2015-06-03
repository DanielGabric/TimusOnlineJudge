cache=[[-1 for i in range(1001)] for i in range(1001)]

def rec(s,n):
    sums=0
    if s < 0:
        return 0
    if n==0:
        if s== 0:
            return 1
        else:
            return 0
    if cache[s][n] !=-1:
        return cache[s][n]
    for i in range(10):
        sums+= rec(s-i,n-1)
    cache[s][n]=sums
    return sums
f = raw_input().split()
if int(f[1]) % 2 == 1:
    print "0"
else:
    print rec(int(f[1])/2,int(f[0]))**2