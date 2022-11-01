#include <stdio.h>
int main (){
    int b[9];
    for(int i = 0; i < 9; i++){
        scanf("%d", &b[i]);
    }
    int max = b[0];
    int sum=0;
    for(int j = 1; j<9;j++){
        if(max<b[j]){
            max = b[j];
            sum = j+1;
        }
    }
    printf("%d\n", max);
    if(sum == 0) printf("%d", 1);
    else printf("%d", sum);
    
    return 0;
}
