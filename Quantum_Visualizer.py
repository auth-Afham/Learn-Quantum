import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# List of functions to plot each visualization
def wave_function(ax):
    """ Quantum Wave Packet """
    ax.clear()
    x = np.linspace(-10, 10, 400)
    psi = np.exp(-(x / 2) ** 2) * np.exp(1j * 5 * x)
    ax.plot(x, np.real(psi), label='Real part')
    ax.plot(x, np.imag(psi), label='Imaginary part')
    ax.plot(x, np.abs(psi), label='Magnitude', linestyle='dashed')
    ax.set_title("Quantum Wave Packet")
    ax.set_xlabel("Position")
    ax.set_ylabel("Wave Amplitude")
    ax.legend()

def quantum_entanglement(ax):
    """ Simulated Quantum Entanglement """
    ax.clear()
    outcomes = ["00", "11"]
    probs = [0.5, 0.5]
    ax.bar(outcomes, probs, color=['blue', 'red'])
    ax.set_title("Simulated Quantum Entanglement")
    ax.set_xlabel("Quantum State")
    ax.set_ylabel("Probability")
    ax.set_ylim(0, 1)

def atomic_orbital(ax):
    """ Hydrogen Atomic Orbital """
    ax.clear()
    x = np.linspace(-5, 5, 200)
    y = np.linspace(-5, 5, 200)
    X, Y = np.meshgrid(x, y)
    Z = np.exp(-np.sqrt(X**2 + Y**2)) * np.cos(np.arctan2(Y, X))
    contour = ax.contourf(X, Y, Z, cmap='viridis')
    plt.colorbar(contour, ax=ax, label='Electron Probability Density')
    ax.set_title("Hydrogen Atomic Orbital")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

# List of visualizations
visualizations = [wave_function, quantum_entanglement, atomic_orbital]
current_index = 0

# Create figure
fig, ax = plt.subplots(figsize=(6, 4))
plt.subplots_adjust(bottom=0.2)
visualizations[current_index](ax)  # Show first visualization

# Button functions
def next_plot(event):
    global current_index
    current_index = (current_index + 1) % len(visualizations)
    visualizations[current_index](ax)
    plt.draw()

def prev_plot(event):
    global current_index
    current_index = (current_index - 1) % len(visualizations)
    visualizations[current_index](ax)
    plt.draw()

# Add buttons
ax_prev = plt.axes([0.7, 0.05, 0.1, 0.075])
ax_next = plt.axes([0.81, 0.05, 0.1, 0.075])
btn_prev = Button(ax_prev, 'Previous')
btn_next = Button(ax_next, 'Next')

btn_prev.on_clicked(prev_plot)
btn_next.on_clicked(next_plot)

plt.show()
