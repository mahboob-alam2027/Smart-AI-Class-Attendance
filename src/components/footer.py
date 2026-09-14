import streamlit as st

def footer_home():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:white;"> Created with ❤️ by </p>
        <span style="font-weight:bold; color:#E0E3FF; font-size:1rem;">Mahboob Alam</span>
        </div>



                """, unsafe_allow_html=True)