#include <stdio.h>

int main(int argc, const char * argv[]) {
    int t, i, min, max;
    scanf("%d", &t);
    int arr[t];
    for(i=0; i<t; i++){
        scanf("%d", &arr[i]);
    }
    min = arr[0];
    max = arr[0];
    for(i=0;i<t;i++){
        if(min>arr[i]){
            min = arr[i];
        }
        if(max<arr[i]){
            max = arr[i];
        }
    }
    printf("%d %d", min, max);
    return 0;
}