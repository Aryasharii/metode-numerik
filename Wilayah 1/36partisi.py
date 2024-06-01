def calculate_area_simpson_3_8(x_values, y_values):
    n = len(x_values)
    h = 3.49

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
x_values = [0.00, 13.96, 27.93, 41.90, 55.87, 69.83, 86.59, 83.81, 97.77, 125.71, 
            6.98, 20.94, 34.9, 48.86, 62.82, 76.78, 90.74, 104.7, 118.66,
            3.49, 10.47, 17.45, 24.43, 31.41, 38.39, 45.37, 52.35, 59.33,
            66.31, 73.29, 80.27, 87.25, 94.23, 101.21, 108.19, 115.17, 122.15]
y_values = [87.76, 83.70, 79.61, 82.09, 91.57, 79.15, 71.77, 44.16, 38.54, 48.76,
            85.81, 81.12, 78.21, 90.34, 94.3, 73.68, 56.13, 41.86, 39.07,
            86.26, 84.21, 81.8, 80.58, 78.8, 79.01, 84.05, 90.95, 90.66,
            82.29, 76.1, 71.66, 66.94, 50.36, 41.43, 42.3, 38.66, 42.78]

sorted_data = sorted(zip(x_values, y_values), key=lambda x: x[0])
sorted_x_values, sorted_y_values = zip(*sorted_data)

print("Data x terurut:")
print(sorted_x_values)

print("\nData y mengikuti urutan nilai x:")
print(sorted_y_values)

# Menghitung luas menggunakan metode Simpson 3/8
area_simpson_3_8 = calculate_area_simpson_3_8(sorted_x_values, sorted_y_values)
print("Luas dengan metode Simpson 3/8:", area_simpson_3_8)
