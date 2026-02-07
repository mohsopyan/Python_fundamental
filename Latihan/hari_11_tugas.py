sensor_data = [5, 2, 30, 16, 9]
sensor_data.append(23)
sensor_data[1] = 0

total_data = len(sensor_data)

print(f"Update Data: {sensor_data}")
print(f"Total Data: {total_data}")

print("\n Laporan Sensor")
for data in sensor_data:
    if data == 0:
        print("Peringatan: Data Rusak (0)")
    else:
        print(f"Nilai Sensor: {data}")