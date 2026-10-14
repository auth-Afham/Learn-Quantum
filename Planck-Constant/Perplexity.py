import numpy as np
import matplotlib.pyplot as plt

# Physical constants in SI units: Planck's constant (J.s), 
# the speed of light (m.s-1), Boltzmann's constant (J.K-1)
h = 6.62607015e-34  # J*s
c = 299792458      # m/s
kB = 1.38064852e-23 # J/K

# Generate random temperatures between 500 K and 8000 K
np.random.seed(0) # For reproducibility
temperatures = np.random.uniform(500, 8000, size=5)

# Wavelength range from visible to near infrared (400 nm to 2000 nm)
lambda_min = 400 * 1e-9 # Convert nm to m
lambda_max = 2000 * 1e-9 # Convert nm to m

n_wavelengths = int((lambda_max - lambda_min) / (10 * lambda_min)) + 10

wavelengths = np.linspace(lambda_min, lambda_max, n_wavelengths)

fig, ax = plt.subplots(figsize=(8,6))

for T in temperatures:
    B_lambda_T = (2*h*c**2) / wavelengths**5 / (np.exp(h*c/(wavelengths*kB*T)) - 1)
    
    ax.plot(wavelengths*1e9, B_lambda_T*10000,
            label=f'T={T:.2f}K')

ax.set_xlabel('Wavelength [nm]')
ax.set_ylabel('Spectral Radiance [W sr^-1 m^-3] x10^4')
ax.legend()
plt.title("Blackbody Radiation Curves")
plt.show()
