import sys
cache={}
def rec(N,lastColor=-1,lastTwo=-1):
    sums=0
    if N==0:
        return 1
    h = str(N)+str(lastColor)+str(lastTwo)
    if h in cache:
        return cache[h]
    if lastColor == -1:
        sums+=rec(N-1,1)
        sums+=rec(N-1,2)
    elif lastTwo ==-1:
        if lastColor == 1:
            sums+=rec(N-1,2,1)
            if N!=1:sums+=rec(N-1,0,1)
        else:
            sums+=rec(N-1,1,2)
            if N!=1:sums+=rec(N-1,0,2) 
    elif lastColor == 1:
        sums+=rec(N-1,2,1)
        if N!=1:sums+=rec(N-1,0,1)
    elif lastColor == 2:
        if N!=1:sums+=rec(N-1,0,2)
        sums+=rec(N-1,1,2)
    elif lastColor ==0:
        if lastTwo == 1:
            sums+=rec(N-1,2,0) 
        else:
            sums+=rec(N-1,1,0)

    cache[h]=sums
    return sums
for line in sys.stdin:
    print rec(int(line))