def calculate_area_simpson_3_8(x_values, y_values):
    n = len(x_values)
    h = 13.96

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
x_values = [0, 13.96, 27.93, 41.9, 55.87, 69.83, 86.592, 83.806, 97.77, 125.71]
y_values = [64.58, 66.38, 74.82, 79.19, 77.45, 78.44, 79.03, 77.27, 63, 58.16]

sorted_data = sorted(zip(x_values, y_values), key=lambda x: x[0])
sorted_x_values, sorted_y_values = zip(*sorted_data)

print("Data x terurut:")
print(sorted_x_values)

print("\nData y mengikuti urutan nilai x:")
print(sorted_y_values)

# Menghitung luas menggunakan metode Simpson 3/8
area_simpson_3_8 = calculate_area_simpson_3_8(sorted_x_values, sorted_y_values)
print("Luas dengan metode Simpson 3/8:", area_simpson_3_8)
