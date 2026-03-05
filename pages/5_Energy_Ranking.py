import streamlit as st
from calculations import energy_analysis, energy_ranking

st.title("Energy Contribution Ranking")

if "waste" not in st.session_state:
    st.warning("Please enter waste data on the Home page first.")
    st.stop()

waste = st.session_state.waste

energy_results, total_energy = energy_analysis(waste)

ranking = energy_ranking(energy_results)

st.subheader("Energy Contribution by Waste Type")

for i, (w, e) in enumerate(ranking, 1):
    st.write(f"{i}. {w} Waste → {e:.2f} kWh")