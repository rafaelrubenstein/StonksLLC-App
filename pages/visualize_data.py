import streamlit as st
import matplotlib.pyplot as plt 
import yfinance as yf
import pandas as pd 
import numpy as np
import plotly.express as px



st.set_page_config(
    page_title="Visualize Data",
    page_icon="💸",
    initial_sidebar_state="collapsed",
    layout = "centered",
)

with open("styles.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    
# navbar
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #04AA6D;">
  <a class="navbar-brand" href="https://stonksllc.streamlit.app" target= "_self">Stonks LLC</a>
   <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/" target= "_self">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/calculate_returns" target= "_self" >Predict Company's Value</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/visualize_data" target= "_self">Visualize Stock Data</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/about_us" target= "_self"> About Us</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="contact" target= "_self">Contact us</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


def compare_two_stocks(stock1,stock2):
  stock1 = stock1.upper()
  stock2 = stock2.upper()
  two_stock_data = yf.download (tickers = stock1 +" " +stock2,
                              period = "5y", #The starting date of our data set
                              interval = "1mo",  
                              group_by = 'ticker', 
                              auto_adjust = True, #Automatically adjuss the closing prices for each period. 
                              treads = True) #Whether to use threads for mass downloading. 
  df_comp = two_stock_data
  df = pd.DataFrame()
  df[stock1] = df_comp[stock1].Close
  df[stock2] = df_comp[stock2].Close
  df[stock1 + ' Monthly Return'] = df[stock1].pct_change(1)
  df[stock2 + ' Monthly Return'] = df[stock2].pct_change(1)
  df[stock1 +' Monthly Cumulative Return'] = np.exp((np.log1p(df[stock1 +' Monthly Return']).cumsum()))
  df[stock2 +' Monthly Cumulative Return'] = np.exp((np.log1p(df[stock2 +' Monthly Return']).cumsum()))
  return df

def plot_monthly(df):
  df = df.iloc[1: , 2:4].apply(lambda x: x * 100)
  fig = px.line(df)
  fig.update_layout(
  title= "Monthly Return",
  xaxis_title="Date",
  yaxis_title="Percent Change",
  legend_title="Stock Ticker")
  st.plotly_chart(fig,use_container_width=True)
  
def plot_cum_monthly_return(df):
  df = df.iloc[1: , 4:6].apply(lambda x: x * 100)
  fig = px.line(df)
  fig.update_layout(
  title= "Cumulative Monthly Return",
  xaxis_title="Date",
  yaxis_title="Percent Change",
  legend_title="Stock Ticker")
  st.plotly_chart(fig,use_container_width=True)

def plot_cum_yearly_return(df,stock1,stock2):
  stock1 = stock1.upper()
  stock2 = stock2.upper()
  df = df.iloc[1::12, :2]
  df[stock1 + ' Yearly Return'] = df[stock1].pct_change(1)
  df[stock2 + ' Yearly Return'] = df[stock2].pct_change(1)
  df[stock1 +' Yearly Cumulative Return'] = np.exp((np.log1p(df[stock1 +' Yearly Return']).cumsum()))
  df[stock2 +' Yearly Cumulative Return'] = np.exp((np.log1p(df[stock2 +' Yearly Return']).cumsum()))
  df = df.iloc[1: , 4:6].apply(lambda x: x * 100)
  fig = px.bar(df)
  fig.update_layout(
  title= "Cumulative Yearly Return",
  xaxis_title="Date",
  yaxis_title="Percent Change",
  legend_title="Stock Ticker")
  st.plotly_chart(fig,use_container_width=True)

def plot_yearly_return(df,stock1,stock2):
  stock1 = stock1.upper()
  stock2 = stock2.upper()
  df = df.iloc[1::12, :2]
  df[stock1 + ' Yearly Return'] = df[stock1].pct_change(1)
  df[stock2 + ' Yearly Return'] = df[stock2].pct_change(1)
  df[stock1 +' Yearly Cumulative Return'] = np.exp((np.log1p(df[stock1 +' Yearly Return']).cumsum()))
  df[stock2 +' Yearly Cumulative Return'] = np.exp((np.log1p(df[stock2 +' Yearly Return']).cumsum()))
  df = df.iloc[1: , 2:4].apply(lambda x: x * 100)
  fig = px.bar(df)
  fig.update_layout(
  title= "Yearly Return",
  xaxis_title="Date",
  yaxis_title="Percent Change",
  legend_title="Stock Ticker")
  st.plotly_chart(fig,use_container_width=True)

st.write("I would like to compare the returns of")

ticker1 = st.text_input("ex. 'aapl' or 'amzn","aapl",key =1)

st.write("with")

ticker2 = st.text_input("","amzn",key =2)

df = compare_two_stocks(ticker1,ticker2)

option = st.radio("",('Visualize Monthly Return Of Last Five Years','Visualize Cumulative Return Of Last Five Years','Visualize Yearly Return Of Last Five Years','Visualize Cumulative Yearly Return Of Last Five Years'))

if option == 'Visualize Monthly Return Of Last Five Years':
  plot_monthly(df)
if option == 'Visualize Cumulative Return Of Last Five Years':
  plot_cum_monthly_return(df)
if option == 'Visualize Yearly Return Of Last Five Years':
  plot_yearly_return(df,ticker1,ticker2)
if option == 'Visualize Cumulative Yearly Return Of Last Five Years':
  plot_cum_yearly_return(df,ticker1,ticker2)