#include <iostream>
using namespace std;
int main()
{
    int x, year, month;
    cin >> x;
    year = x / 100;
    month = x % 100;
    if (year <= 10)
    {
        cout << "saal:" << 0 << year << endl;
    }
    else
    {
        cout << "saal:" << year << endl;
    }
    if (month < 10)
    {
        cout << "maah:" << 0 << month;
    }
    else
    {
        cout << "maah:" << month;
    }
    return 0;
}
// Mohammad YousefiPour - Github.com/myp79