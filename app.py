import streamlit as st

st.set_page_config(page_title="Waste to Energy System", layout="wide")

st.title("Smart Municipal Waste-to-Energy Analytics System")

st.header("Enter Waste Composition")

organic = st.number_input("Organic Waste (kg)", 0.0)
plastic = st.number_input("Plastic Waste (kg)", 0.0)
paper = st.number_input("Paper Waste (kg)", 0.0)
metal = st.number_input("Metal Waste (kg)", 0.0)

if st.button("Save Waste Data"):

    st.session_state.waste = {
        "Organic": organic,
        "Plastic": plastic,
        "Paper": paper,
        "Metal": metal
    }

    st.success("Waste data saved successfully!")

st.info("After saving data, use the sidebar to open analysis pages.")