#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    int x, n;
    cin >> x >> n;
    if (n == 0)
    {
        cout << 20;
    }
    else if (n == 7)
    {
        cout << x;
    }
    else
    {
        cout << max(0, x - n);
    }
    return 0;
}
// Mohammad YousefiPour - Github.com/myp79