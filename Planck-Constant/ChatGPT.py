import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Constants
true_h = 6.626e-34  # Planck's constant (Js)
work_function = 2.1e-19  # Example work function (J)

# Generate random frequencies in visible-UV range (Hz)
np.random.seed(42)
frequencies = np.random.uniform(4e14, 9e14, 20)  # Random frequencies (Hz)

# Compute kinetic energy using the photoelectric equation: KE = h*f - work_function
kinetic_energies = true_h * frequencies - work_function
kinetic_energies[kinetic_energies < 0] = 0  # No emission if energy is insufficient

# Perform linear regression to estimate Planck's constant
slope, intercept, r_value, _, _ = linregress(frequencies, kinetic_energies)

# Plot the data
plt.figure(figsize=(8, 5))
plt.scatter(frequencies, kinetic_energies, color='blue', label='Simulated Data')
plt.plot(frequencies, slope * frequencies + intercept, color='red', linestyle='--', label='Best Fit Line')
plt.axhline(0, color='black', linewidth=0.5)

# Labels and title
plt.xlabel('Frequency (Hz)')
plt.ylabel('Kinetic Energy (J)')
plt.title("Photoelectric Effect and Planck's Constant Approximation")
plt.legend()
plt.grid(True)

# Display estimated Planck's constant
estimated_h = slope
print(f"Estimated Planck's Constant: {estimated_h:.3e} Js (True h = {true_h} Js)")

# Show the plot
plt.show()