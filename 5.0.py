int find_iterations_for_precision(float target_error) {
    float pi_approx;
    for (int iter = 1; ; iter++) {
        pi_approx = Leibniz(iter);  // вычислили π
        float error = fabs(pi_approx - π_true);
        
        if (error < target_error) {
            return iter;  // нашли нужное число итераций!
        }
    }
}
