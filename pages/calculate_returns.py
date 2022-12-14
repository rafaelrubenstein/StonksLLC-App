import streamlit as st
import pandas as pd
import pickle
import plotly.express as px
import yfinance as yf
from bs4 import BeautifulSoup
import requests
from sklearn.preprocessing import StandardScaler

st.set_page_config(
    page_title="Predict Undervalued",
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



model = pickle.load(open("models/model.pkl", 'rb'))
scaler = pickle.load(open("models/scaler.pkl", 'rb'))

def scrape_os_and_calulate_mkvalt(ticker):

    ticker = ticker.upper()
    msft = yf.Ticker(ticker)
    try: 
        scrape_url = 'https://finance.yahoo.com/quote'
        ticker_url = "{}/{}".format(scrape_url, ticker) +'/balance-sheet?p='+ ticker
        
        headers={'User-Agent': 'Custom'}

        response = requests.get(ticker_url,headers=headers )
      
        html = response.content
        soup = BeautifulSoup(html,"html.parser")
      
        ordinary_shares = soup.find(title = "Ordinary Shares Number")
        date = soup.find(class_='D(tbhg)').text
        if len(date) == 49:
            fyear_end_date = date[15:19] + "-" + date[9:11] + "-" + date[12:14]
        else:
            fyear_end_date = date[14:18] + "-" + date[9:10] + "-" + date[11:13]
      
        shares = []
        for i in ordinary_shares.parent.next_siblings:
            number = i.text.replace(",",'')
            shares.append(int(number))
      
        most_current_fyear_ordinary_shares = shares[0] / 100 
      
        j = msft.history(start = fyear_end_date)
        closing_price = j.Close.iloc[0]
        marketvalue = closing_price * most_current_fyear_ordinary_shares
        
    except:
        st.warning("The Ticker May be Delisted. Please check if the Ticker exists and make sure to enter correctly")
        st.stop()
    else:
        return [marketvalue, msft]


def clean_balance_sheet_for_feautures(msft, marketvalue):
    balanceSheet = msft.balance_sheet
    
    dict_index_needed = {'Intangible Assets':1 ,'Total Liab': 2,'Total Assets':3,'Cash':4,'Total Current Liabilities':5,
           'Total Current Assets':6,'Net Receivables':7,'Long Term Debt':8}
     
    index = balanceSheet.index.to_list()
    
    for i in range(len(index) - 1, -1, -1):
        if index[i] in dict_index_needed:
            index.pop(i)
        
    balanceSheet.drop(index = index, inplace = True)
    
    first_col = balanceSheet.columns[0]
    
    current_numbers_needed = balanceSheet[first_col]
    current_numbers_needed = current_numbers_needed.to_dict()
#     convert numbers to be in millions 
    for key in current_numbers_needed:
        current_numbers_needed[key] = current_numbers_needed[key] / 100000    
    current_numbers_needed["Market Value"] = marketvalue
# check to see that dict has every value and key needed for features 
    for key in dict_index_needed.keys():
        if key not in current_numbers_needed:
            current_numbers_needed[key] = 0
    return current_numbers_needed
# st.warning("We are aware of a bug right now that is affecting the financial data. We are working on getting that fixed")
st.info("Please keep In mind we are currently scraping the data so some tickers may not be available. We are working on getting a better API")
st.write("Please enter the Ticker of the company you would like to predict its value")

ticker = st.text_input("Ticker for company an example is the apple ticker","aapl")

market_value, msft = scrape_os_and_calulate_mkvalt(ticker)

financial_data = clean_balance_sheet_for_feautures(msft,market_value)


make_prediction = st.button("Predict if stock is undervalued")

if make_prediction:
    financial_data_df_to_predict = pd.DataFrame([financial_data])
    financial_data_df_to_predict = financial_data_df_to_predict.sort_index(axis= 1)
    to_predict_scaled = scaler.transform(financial_data_df_to_predict)
    prediction = model.predict(to_predict_scaled)

    if prediction:
        st.write("The stock is likely undervalued! You should invest in it!")
    else:
        st.write("This stock is not undervalued")

    st.text("These are the financial numbers that were used to predict the company's value")        
    financial_data_df = pd.DataFrame.from_dict(financial_data,orient="index")
    st.dataframe(financial_data_df)        
    st.caption("Numbers Above are in millions")
