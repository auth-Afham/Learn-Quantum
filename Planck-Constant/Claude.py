import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Planck constant (in J⋅s)
h = 6.626e-34

def plot_planck_relationships():
    # Create frequencies array (in Hz)
    frequencies = np.linspace(1e14, 5e14, 1000)
    
    # Calculate energies using E = hf
    energies = h * frequencies
    
    # Create figure with GridSpec for multiple plots
    fig = plt.figure(figsize=(15, 10))
    gs = GridSpec(2, 2, figure=fig)
    
    # Plot 1: E = hf relationship
    ax1 = fig.add_subplot(gs[0, :])
    ax1.plot(frequencies/1e14, energies/1e-19, 'b-', linewidth=2)
    ax1.set_title('Energy vs Frequency (E = hf)', fontsize=12)
    ax1.set_xlabel('Frequency (10¹⁴ Hz)', fontsize=10)
    ax1.set_ylabel('Energy (10⁻¹⁹ Joules)', fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    # Add text box with Planck constant
    ax1.text(0.02, 0.95, f'Planck constant (h) ≈ {h:.2e} J⋅s', 
             transform=ax1.transAxes, bbox=dict(facecolor='white', alpha=0.8))
    
    # Plot 2: Photon wavelengths and energies
    wavelengths = np.linspace(200e-9, 800e-9, 1000)  # 200-800 nm
    photon_energies = (h * 3e8) / wavelengths
    
    ax2 = fig.add_subplot(gs[1, 0])
    ax2.plot(wavelengths*1e9, photon_energies/1e-19, 'r-', linewidth=2)
    ax2.set_title('Photon Energy vs Wavelength', fontsize=12)
    ax2.set_xlabel('Wavelength (nm)', fontsize=10)
    ax2.set_ylabel('Energy (10⁻¹⁹ Joules)', fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    # Plot 3: Quantum harmonic oscillator energy levels
    n_levels = 5
    energy_levels = np.arange(n_levels)
    frequencies_osc = np.linspace(1e12, 5e12, 100)
    
    ax3 = fig.add_subplot(gs[1, 1])
    for n in energy_levels:
        E_n = h * frequencies_osc * (n + 0.5)
        ax3.plot(frequencies_osc/1e12, E_n/1e-21, '-', 
                label=f'n={n}', linewidth=2)
    
    ax3.set_title('Quantum Harmonic Oscillator Energy Levels', fontsize=12)
    ax3.set_xlabel('Oscillator Frequency (THz)', fontsize=10)
    ax3.set_ylabel('Energy (10⁻²¹ Joules)', fontsize=10)
    ax3.grid(True, alpha=0.3)
    ax3.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_planck_relationships()