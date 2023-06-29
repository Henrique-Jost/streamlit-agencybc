import streamlit as st

st.header("Dados")

tab1, tab2, tab3, tab4 = st.tabs(["SEO", "Web Analytics", "Google Ads", "Facebook Ads"])

with tab1:
   st.header("SEO")

with tab2:
   st.header("Web Analytics")

with tab3:
   st.header("Google Ads")

with tab4:
   st.header("Facebook Ads")