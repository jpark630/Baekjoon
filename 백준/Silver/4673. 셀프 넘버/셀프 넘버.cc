#include <stdio.h>
int isSelfNum(int n){
    int sum = n;
    while(n>0){
        sum+=n%10;
        n/=10;
    }
    return sum;
}

int main(int argc, const char * argv[]) {
    int arr[10001], result=0;
    for(int i=0;i<10001;i++){
        result=isSelfNum(i);
        if(result<10001) arr[result]=1;
    }
    for(int j=0; j<10001; j++){
        if(arr[j]!=1) printf("%d\n",j);
    }
    
    return 0;
}
