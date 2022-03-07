#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    int n, k, c, max = 0;
    cin >> n >> k;
    int cake[n];
    int min3 = 100000;
    for (int i = 0; i < n; i++)
    {
        cin >> c;
        cake[i] = c;
    }
    if (k == 1)
    {
        for (int i = 0; i < n; i++)
        {
            if (cake[i] > max)
            {
                max = cake[i];
            }
        }
        cout << max;
    }
    else if (k == 2)
    {
        cout << min(cake[0], cake[n - 1]);
    }
    else
    {
        int min1 = cake[0];
        int min2 = cake[n - 1];
        for (int i = 1; i < n - 1; i++)
        {
            if (cake[i] > max)
            {
                max = cake[i];
            }
            else if (cake[i] < min3)
            {
                min3 = cake[i];
            }
        }
        if (k > 3)
        {
            cout << min(min3, min(max, min(min1, min2)));
        }
        else
        {
            cout << min(max, min(min1, min2));
        }
    }
    return 0;
}
// Mohammad YousefiPour - Github.com/myp79