#include <iostream>
using namespace std;
int main()
{
    int m, n, sum = 0;
    cin >> n >> m;
    for (int i = -10; i <= m; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            sum += ((i + j) * (i + j) * (i + j)) / (j * j);
        }
    }
    cout << sum;
    return 0;
}
// Mohammad YousefiPour - Github.com/myp79