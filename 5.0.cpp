#include <iostream>
#include <cmath>
#include <chrono>
#include <iomanip>
using namespace std;

const float π_true = 3.14159265358979323846f;

float Leibniz(int iter) {
    float π = 0.0f;
    for (int i = 0; i < iter; i++) {
        float curr = 1.0f / (2 * i + 1);
        if (i % 2 == 0) {
            π += curr;
        }
        else {
            π -= curr;
        }
    }
    return 4 * π;
}

int find_iterations_for_precision(float target_error) {
    for (int iter = 1; ; iter++) {
        float pi_approx = Leibniz(iter);
        float error = fabs(pi_approx - π_true);
        
        if (error < target_error) {
            return iter;
        }
    }
}

int main() {
    float target_errors[] = {0.1f, 0.01f, 0.001f, 0.0001f, 
                             0.00001f, 0.000001f, 0.0000001f, 0.00000001f};
    
    cout << "Нахождение итераций для формулы Лейбница:" << endl;
    cout << "Точность\tИтерации\tПолученное π\tОшибка" << endl;
    cout << "-------------------------------------------------------" << endl;
    
    for (int i = 0; i < 8; i++) {
        float target = target_errors[i];
        int iterations = find_iterations_for_precision(target);
        float pi_approx = Leibniz(iterations);
        float error = fabs(pi_approx - π_true);
        
        cout << fixed << setprecision(8);
        cout << target << "\t" << iterations << "\t\t";
        cout << setprecision(10) << pi_approx << "\t";
        cout << scientific << setprecision(2) << error << endl;
    }
    
    return 0;
}
