import streamlit as st
import matplotlib.pyplot as plt
from config import TREATMENT_EFFICIENCY

st.title("Treatment Method Comparison")

# Check if waste data exists
if "waste" not in st.session_state:
    st.warning("Please enter waste data on the Home page first.")
    st.stop()

waste = st.session_state.waste

# Calculate total waste automatically
total_waste = sum(waste.values())

st.subheader("Waste Data Used")

st.write(f"Organic Waste: {waste['Organic']} kg")
st.write(f"Plastic Waste: {waste['Plastic']} kg")
st.write(f"Paper Waste: {waste['Paper']} kg")
st.write(f"Metal Waste: {waste['Metal']} kg")

st.write(f"Total Waste: {total_waste:.2f} kg")

# Treatment methods
methods = list(TREATMENT_EFFICIENCY.keys())
energies = [TREATMENT_EFFICIENCY[m] * total_waste for m in methods]

# Graph
fig, ax = plt.subplots()

ax.bar(methods, energies)

ax.set_xlabel("Treatment Method")
ax.set_ylabel("Energy Potential (kWh)")
ax.set_title("Energy Potential by Treatment Method")

plt.xticks(rotation=25)

st.pyplot(fig)