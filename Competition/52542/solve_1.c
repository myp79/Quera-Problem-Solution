#include <stdio.h>
int main()
{
    int n;
    scanf("%d", &n);
    int x[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &x[i]);
    }
    for (int i = 0; i < n; i++)
    {
        if (x[i] <= 3)
        {
            for (int j = 0; j < x[i]; j++)
            {
                printf("*");
            }
            printf("\n");
        }
        else
        {
            printf("*\n");
        }
    }
    return 0;
}
// Mohammad YousefiPour - Github.com/myp79