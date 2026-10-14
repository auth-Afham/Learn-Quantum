import numpy as np
import matplotlib.pyplot as plt

# Constants
PLANCK_CONSTANT = 6.62607015e-34  # Planck constant in J·s (joule-seconds)
SPEED_OF_LIGHT = 3.0e8            # Speed of light in m/s

# Function to calculate energy from frequency using E = h * f
def calculate_energy(frequency):
    return PLANCK_CONSTANT * frequency

# Function to generate random frequencies (in Hz) within a realistic range
def generate_random_frequencies(num_points, min_freq=1e12, max_freq=1e15):
    # Frequencies in terahertz (THz) to petahertz (PHz) range, e.g., infrared to ultraviolet
    return np.random.uniform(min_freq, max_freq, num_points)

# Function to convert frequency to wavelength (λ = c / f)
def frequency_to_wavelength(frequency):
    return SPEED_OF_LIGHT / frequency

# Generate random data
np.random.seed(42)  # For reproducibility
num_points = 100
frequencies = generate_random_frequencies(num_points)
energies = calculate_energy(frequencies)
wavelengths = frequency_to_wavelength(frequencies)

# Create visualizations
plt.figure(figsize=(14, 8))

# Plot 1: Energy vs Frequency
plt.subplot(2, 1, 1)
plt.scatter(frequencies, energies, color='blue', alpha=0.6, label='Photon Energy')
plt.title('Energy vs Frequency (E = h * f)', fontsize=14)
plt.xlabel('Frequency (Hz)', fontsize=12)
plt.ylabel('Energy (J)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.text(0.05, 0.95, f'Planck Constant (h) = {PLANCK_CONSTANT} J·s', 
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top')

# Plot 2: Energy vs Wavelength
plt.subplot(2, 1, 2)
plt.scatter(wavelengths, energies, color='red', alpha=0.6, label='Photon Energy')
plt.title('Energy vs Wavelength (λ = c / f)', fontsize=14)
plt.xlabel('Wavelength (m)', fontsize=12)
plt.ylabel('Energy (J)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# Adjust layout and display
plt.tight_layout()
plt.show()

# Print some sample data for reference
print("\nSample Data (First 5 Points):")
print(f"{'Frequency (Hz)':<20} {'Wavelength (m)':<20} {'Energy (J)':<20}")
print("-" * 60)
for i in range(5):
    print(f"{frequencies[i]:<20.2e} {wavelengths[i]:<20.2e} {energies[i]:<20.2e}")