#include <iostream>
using namespace std;
bool fibo(int n)
{
    int a = 1, b = 1, sum = 1;
    while (true)
    {
        if (sum == n)
        {
            return true;
        }
        if (sum > n)
        {
            return false;
        }
        sum = a + b;
        a = b;
        b = sum;
    }
}
int main()
{
    int x;
    cin >> x;
    for (int i = 1; i <= x; i++)
    {
        if (fibo(i))
        {
            cout << "+";
        }
        else
        {
            cout << "-";
        }
    }

    return 0;
}
// Mohammad YousefiPour - Github.com/myp79