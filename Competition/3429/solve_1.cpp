#include <iostream>
using namespace std;
int main()
{
    int t;
    cin >> t;
    if (t < 0)
    {
        cout << "Ice";
    }
    else if (t >= 0 && t <= 100)
    {
        cout << "Water";
    }
    else
    {
        cout << "Steam";
    }

    return 0;
}
// Mohammad YousefiPour - Github.com/myp79