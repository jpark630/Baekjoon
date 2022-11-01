#include<stdio.h>
int main (){
    int a, b, c, d, e, f;
    scanf("%d\n%d", &a, &b);
    c = a*(b%10);
    d = a*(b/10%10);
    e = a*(b/100);
    printf("%d\n", c);
    printf("%d\n", d);
    printf("%d\n", e);
    printf("%d", c+(d*10)+(e*100));
    return 0;
}
