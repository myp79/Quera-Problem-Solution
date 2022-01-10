#include <iostream>
using namespace std;
int main()
{
    int x, y, a, b;
    cin >> x >> y;
    if (x == 0)
    {
        x = 12;
    }
    if (y == 0)
    {
        y = 60;
    }
    a = 12 - x;
    b = 60 - y;
    if (a / 10 >= 1)
    {
        if (b / 10 >= 1)
        {
            cout << a << ":" << b;
        }
        else
        {
            cout << a << ":"
                 << "0" << b;
        }
    }
    else
    {
        if (b / 10 >= 1)
        {
            cout << "0" << a << ":" << b;
        }
        else
        {
            cout << "0" << a << ":"
                 << "0" << b;
        }
    }
    return 0;
}
// Mohammad YousefiPour - Github.com/myp79