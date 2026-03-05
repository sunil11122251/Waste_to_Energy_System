import streamlit as st
from calculations import energy_analysis
from config import TREATMENT_METHOD

st.title("Waste Treatment Analysis")

if "waste" not in st.session_state:

    st.warning("Please enter waste data on the Home page first.")
    st.stop()

waste = st.session_state.waste

energy_results,total_energy = energy_analysis(waste)

for w in waste:

    st.write(f"{w} → {TREATMENT_METHOD[w]}")

st.success(f"Total Energy Generated: {total_energy:.2f} kWh")