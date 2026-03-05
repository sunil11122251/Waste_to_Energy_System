import streamlit as st
from calculations import energy_analysis, revenue

st.title("Economic Analysis")

# check if waste data exists
if "waste" not in st.session_state:
    st.warning("Please enter waste data on the Home page first.")
    st.stop()

waste = st.session_state.waste

energy_results, total_energy = energy_analysis(waste)

rev = revenue(total_energy)

st.subheader("Economic Output")

st.write(f"Total Energy Generated: {total_energy:.2f} kWh")

st.metric("Estimated Electricity Revenue", f"₹{rev:.2f}")