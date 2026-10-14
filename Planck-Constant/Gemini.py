import matplotlib.pyplot as plt
import numpy as np

# Constants (using approximate values for visualization purposes)
PLANCK_CONSTANT = 6.626e-34  # Actual Planck constant (very small)
SPEED_OF_LIGHT = 3e8  # Speed of light
BOLTZMANN_CONSTANT = 1.38e-23 # Boltzmann constant

# Generate random data for frequency and temperature
num_points = 100
frequencies = np.linspace(1e14, 1e16, num_points)  # Range of frequencies (Hz)
temperatures = np.linspace(100, 3000, num_points) # Range of temperatures (Kelvin)

# Calculate energy using Planck's formula (simplified for visualization)
def planck_energy(frequency, temperature):
    # We are scaling the Planck constant for visualization.
    # The actual values are incredibly tiny and would make the plot unreadable.
    # This scaling DOES NOT represent actual physical values, but rather
    # a visually representative curve.
    h = PLANCK_CONSTANT * 1e20  # Scaled Planck constant for visualization
    k = BOLTZMANN_CONSTANT * 1e20 # Scaled Boltzmann constant for visualization
    return (h * frequency) / (np.exp((h * frequency) / (k * temperature)) - 1)


# Calculate energy for each frequency and temperature
energies = np.array([[planck_energy(f, T) for f in frequencies] for T in temperatures])

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the energy as a function of frequency for different temperatures
for i in range(0, len(temperatures), 10): # Plot a subset of temperatures for clarity
    ax.plot(frequencies, energies[i], label=f"T = {temperatures[i]:.0f} K")


ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Energy (Scaled for visualization)") # Important note about scaling
ax.set_title("Planck's Law: Energy vs. Frequency at Different Temperatures")
ax.legend()
ax.grid(True)

# Annotate the Planck constant (scaled)
ax.annotate(f"Scaled Planck Constant (h): {PLANCK_CONSTANT * 1e20:.2e}", 
            xy=(0.05, 0.90), xycoords='axes fraction', fontsize=10)

# Explain the scaling (crucial)
ax.text(0.05, 0.80, "Note: The Planck constant and Boltzmann constant\nare scaled for visualization purposes. The plotted\nenergy values do not represent actual physical values,\nbut rather demonstrate the relationship between energy,\nfrequency, and temperature.", fontsize=10, transform=ax.transAxes)


plt.tight_layout()
plt.show()



# 3D plot (optional - may be harder to interpret)
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

X, Y = np.meshgrid(frequencies, temperatures)
ax.plot_surface(X, Y, energies, cmap='viridis')

ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel("Temperature (K)")
ax.set_zlabel("Energy (Scaled for visualization)")
ax.set_title("Planck's Law: Energy vs. Frequency and Temperature")

plt.tight_layout()
plt.show()