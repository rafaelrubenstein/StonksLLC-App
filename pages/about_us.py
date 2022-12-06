import streamlit as st

st.set_page_config(
    page_title="About us",
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

col1,col2,col3 = st.columns(3)

with col1:
  st.title("Rafael Rubenstein")
  st.image("pages/rafael.jpg")
  st.write("""Rafael Graduated Brooklyn College with a B.S in Computer science. 
  He is currently pursuing his Masters In Computer Science-Concentration in Data Science from University Of
  Illinoi Urabna-Champaign.
  
  He has a passion for finance and healthcare. He spends his free time working out, reading, playing video games, 
  and watching Anime.""")

with col2:
  st.title("Yaakov Goffstein")
  st.image("pages/yaakov.jpeg")
  st.write("""FILL IN INFO """)

with col3:
  st.title("Nguyen Than")
  st.image("pages/stockprices.jpg")
  st.write("""FILL IN INFO """)