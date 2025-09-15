#include <stdio.h>

int main()
{
    int a[40], n, se, i, found = 0;

    printf("Enter how many elements to add: ");
    scanf("%d", &n);

    
    for (i = 0; i < n; i++) {
        printf("Enter element %d: ", i + 1);
        scanf("%d", &a[i]);
    }

    
    printf("Enter element to search: ");
    scanf("%d", &se);


    for (i = 0; i < n; i++) 
    {
        if (a[i] == se) 
        {
            printf("Element %d found at position %d\n", se, i + 1);
            found = 1;
            break; 
        }
    }

    if (found == 0) {
        printf("Element %d not found in the array.\n", se);
    }

    return 0;
}
