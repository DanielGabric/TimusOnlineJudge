#slow in python but same solution is better in C
import Library
mod = 10**9+9
n = input()
primes = Library.getPrimeList(1000)
for i in range(len(primes)-1,-1,-1):
    if primes[i]<100: 
        primes.pop(i)
print primes
F = [[ 0 for i in range(0,100)] for i in range(0, n+1)]
for i in primes:
    F[3][i%100]+=1
for N in range(4,n+1):
    for i in range(1,10,2):
        for j in range(10,100):
            if j*10+i in primes:
                F[N][i+(j%10)*10]+=F[N-1][j]
                F[N][i+(j%10)*10]%=mod
print sum(F[10000])%mod

