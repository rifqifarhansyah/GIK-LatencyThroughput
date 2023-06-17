import matplotlib.pyplot as plt

thread = [1, 2, 4, 8, 16, 32, 64]

throughput1 = [1159.18, 2271.90, 4047.66, 6174.90, 6940.88, 7826.95, 7818.17]
throughput2 = [644.12, 1284.61, 2299.97, 3508.72, 3796.36, 4331.43, 4339.36]
throughput3 = [443.75, 890.41, 1593.60, 2419.49, 2605.01, 2971.51, 2992.54]
throughput4 = [339.56, 679.87, 1206.15, 1835.33, 1970.26, 2255.27, 2271.45]
throughput5 = [270.99, 551.43, 979.34, 1471.66, 1609.28, 1820.67, 1835.63]
throughput6 = [136.21, 277.28, 496.84, 744.75, 830.58, 912.84, 919.87]

# Plotting
plt.figure(figsize=(8, 6))

plt.plot( thread, throughput1, label='L = 10')
plt.plot( thread, throughput2, label='L = 20')
plt.plot( thread, throughput3, label='L = 30')
plt.plot( thread, throughput4, label='L = 40')
plt.plot( thread, throughput5, label='L = 50')
plt.plot( thread, throughput6, label='L = 100')

plt.xlabel('Thread')
plt.ylabel('Throughput')
plt.title('Throughput vs Thread')
plt.legend()

plt.grid(True)
plt.show()
