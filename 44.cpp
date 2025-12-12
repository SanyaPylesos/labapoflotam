#include <iostream>
using namespace std;

int main() {
    float num = 16777210.0f; 
    
    while (num < num + 1.0f) {
        cout << num << endl;
        num += 1.0f;
    }
    cout << "переполнилось";

    return 0;
}
