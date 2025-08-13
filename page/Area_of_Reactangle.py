import streamlit as st
import math

st.title("Area of Rectangle")

@st.cache_data
def rectangle_area(length_mm: float, width_mm: float) -> float:
    if width_mm <= 0 or length_mm <= 0:
        return float('nan')
    return (width_mm / 1000.0) * (length_mm / 1000.0)  # mm² to m²

length_mm = st.number_input("Length (mm)", min_value=0.0)
width_mm = st.number_input("Width (mm)", min_value=0.0)

if st.button("Calculate Area"):
    area = rectangle_area(length_mm, width_mm)
    if math.isnan(area):
        st.error("Invalid input values.")
    else:
        st.success(f"Area of Rectangle: {area:.2f} m²")

