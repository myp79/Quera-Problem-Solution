#include <iostream>
using namespace std;
int main()
{
    int fact = 1, n;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        fact *= i;
    }
    cout << fact;
    return 0;
}
// Mohammad YousefiPour - Github.com/myp79