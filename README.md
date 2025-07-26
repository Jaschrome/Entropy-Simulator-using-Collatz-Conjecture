# 🧪 Entropy Simulator using Collatz Conjecture

A Streamlit app that models energy decay and entropy using the mathematical behavior of the Collatz Conjecture.

## 🎯 Features
- Entropy is derived from the distribution of peak energies across particles.
- Temperature = initial energy range.
- Real-time graph + stats with sliders.
- Based on statistical mechanics + chaos theory.

## 📊 What is Simulated?
Each particle starts with an energy (random int). It decays via:
- `/2` if even
- `3n + 1` if odd

The peak energy in each decay chain is used to analyze energy spread and entropy.

## 🛠 Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
