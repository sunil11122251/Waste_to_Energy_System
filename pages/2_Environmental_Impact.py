import streamlit as st
from calculations import energy_analysis,co2_reduction

st.title("Environmental Impact Analysis")

if "waste" not in st.session_state:

    st.warning("Please enter waste data on Home page.")
    st.stop()

waste = st.session_state.waste

energy_results,total_energy = energy_analysis(waste)

co2 = co2_reduction(total_energy)

st.metric("CO₂ Reduction",f"{co2:.2f} kg")
st.write("Organic – Anaerobic Digestion: Anaerobic digestion converts organic waste into biogas and reduces landfill pollution.")
st.write("Plastic – Pyrolysis: Pyrolysis converts plastic waste into fuel and reduces plastic pollution.")
st.write("Paper – Incineration: Incineration burns paper waste to generate energy and reduces landfill volume.")
st.write("Metal – Recycling: Recycling metals saves natural resources and reduces mining impact ♻️.")