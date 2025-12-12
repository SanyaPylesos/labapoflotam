#include <iostream>
using namespace std;

int main() {
    float num = 100.0f;
    
        
        if (num == num + 0.000001f) {
            cout << "эээ ну оно переполнилось короче";
        }
    
    return 0;
}
