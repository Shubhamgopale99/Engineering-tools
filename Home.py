import streamlit as st

st.set_page_config(page_title="Tank & Coil Toolbox", layout="wide")

st.title("Tank & Coil Engineering Toolbox")
st.markdown(
    """
    Welcome to the **Tank & Coil Engineering Toolbox**.
    
    This multipage app includes:
    - Volume ↔ Dimension conversions
    - Dish ends calculations
    - Limpet coil design
    - Arc length calculation
    - Heat exchanger area
    - ASME UG-27 shell thickness check
    - And more!
    
    **Navigate using the sidebar** to choose your tool.
    """
)

st.info("Select a tool from the sidebar to get started.")
