import matplotlib.pyplot as plt

thread = [1, 2, 4, 8, 16, 32, 64]

latency1 = [840.32, 857.06, 964.84, 1271.53, 2280.28, 4059.18, 8130.94]

latency2 = [1528.75, 1532.31, 1714.01, 2254.40, 4186.96, 7351.82, 14675.12]

latency3 = [2228.47, 2220.18, 2483.86, 3279.49, 6112.66, 10732.33, 21301.78]

latency4 = [2918.74, 2914.59, 3288.65, 4330.10, 8089.65, 14147.92, 28080.66]

latency5 = [3662.78, 3598.54, 4055.53, 5405.76, 9909.30, 17528.79, 34786.10]

latency6 = [7308.47, 7178.53, 8015.20, 10704.29, 19220.29, 34995.37, 69382.51]

# Plotting
plt.figure(figsize=(8, 6))

plt.plot( thread, latency1, label='L = 10')
plt.plot( thread, latency2, label='L = 20')
plt.plot( thread, latency3, label='L = 30')
plt.plot( thread, latency4, label='L = 40')
plt.plot( thread, latency5, label='L = 50')
plt.plot( thread, latency6, label='L = 100')

plt.xlabel('Thread')
plt.ylabel('Mean Latency')
plt.title('Mean Latency vs Thread')
plt.legend()

plt.grid(True)
plt.show()
