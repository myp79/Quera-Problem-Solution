#include <iostream>
using namespace std;
int main()
{
    int a, b, c, result1, result2, result3;
    cin >> a >> b >> c;
    result1 = (c * c) == (a * a) + (b * b);
    result2 = (b * b) == (a * a) + (c * c);
    result3 = (a * a) == (c * c) + (b * b);
    if (result1 || result2 || result3)
    {
        cout << "YES";
    }
    else
    {
        cout << "NO";
    }
    return 0;
}
// Mohammad YousefiPour - Github.com/myp79