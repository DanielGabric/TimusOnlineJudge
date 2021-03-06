#include <stdio.h>
#define N 10000
#define mod 1000000009
typedef long long int LONG;
int primes[143]={101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997};
int main(){
    int input;
    scanf("%d",&input);
    LONG F[N+1][100]={0};
    int ps[1000]={0};
    int i,j,length;
    //intializing primes and base cases for DP
    for(i=0;i<143;++i){
        ps[primes[i]]=1;
        F[3][primes[i]%100]++;
    }
    //We only care about the length of the number and the last two digits
    //Generate all odd digits and all 2 digit numbers
    //if the the 2 digit number + odd digit is a prime
    //then add all combinations of three primes with those last two digits
    //being the end
    //i.e. i = 3, j = 23, length = 5
    //233 is a prime so
    // F[5][33] = (F[5][33]+F[4][23]) % mod
    //calculate sub problems to solve the main problem
    for(length=4;length<=N;++length)
        for(i=1;i<=9;i+=2)
            for(j=10;j<=99;++j)
                if(ps[j*10+i])
                    F[length][i+(j%10)*10]=(F[length][i+(j%10)*10]+F[length-1][j])%mod;
    LONG sum=0;
    for(i=0;i<100;++i)
        sum=(sum+F[input][i])%mod;
    printf("%lli\n",sum);
    return 0;
}