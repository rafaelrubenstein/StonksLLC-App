import streamlit as st
import matplotlib.pyplot as plt 
import yfinance as yf
import pandas as pd 
import numpy as np



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

def get_index_prices(index1,index2,index3,index4,index5):
  #  this may not be needed but would be used to set the end date
  # date = (datetime.datetime.today()- timedelta(days = 1)).date().isoformat()
  date_5_years_ago = (datetime.datetime.today()- timedelta(days = 1825)).date().isoformat()
  indexfunds = index1 + " " + index2 + " " + index3 + " " + index4 + " " + index5
  raw_data = yf.download (tickers = indexfunds,
                              start = date_5_years_ago, #The starting date of our data set
                              interval = "1mo",  
                              group_by = 'ticker', 
                              auto_adjust = True, #Automatically adjuss the closing prices for each period. 
                              treads = True) #Whether to use threads for mass downloading. 
  
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
  df[stock1 + ' return'] = df[stock1].pct_change(1)
  df[stock2 + ' return'] = df[stock2].pct_change(1)
  df[stock1 +' cumulative return'] = np.exp(np.log1p(df[stock1 +' return']).cumsum())
  df[stock2 +' cumulative return'] = np.exp(np.log1p(df[stock2 +' return']).cumsum())
  return df

def plot_monthly(df):
  df = df.iloc[: , 2:4]
  st.line_chart(df)
  
def plot_cum_return(df):
  df = df.iloc[: , 4:6]
  st.line_chart(df)

st.write("Please enter the first Ticker of the company you would like to compare visually")

ticker1 = st.text_input("Ticker for company an example is the apple ticker","aapl",key =1)

st.write("Please enter the second Ticker of the company you would like to compare visually")

ticker2 = st.text_input("Ticker for company an example is the amazon ticker","amzn",key =2)

df = compare_two_stocks(ticker1,ticker2)

option = st.radio("Choose a Visual",('Visualize Monthly Return of last five years','Visualize Cumulative Return of last five years'))

if option == 'Visualize Monthly Return of last five years':
  plot_monthly(df)
if option == 'Visualize Cumulative Return of last five years':
  plot_cum_return(df)