import streamlit as st
import matplotlib.pyplot as plt
from simulation import waste_growth_prediction

st.title("Waste Growth Prediction")

# Check if waste data exists
if "waste" not in st.session_state:
    st.warning("Please enter waste data on the Home page first.")
    st.stop()

waste = st.session_state.waste

# Calculate total waste from stored data
total_waste = sum(waste.values())

st.subheader("Current Waste Data")

st.write(f"Organic Waste: {waste['Organic']} kg")
st.write(f"Plastic Waste: {waste['Plastic']} kg")
st.write(f"Paper Waste: {waste['Paper']} kg")
st.write(f"Metal Waste: {waste['Metal']} kg")

st.write(f"Total Waste: {total_waste:.2f} kg")

# Predict growth
years, growth = waste_growth_prediction(total_waste)

fig, ax = plt.subplots()

ax.plot(years, growth, marker="o")

ax.set_xlabel("Years")
ax.set_ylabel("Waste (kg)")
ax.set_title("Future Waste Growth Prediction")

st.pyplot(fig)