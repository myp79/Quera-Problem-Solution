#include <iostream>
using namespace std;
int max(const int array[])
{
    int maximum = array[0];
    for (int i = 1; i < 4; ++i)
    {
        if (array[i] > maximum)
        {
            maximum = array[i];
        }
    }
    return maximum;
}
int min(const int array[])
{
    int minimum = array[0];
    for (int i = 1; i < 4; ++i)
    {
        if (array[i] < minimum)
        {
            minimum = array[i];
        }
    }
    return minimum;
}
int main()
{
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    int array[] = {a, b, c, d};
    printf("Sum : %.6f\n", (float)(a + b + c + d));
    printf("Average : %.6f\n", (float)(a + b + c + d) / (float)4);
    printf("Product : %.6f\n", (float)(a * b * c * d));
    printf("MAX : %.6f\n", (float)max(array));
    printf("MIN : %.6f\n", (float)min(array));
    return 0;
}
// Mohammad YousefiPour - Github.com/myp79