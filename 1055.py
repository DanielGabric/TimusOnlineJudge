def sieve(n):
    isPrime = [False]*2+[True]*(n-1)
    i=2
    while i*i<=n:
        j=i
        while i * j <=n:
            isPrime[i*j]=False
            j+=1
        i+=1
    return isPrime
def getPrimeList(n):
    isPrime = sieve(n)
    listPrimes = []
    for i in range(2, n+1):
        if isPrime[i]:listPrimes.append(i)

    return listPrimes
primes = getPrimeList(50000)
sums=0
raw = raw_input().split()
n = int(raw[0])
r = int(raw[1])
for p in primes:
    pj=p
    N=0
    while pj<=n:
        N += (n/pj-r/pj-(n-r)/pj)
        pj*=p
    if N > 0: sums+=1
print sums