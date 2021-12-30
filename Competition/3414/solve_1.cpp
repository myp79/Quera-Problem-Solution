#include <iostream>
using namespace std;
int main()
{
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    if (b == d)
    {
        cout << "Horizontal";
    }
    else if (a == c)
    {
        cout << "Vertical";
    }
    else
    {
        cout << "Try again";
    }

    return 0;
}
// Mohammad YousefiPour - Github.com/myp79