#include <iostream>
using namespace std;
int main()
{
    int x, sum = 0;
    cin >> x;
    for (int i = 1; i <= x / 2; i++)
    {
        if (x % i == 0)
            sum += i;
    }
    sum == x ? cout << "YES" : cout << "NO";
    cout << endl;
    return 0;
}
// Mohammad YousefiPour - Github.com/myp79