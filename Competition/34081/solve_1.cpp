#include <iostream>
using namespace std;
int main()
{
    int n, k, i = 1;
    int counter = 0;
    cin >> n >> k;
    while ((i + k) % n != 1)
    {
        i += k;
        counter++;
    }
    cout << counter + 1;
}
// Mohammad YousefiPour - Github.com/myp79