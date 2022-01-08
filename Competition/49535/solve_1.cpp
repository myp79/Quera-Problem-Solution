#include <iostream>
using namespace std;
int main()
{
    int n, k, sum = 0, a, i = 0;
    cin >> n >> k;
    while (i < n)
    {
        cin >> a;
        sum += a;
        i++;
    }
    sum >= k ? cout << "YES" : cout << "NO";
    return 0;
}
// Mohammad YousefiPour - Github.com/myp79