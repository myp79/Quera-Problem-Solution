#include <iostream>

using namespace std;

int main() {
    int x1, v1, x2, v2;
    cin >> x1 >> v1 >> x2 >> v2;
    int difV = v2 - v1;
    int difX = x2 - x1;
    if (difV == 0) {
        cout << "WAIT WAIT";
    } else if (difX / difV > 0) {
        cout<<"BORO BORO";
    } else {
        cout << "SEE YOU";
    }

}
// Mohammad YousefiPour - Github.com/myp79