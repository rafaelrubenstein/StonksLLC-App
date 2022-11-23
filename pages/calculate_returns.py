import streamlit as st
import pandas as pd
import pickle
import plotly.express as px

with open("/styles.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    
# navbar
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://stonksllc.streamlit.app" target="_blank">Stonks LLC</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/calculate_returns">Predict Company's Value</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/visualize_data">Visualize Stock Data</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/about_us"> About Us</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="contact">Contact us</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)



knclass = pickle.load(open("models/kneighborclass.pkl", 'rb'))


st.write("These numbers can be found on the company's balance sheet, if a company has 400,000,000 assets please enter as 400")

act = st.number_input("Enter the companys Total Current Assets",key=1)

at = st.number_input("Enter the companys Total Current Assets",key=2)

che = st.number_input("Enter the companys Cash and short term investments",key=3)

dltt = st.number_input("Enter the companys Total Longterm Debt",key=4)

intan = st.number_input("Enter the companys Total Intangible assets",key=5)

lct = st.number_input("Enter the companys Total Current Liabilities",key=6)

lt = st.number_input("Enter the companys Total Liabilities",key=7)

rect = st.number_input("Enter the companys Total Recievables",key=8)

st.write("This can be found on the income statement")
spi = st.number_input("Enter the companys Special items",key=9)

mkvalt = st.number_input("Enter the companys Current Market value",key=10)

make_prediction = st.button("Predict if stock is undervalued")

to_predict = [act,at,che,dltt,intan,lct,lt,rect,spi,mkvalt]

if make_prediction:
    prediction = knclass.predict([to_predict])

    if prediction:
        st.write("The stock is undervalued! You should invest in it")
    else:
        st.write("This stock is not undervalued")
