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
x_values = [0.00, 13.96, 27.93, 41.90, 55.87, 69.83, 86.59, 83.81, 97.77, 125.71]
y_values = [87.76, 83.70, 79.61, 82.09, 91.57, 79.15, 71.77, 44.16, 38.54, 48.76]

# Menghitung luas menggunakan metode Simpson 3/8
area_simpson_3_8 = calculate_area_simpson_3_8(x_values, y_values)
print("Luas dengan metode Simpson 3/8:", area_simpson_3_8)
