#include <stdio.h>

int main(int argc, const char * argv[]) {
    int a, c;
    scanf("%d", &a);
    c = a;
    int i=0;
    do{
        if(c<10){
            c = c*10+c;
        }
        else{
            c = (c%10)*10+((c/10)+(c%10))%10;
        }
        i++;
    }while(a!=c);
    printf("%d", i);

    return 0;
}
