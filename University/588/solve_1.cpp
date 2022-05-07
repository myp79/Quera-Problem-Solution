#include <iostream>
using namespace std;
int main()
{
    int n, x, max = 0;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> x;
        if (x >= max)
        {
            max = x;
        }
    }
    cout << max;

    return 0;
}
// Mohammad YousefiPour - Github.com/myp79