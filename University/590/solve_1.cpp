#include <iostream>
using namespace std;
int main()
{
    long int a, b, c, pow;
    cin >> a >> b;
    pow = a * b;
    if (b > a)
    {
        c = a;
        a = b;
        b = c;
    }
    while (a % b > 0)
    {
        c = b;
        b = a % b;
        a = c;
    }
    cout << b << ' ' << pow / b;

    return 0;
}
// Mohammad YousefiPour - Github.com/myp79