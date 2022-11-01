#include <stdio.h>
int main (){
    int a, b, c;
    scanf("%d %d %d",&a, &b, &c);
    int sum = a*b*c;
    int result[10]={0};
    
    while(sum>0){
        result[sum%10]++;
        sum /= 10;
    }
    for(int i = 0; i < 10; i++){
        printf("%d\n", result[i]);
    }
}
