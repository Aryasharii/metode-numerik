def calculate_area_simpson_3_8(x_values, y_values):
    n = len(x_values)
    h = 3.74

    if n % 3 != 1:
        raise ValueError("Jumlah titik harus memenuhi syarat untuk metode Simpson 3/8.")

    area = y_values[0] + y_values[n-1]

    for i in range(1, n - 1):
        if i % 3 == 0:
            area += 2 * y_values[i]
        else:
            area += 3 * y_values[i]

    area *= 3 * h / 8

    return area

# Data titik-titik x dan y
x_values = [0, 14.96, 29.93, 44.90, 59.87, 74.83, 89.806, 104.77, 119.74, 134.71,
            7.48, 22.44, 37.4, 52.36, 67.32, 82.28, 97.24, 112.2, 127.16, 
            3.74, 11.22, 18.7, 26.18, 33.66, 41.14, 48.62, 56.1, 63.58,
            71.06, 78.54, 86.02, 93.5, 100.98, 108.46, 115.94, 123.42, 130.9]

y_values = [88.06, 81.41, 83.49, 95.11, 113.5, 96.04, 101.26, 45.9, 44.03, 46.28,
            81.41, 83.19, 86.74, 102.13, 98.31, 100.66, 48.86, 45.82, 43.02,
            84.63, 81.67, 83.32, 83.3, 84.49, 90.85, 98.63, 102.39, 100.31,
            97.2, 98.35, 101.11, 50.11, 52.51, 46.05, 44.58, 45.72, 42.76]

sorted_data = sorted(zip(x_values, y_values), key=lambda x: x[0])
sorted_x_values, sorted_y_values = zip(*sorted_data)

print("Data x terurut:")
print(sorted_x_values)

print("\nData y mengikuti urutan nilai x:")
print(sorted_y_values)

# Menghitung luas menggunakan metode Simpson 3/8
area_simpson_3_8 = calculate_area_simpson_3_8(sorted_x_values, sorted_y_values)
print("Luas dengan metode Simpson 3/8:", area_simpson_3_8)
