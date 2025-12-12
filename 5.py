import matplotlib.pyplot as plt

# Данные: количество итераций для каждой точности (десятичного знака)
Leibniz_iter = [9, 100, 1000, 9354, 69957, 227569, 293567, 295861]
Wallis_iter = [8, 78, 787, 2049, 2049, 2049, 2049, 2049]
Nilakantha_iter = [1, 2, 6, 13, 29, 58, 94, 115]
Madhava_iter = [1, 5, 9, 16, 20, 41, 50, 85]
BBP_iter = [1, 1, 1, 2, 3, 4, 5, 12]

# Время выполнения в секундах (примерные данные, нужны реальные из программы)
# Замени эти значения на реальные из вывода программы!
time_Leibniz = [5.540000e-07, 3.470000e-07, 3.790000e-07, 3.470000e-07, 
                3.470000e-07, 3.530000e-07, 3.510000e-07, 3.450000e-07]

time_Wallis = [3.700000e-07, 3.500000e-07, 3.700000e-07, 3.480000e-07, 
               3.460000e-07, 3.520000e-07, 3.530000e-07, 3.480000e-07]

time_Nilakantha = [3.720000e-07, 3.500000e-07, 3.660000e-07, 3.450000e-07, 
                   3.480000e-07, 3.500000e-07, 3.490000e-07, 3.480000e-07]

time_Madhava = [7.846000e-06, 1.558380e-04, 6.540000e-07, 7.210000e-07, 
                7.380000e-07, 1.233000e-06, 1.195000e-06, 1.780000e-06]

time_BBP = [4.280000e-07, 4.130000e-07, 3.770000e-07, 4.790000e-07, 
            4.230000e-07, 4.410000e-07, 4.570000e-07, 5.870000e-07]

# Точности (десятичные знаки) от 10^-1 до 10^-8
precision_levels = ['10⁻¹', '10⁻²', '10⁻³', '10⁻⁴', '10⁻⁵', '10⁻⁶', '10⁻⁷', '10⁻⁸']
x_positions = range(len(precision_levels))

plt.figure(figsize=(14, 8))

# График времени от точности
plt.subplot(1, 2, 1)
plt.plot(x_positions, time_Leibniz, 'o-', label='Лейбниц', linewidth=2)
plt.plot(x_positions, time_Wallis, 's-', label='Валлис', linewidth=2)
plt.plot(x_positions, time_Nilakantha, '^-', label='Нилаканта', linewidth=2)
plt.plot(x_positions, time_Madhava, 'd-', label='Мадхава', linewidth=2)
plt.plot(x_positions, time_BBP, '*-', label='BBP', linewidth=2)

plt.xticks(x_positions, precision_levels)
plt.xlabel('Достигнутая точность (десятичный знак)', fontsize=12)
plt.ylabel('Время выполнения (секунды)', fontsize=12)
plt.title('Зависимость времени от точности', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)
plt.yscale('log')  # Логарифмическая шкала для времени

# График итераций от точности (для сравнения)
plt.subplot(1, 2, 2)
plt.plot(x_positions, Leibniz_iter, 'o-', label='Лейбниц', linewidth=2)
plt.plot(x_positions, Wallis_iter, 's-', label='Валлис', linewidth=2)
plt.plot(x_positions, Nilakantha_iter, '^-', label='Нилаканта', linewidth=2)
plt.plot(x_positions, Madhava_iter, 'd-', label='Мадхава', linewidth=2)
plt.plot(x_positions, BBP_iter, '*-', label='BBP', linewidth=2)

plt.xticks(x_positions, precision_levels)
plt.xlabel('Достигнутая точность (десятичный знак)', fontsize=12)
plt.ylabel('Количество итераций', fontsize=12)
plt.title('Зависимость итераций от точности', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)
plt.yscale('log')  # Логарифмическая шкала для итераций

plt.tight_layout()
plt.show()

# Еще один график: сравнение времени на одной точности
plt.figure(figsize=(10, 6))

formulas = ['Лейбниц', 'Валлис', 'Нилаканта', 'Мадхава', 'BBP']
times_at_precision_4 = [time_Leibniz[3], time_Wallis[3], time_Nilakantha[3], 
                        time_Madhava[3], time_BBP[3]]  # для точности 10^-4

bars = plt.bar(formulas, times_at_precision_4, color=['blue', 'orange', 'green', 'red', 'purple'])
plt.xlabel('Формула', fontsize=12)
plt.ylabel('Время выполнения (секунды)', fontsize=12)
plt.title('Время достижения точности 10⁻⁴', fontsize=14)
plt.grid(True, alpha=0.3, axis='y')

# Добавляем значения на столбцы
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2e}', ha='center', va='bottom')

plt.tight_layout()
plt.show()
