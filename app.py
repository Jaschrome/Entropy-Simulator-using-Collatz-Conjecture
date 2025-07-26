import streamlit as st
import matplotlib.pyplot as plt
import random

def collatz_sequence(n):
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq

def simulate_decay(n_particles):
    decay_lengths = []
    for _ in range(n_particles):
        start = random.randint(10, 1000)
        seq = collatz_sequence(start)
        even_steps = sum(1 for x in seq if x % 2 == 0)
        decay_lengths.append(even_steps)
    return decay_lengths

st.set_page_config(page_title="Collatz Radioactive Decay Simulator")

st.title("🧪 Collatz-Based Radioactive Decay Simulator")
st.markdown("Simulates energy decay by counting even steps in Collatz sequences.")

particles = st.slider("Number of particles", 100, 5000, 1000)
data = simulate_decay(particles)

fig, ax = plt.subplots()
ax.hist(data, bins=30, color="purple", edgecolor="black")
ax.set_title("Decay Step Distribution")
ax.set_xlabel("Decay Steps (Even Transitions)")
ax.set_ylabel("Number of Particles")
st.pyplot(fig)
