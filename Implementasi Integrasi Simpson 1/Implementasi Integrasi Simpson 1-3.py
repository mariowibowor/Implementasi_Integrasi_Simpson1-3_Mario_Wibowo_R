import time
import numpy as np

# Medefinisikan fungsi yang diintegralkan
def f(x):
    return 4/(1+x**2)

# Implementasi Simpson 1/3
def simpson13(x0, xn, n):
    # Meghitung step size
    h = (xn - x0) / n

    # Mencari penjumlahan sum
    integration = f(x0) + f(xn)

    for i in range(1, n):
        k = x0 + i*h

        if i%2 == 0:
            integration += 2 * f(k)
        else:
            integration += 4 * f(k)

    # Mencari nilai terakhir integral
    integration *= h/3

    return integration

# Menghitung RMS Error
def calculate_rms(n, reference_pi):
    result = simpson13(0, 1, n)
    return np.sqrt(((result - reference_pi) ** 2))

# Eksekusi
reference_pi = 3.14159265358979323846
N_values = [10, 100, 1000, 10000]

for N in N_values:
    start_time = time.time()
    pi_estimate = simpson13(0, 1, N)
    end_time = time.time()
    execution_time = end_time - start_time
    rms_error = calculate_rms(N, reference_pi)

    print(f"N: {N}, Pi Estimate: {pi_estimate}, RMS Error: {rms_error}, Execution Time: {execution_time}")
