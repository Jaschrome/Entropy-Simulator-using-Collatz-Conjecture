import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random
import math

# Collatz sequence generator
def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence

# Simulate particles using Collatz-based energy decay
def simulate_collatz_gas(num_particles, temp_range):
    peak_energies = []
    for _ in range(num_particles):
        initial_energy = random.randint(*temp_range)
        seq = collatz_sequence(initial_energy)
        peak = max(seq)
        peak_energies.append(peak)

    states, counts = np.unique(peak_energies, return_counts=True)
    probabilities = counts / counts.sum()
    entropy = -np.sum(probabilities * np.log(probabilities))

    return states, counts, entropy

# Plot the results
def plot_distribution(states, counts, entropy, num_particles):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(states, counts, width=10, color='mediumseagreen', edgecolor='black')
    ax.set_title(f'Entropy Simulator using Collatz Conjecture\nEntropy = {entropy:.3f} for {num_particles} particles')
    ax.set_xlabel('Peak Energy (Max Collatz Value)')
    ax.set_ylabel('Particle Count')
    ax.grid(True)
    st.pyplot(fig)

# Streamlit UI
st.set_page_config(page_title="Collatz Entropy Simulator")
st.title("🧪 Entropy Simulator using Collatz Conjecture")

st.markdown("""
This simulation models a gas of particles where each particle's energy decays following the Collatz Conjecture. Entropy is calculated based on the distribution of peak energies in each sequence.
""")

num_particles = st.slider("Number of Particles", 100, 5000, 1000, step=100)
temp_min = st.slider("Minimum Initial Energy (Temperature)", 10, 500, 10)
temp_max = st.slider("Maximum Initial Energy (Temperature)", temp_min + 1, 2000, 1000)

if temp_min >= temp_max:
    st.warning("Minimum temperature must be less than maximum.")
else:
    states, counts, entropy = simulate_collatz_gas(num_particles, (temp_min, temp_max))
    plot_distribution(states, counts, entropy, num_particles)

    st.markdown(f"**Calculated Entropy:** {entropy:.4f}")
    st.markdown("""
    ---
    📈 You can interpret this as a thermodynamic system where the shape of the histogram shows the 'disorder' in particle energies. Try adjusting temperature and particle count to explore different entropy outcomes.
    """)
