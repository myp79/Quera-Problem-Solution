#include <iostream>
using namespace std;
bool prime(int x){
    int counter=0;
    for (int i = 2; i <x ; ++i) {
        if (x%i==0){
            counter++;
        }
    }
    return counter==0;
}
int main() {
    int a,b,counter=0;
    cin>>a>>b;
    for (int i = a+1; i <b ; ++i) {
        if (prime(i)){
            if (counter!=0){
                cout<<",";
            }
                counter++;
            cout<<i;
        }
    }

    return 0;
}
// Mohammad YousefiPour - Github.com/myp79