#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;
    for (int i = 0; i < n+1; ++i) {
        for (int k = n; k > i; --k) {
            cout<<" ";
        }
        for (int j = 0; j <2*i+1 ; ++j) {
            cout<<"*";
        }
        cout<<endl;
    }
    for (int i = n; i > 0; --i) {
        for (int k = n-i; k >= 0; --k) {
            cout<<" ";
        }
        for (int j =2*i-1; j >0 ; j--) {
            cout<<"*";
        }
        cout<<endl;
    }

    return 0;
}
// Mohammad YousefiPour - Github.com/myp79