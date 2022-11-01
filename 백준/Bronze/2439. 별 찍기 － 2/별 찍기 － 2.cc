#include <stdio.h>
int main (){
    int a;
    scanf("%d", &a);
    for(int i = 1; i <= a; i++){
        for(int k = a-i; k>0; k--){
            printf(" ");
        }
        for(int j = 0; j < i; j++){
            printf("*");
        }
        printf("\n");
    }
    return 0;
}