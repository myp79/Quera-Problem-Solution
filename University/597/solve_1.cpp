#include <iostream>
using namespace std;
int main()
{
    int n, x = 0, y = 0;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        switch (i % 4)
        {
        case 1:
            x *= -1;
            x++;
            break;
        case 2:
            y *= -1;
            y++;
            break;
        case 3:
            x *= -1;
            break;

        default:
            y *= -1;
            break;
        }
    }
    cout << x << " " << y;
}
// Mohammad YousefiPour - Github.com/myp79