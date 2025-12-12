#include <iostream>
using namespace std;

void printBinary(unsigned int n) {
    for (int i = 31; i >= 0; i--) {
        cout << ((n >> i) & 1); 
        
        if(i / 4 * 4 == i){
        cout << ' ';
    }
        
    }
    cout << endl;
    
    
}

int main() {
    unsigned int num;
    cin >> num;
    printBinary(num);
    return 0;
}
