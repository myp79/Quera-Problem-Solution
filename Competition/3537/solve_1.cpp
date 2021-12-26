#include <iostream>
#include <string>
using namespace std;
int main()
{
    int n, i = 0;
    string result;
    cin >> n;
    while (i < n)
    {
        result.append("o");
        i++;
    }
    cout << "W" << result << "w!" << endl;
    return 0;
}

// Mohammad YousefiPour - Github.com/myp79