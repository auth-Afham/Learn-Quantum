import numpy as np
import matplotlib.pyplot as plt

# Constants
h = 6.626e-34  # Planck constant (J·s)
c = 3e8        # Speed of light (m/s)

# Generate random wavelengths (in nanometers)
wavelengths_nm = np.random.uniform(100, 1000, 100)  # Random wavelengths between 100 nm and 1000 nm
wavelengths_m = wavelengths_nm * 1e-9  # Convert nm to meters

# Calculate frequencies (ν = c / λ)
frequencies = c / wavelengths_m

# Calculate energies (E = h * ν)
energies = h * frequencies

# Plotting
plt.figure(figsize=(12, 6))

# Plot Energy vs Wavelength
plt.subplot(1, 2, 1)
plt.plot(wavelengths_nm, energies, 'bo', markersize=5)
plt.xlabel('Wavelength (nm)')
plt.ylabel('Energy (J)')
plt.title('Energy vs Wavelength')
plt.grid(True)

# Plot Energy vs Frequency
plt.subplot(1, 2, 2)
plt.plot(frequencies, energies, 'ro', markersize=5)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Energy (J)')
plt.title('Energy vs Frequency')
plt.grid(True)

plt.tight_layout()
plt.show()