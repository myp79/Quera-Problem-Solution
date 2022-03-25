#include <iostream>

using namespace std;

int main()
{
    int n, k, counter = 0, i;
    cin >> n >> k;
    int arr[n];
    for (i = 0; i < n; ++i)
    {
        cin >> arr[i];
    }
    i = 0;
    while (i < n)
    {
        int sum = 0;
        while (sum <= k)
        {
            sum += arr[i];
            i++;
        }
        i--;
        counter++;
    }
    cout << counter;
    return 0;
}
// Greedy Approch
// Mohammad YousefiPour - Github.com/myp79
