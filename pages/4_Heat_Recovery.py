import streamlit as st
from calculations import energy_analysis, heat_recovery

st.title("Heat Recovery Analysis")

if "waste" not in st.session_state:
    st.warning("Please enter waste data on the Home page first.")
    st.stop()

waste = st.session_state.waste

energy_results, total_energy = energy_analysis(waste)

heat = heat_recovery(total_energy)

st.subheader("Energy Recovery")

st.write(f"Total Electrical Energy: {total_energy:.2f} kWh")

st.metric("Recovered Heat Energy (40%)", f"{heat:.2f} kWh")