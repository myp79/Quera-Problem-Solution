#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    double n;
    int k;
    cin >> n >> k;
    while (k != 0)
    {
        n /= 2;
        k--;
    }
    cout << floor(n);
}
// Mohammad YousefiPour - Github.com/myp79