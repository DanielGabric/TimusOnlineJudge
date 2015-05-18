#include <stdio.h>
int main(){
    long long int dp[60001]={0},i,j,input;
    for (i=1;i<=60000;++i){
        dp[i]=i+1;
        for(j=1;j*j<=i;++j){
            dp[i]=(dp[i]<dp[i-j*j])?dp[i]:(1+dp[i-j*j]);
        }
    }
    while(scanf("%d",&input)!=EOF){
        printf("%llu\n", dp[input]);
    }
    return 0;
}