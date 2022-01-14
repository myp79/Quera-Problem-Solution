#include <iostream>
using namespace std;
int main()
{
    int x, y, a, sum = 0;
    cin >> x >> y;
    for (int i = 0; i < x; i++)
    {
        cin >> a;
        sum += a;
    }
    if (sum % y > 0)
    {
        sum = sum / y;
        cout << x - sum - 1;
    }
    else
    {
        sum = sum / y;
        cout << x - sum;
    }
    return 0;
}
// Mohammad YousefiPour - Github.com/myp79