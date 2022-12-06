import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.switch_page_button import switch_page
import pandas as pd 


st.set_page_config(
    page_title="Stonks LLC",
    page_icon="💸",
    initial_sidebar_state="collapsed",
    layout = "centered",
)
with open("styles.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# navbar
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://stonksllc.streamlit.app" target= "_self">Stonks LLC</a>
   <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="https://stonksllc.streamlit.app" target= "_self">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://stonksllc.streamlit.app/calculate_returns" target="_self" >Predict Company's Value</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://stonksllc.streamlit.app/visualize_data" target= "_self">Visualize Stock Data</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://stonksllc.streamlit.app/about_us" target= "_self"> About Us</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://stonksllc.streamlit.app/contact" target= "_self">Contact us</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

# Create a page header
st.header("Welcome To The Future Of Investing")

st.write("Click a Button Below To Get Started")
col1, col2 = st.columns([1,1])
col3, col4 = st.columns([1,1])

with col1:
    predict_stock = st.button("Predict A Company's Value")
    if predict_stock:
        switch_page("calculate_returns")

with col2:
    visualize = st.button("Visualize Stock Data")
    if visualize:
        switch_page("visualize_data")
        
with col3:
    aboutus = st.button("Find Out More About Us!")
    if aboutus:
        switch_page("about_us")
        
with col4:
    contact = st.button("Contact Us")
    if contact:
        switch_page("contact")

st.image("StockData.png",caption ="What Stock Data Looks Like")        

