#!/usr/bin/python3

# Change the n1 and n2 values below to visualize other energy levels
# If they differ by more than 1, the <x> expectation value will stay in the middle over time!

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ------------------------------------------------------------------------------
# Constants and parameters
# ------------------------------------------------------------------------------
n1, n2 = 1,2          # Quantum numbers of the two states in superposition
hbar = 1.0545718e-34   # Planck's constant / 2π (J·s)
m = 9.10938356e-31     # Electron mass (kg), or choose another mass if desired
L = 1e-9               # Well width in meters

# Number of spatial points
N = 200
x = np.linspace(0, L, N)

# Total time and number of frames
T = 5e-15              # Final time (seconds)
num_frames = 500
dt = T / num_frames

# ------------------------------------------------------------------------------
# Energy eigenvalues
# ------------------------------------------------------------------------------
# E_n = (n^2 π^2 ħ^2) / (2mL^2)
def energy_level(n, L, m):
    return (n**2 * (np.pi**2) * (hbar**2)) / (2 * m * (L**2))

E1 = energy_level(n1, L, m)
E2 = energy_level(n2, L, m)

# ------------------------------------------------------------------------------
# Spatial wavefunctions (time-independent parts)
# Each stationary state: ψ_n(x) = sqrt(2/L) sin(nπx/L)
# ------------------------------------------------------------------------------
def psi_n(n, x, L):
    return np.sqrt(2.0 / L) * np.sin(n * np.pi * x / L)

psi1_x = psi_n(n1, x, L)
psi2_x = psi_n(n2, x, L)

# ------------------------------------------------------------------------------
# Time-dependent overall wavefunction
# Superposition: (1/√2) [ψ1 e^{-i E1 t / ħ} + ψ2 e^{-i E2 t / ħ}]
# Probability density: |ψ(x, t)|^2
# ------------------------------------------------------------------------------
def psi_superposition(psi1, psi2, E1, E2, t):
    # Complex exponentials for time evolution
    factor1 = np.exp(-1j * E1 * t / hbar)
    factor2 = np.exp(-1j * E2 * t / hbar)
    return (1.0 / np.sqrt(2)) * (psi1 * factor1 + psi2 * factor2)

def probability_density(psi):
    # |psi|^2 = psi * conjugate(psi)
    return np.abs(psi)**2

# ------------------------------------------------------------------------------
# Set up the figure and animation
# ------------------------------------------------------------------------------
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2, color='blue', label='Probability density')

# Create a vertical line to indicate the expectation value
expectation_line = ax.axvline(0, color='purple', lw=2, label='⟨x⟩')

ax.set_xlim(0, L)
ax.set_ylim(0, 0.5e10)  # adjust the y-limit as needed for your parameters
ax.set_xlabel("x (m)")
ax.set_ylabel("Probability density")
ax.set_title("Infinite well time evolution of superposition of En {} and {}".format(n1, n2))
ax.legend(loc='upper right')


# Initialization function: clear the data
def init():
    line.set_data([], [])
    expectation_line.set_xdata([0, 0])
    return line, expectation_line

# Animation function
def animate(i):
    t = i * dt
    # Construct the wavefunction in space
    psi_t = psi_superposition(psi1_x, psi2_x, E1, E2, t)
    # Compute probability density
    prob = probability_density(psi_t)

    # Update probability density line
    line.set_data(x, prob)
    
    # Compute expectation value of x
    # Use a numerical integration approach, e.g. trapz
    x_mean = np.trapz(prob * x, x)
    
    # Update the vertical line at x_mean
    expectation_line.set_xdata([x_mean, x_mean])
    
    # Update the title
    ax.set_title(f"Time evolution, t = {t:.2e} s, ⟨x⟩ = {x_mean:.3e} m")

    return line, expectation_line


# Create animation
ani = animation.FuncAnimation(
    fig, animate, init_func=init, frames=num_frames, interval=50, blit=True
)

plt.show()
