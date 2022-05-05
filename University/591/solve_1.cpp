#include <iostream>
using namespace std;
int main()
{
    int x;
    cin >> x;
    for (int i = 0; i < x; i++)
    {
        cout << "*";
    }
    cout << endl;
    for (int i = 0; i < x - 2; i++)
    {
        cout << "*";
        for (int j = 0; j < x - 2; j++)
        {
            cout << " ";
        }
        cout << "*" << endl;
    }
    for (int i = 0; i < x; i++)
    {
        cout << "*";
    }

    return 0;
}
// Mohammad YousefiPour - Github.com/myp79