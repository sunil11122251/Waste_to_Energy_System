import streamlit as st
from calculations import energy_analysis

st.title("Energy Demand vs Supply Analysis")

if "waste" not in st.session_state:
    st.warning("Please enter waste data on the Home page first.")
    st.stop()

waste = st.session_state.waste

energy_results, total_energy = energy_analysis(waste)

demand = st.number_input("Enter City Energy Demand (kWh)", 0.0)

st.subheader("Energy Comparison")

st.write(f"Energy Generated from Waste: {total_energy:.2f} kWh")

difference = total_energy - demand

if difference > 0:
    st.success(f"Surplus Energy: {difference:.2f} kWh")

elif difference < 0:
    st.error(f"Energy Deficit: {abs(difference):.2f} kWh")

else:
    st.info("Energy exactly meets demand")