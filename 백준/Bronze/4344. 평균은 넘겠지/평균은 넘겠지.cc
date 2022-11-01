
#include <stdio.h>

int main(int argc, const char * argv[]) {
    
    int test, t;
    
    scanf("%d", &test);
    
    for(int i=0; i<test; i++){
        scanf("%d", &t);
        int arr[t];
        double sum = 0;
        for(int a=0; a<t; a++){
            scanf("%d", &arr[a]);
            sum += arr[a];
        }
        double mem=0;
        double ave = 0;
        ave = sum/t;
        for(int c=0;c<t;c++){
            if(arr[c]>ave) mem++;
        }
        float percent = 100*mem/t;
        printf("%.3f%%\n",percent);
    }
    
    return 0;
}