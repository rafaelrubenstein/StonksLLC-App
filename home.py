import streamlit as st
import streamlit.components.v1 as components
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
components.html("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
 <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
<nav class="navbar navbar-expand-lg bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="home">Stonks LLC</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <a class="nav-link active" aria-current="page" href="home">Home</a>
        <a class="nav-link" href="/calulate_returns">Predit Company's Value</a>
        <a class="nav-link" href="">About us</a>
        <a class="nav-link href="">Contact Us</a>
      </div>
    </div>
  </div>
</nav>
""")

# Create a page header
st.header("Welcome To The Future Of Investing")

col1, col2 = st.columns([1,1])

with col1:
    st.write("<a href= '/calculate_returns' > Predict The Company's Value", unsafe_allow_html=True)


with col2:

    st.image("StockData.png")

