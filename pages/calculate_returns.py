import streamlit as st
import pandas as pd
import pickle
import plotly.express as px



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
