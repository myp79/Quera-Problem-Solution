#include <iostream>
using namespace std;
int main()
{
    unsigned long long int n, sum = 0;
    cin >> n;
    while (n / 10 > 0)
    {
        sum += n % 10;
        n /= 10;
    }
    sum += n;
    while (sum / 10 > 0)
    {
        n = sum;
        sum = 0;
        while (n / 10 > 0)
        {
            sum += n % 10;
            n /= 10;
        }
        sum += n;
    }

    cout << sum << endl;

    return 0;
}
// Mohammad YousefiPour - Github.com/myp79