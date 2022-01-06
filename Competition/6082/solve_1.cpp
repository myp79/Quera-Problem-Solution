#include <iostream>
using namespace std;
int main()
{
    int n, m, sum = 0;
    cin >> n >> m;
    char in;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> in;
            if (in == '*')
            {
                sum++;
            }
        }
    }
    cout << sum;
}
// Mohammad YousefiPour - Github.com/myp79