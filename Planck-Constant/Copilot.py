import numpy as np
import matplotlib.pyplot as plt

# Define Planck's constant (in Joule-seconds)
h = 6.62607015e-34

# Generate random frequency data (in Hz)
num_points = 100
frequencies = np.random.uniform(low=1e14, high=1e15, size=num_points)

# Calculate corresponding energy values using Planck's equation E = h * f
energies = h * frequencies

# Plot the data
plt.figure(figsize=(10, 6))
plt.scatter(frequencies, energies, color='blue', alpha=0.6, label='Random data points')

# Add labels and title
plt.xlabel('Frequency (Hz)')
plt.ylabel('Energy (J)')
plt.title('Visualization of Planck\'s Constant using Random Data')
plt.legend()
plt.grid(True)
plt.show()
