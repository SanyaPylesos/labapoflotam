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
    union {
        float fval;
        unsigned int ival;
    } converter;
    
    float f;
    cin >> f;
    
    converter.fval = f;
    printBinary(converter.ival);
    
    return 0;}
