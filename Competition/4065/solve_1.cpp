#include <iostream>
using namespace std;
int main()
{
    int a, b, l;
    cin >> a >> b >> l;
    if (l % 2 == 0)
    {
        cout << (a + b) * (l / 2);
    }
    else
    {
        cout << a * (l / 2 + 1) + b * (l / 2);
    }
    return 0;
}
// Mohammad YousefiPour - Github.com/myp79