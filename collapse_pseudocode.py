import random

# Define a wavefunction as a dictionary of probabilities for outcomes
def create_wavefunction(outcomes, probabilities):
    """
    Creates a wavefunction with outcomes and associated probabilities.
    :param outcomes: List of possible outcomes (e.g., ['left', 'right'])
    :param probabilities: List of probabilities corresponding to outcomes
    :return: A wavefunction as a dictionary
    """
    return {outcome: prob for outcome, prob in zip(outcomes, probabilities)}

# Combine quantum wavefunction with the environment wavefunction
def combine_wavefunctions(quantum_wf, env_wf):
    """
    Combines two wavefunctions by normalizing their probabilities.
    :param quantum_wf: Quantum wavefunction (dictionary)
    :param env_wf: Environment wavefunction (dictionary)
    :return: A new combined wavefunction
    """
    combined_wf = {}
    for outcome in quantum_wf.keys():
        if outcome in env_wf:
            # Multiply probabilities and normalize later
            combined_wf[outcome] = quantum_wf[outcome] * env_wf[outcome]
    # Normalize combined probabilities
    total_prob = sum(combined_wf.values())
    for outcome in combined_wf:
        combined_wf[outcome] /= total_prob
    return combined_wf

# Collapse wavefunction to a single outcome based on probabilities
def collapse_wavefunction(wavefunction):
    """
    Collapses a wavefunction to a single outcome based on its probabilities.
    :param wavefunction: The wavefunction to collapse
    :return: A single outcome
    """
    outcomes = list(wavefunction.keys())
    probabilities = list(wavefunction.values())
    return random.choices(outcomes, weights=probabilities, k=1)[0]

# Example: Quantum system and environment wavefunctions
quantum_wf = create_wavefunction(['left', 'right'], [0.7, 0.3])  # Quantum has 70% chance 'left'
env_wf = create_wavefunction(['left', 'right'], [0.5, 0.5])      # Environment doesn't favor any side

# Step 1: Combine quantum wavefunction with the environment's wavefunction
combined_wf = combine_wavefunctions(quantum_wf, env_wf)
print(f"Combined Wavefunction: {combined_wf}") # 'left' has 60% chance and 'right' has 40% chance

# Step 2: Collapse the combined wavefunction to a single outcome
collapsed_outcome = collapse_wavefunction(combined_wf)
print(f"Collapsed Outcome: {collapsed_outcome}")
