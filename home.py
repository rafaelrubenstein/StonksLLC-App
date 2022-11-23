import streamlit as st
import pandas as pd 


st.set_page_config(
    page_title="Stonks LLC",
    page_icon="💸",
)

# Create a page header
st.header("Welcome To The Future Of Investing")

col1, col2 = st.columns([1,1])

with col1:
    st.write("<a href= '/calculate_returns' > Predict The Company's Value", unsafe_allow_html=True)


with col2:

    st.image("StockData.png")