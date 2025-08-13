#include <stdio.h>

int main() {
    int a, b, c, big;

    printf("Enter three numbers: ");
    scanf("%d %d %d", &a, &b, &c);

    if (a > b)
        big = a;
    else
        big = b;

    if (c > big)
        big = c;

    printf("The biggest number is: %d\n", big);

    return 0;
}
