import streamlit as st

def footer_home():

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:white;"> Created with ❤️ by </p>
        <span style="font-weight:bold; color:#E0E3FF; font-size:1rem;">Mahboob Alam</span>
        </div>
                """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown(
        """
        <div style='text-align: center; padding: 10px; font-weight: bold;'>
            Created with ❤️ by <span style='color: Black;'>Mahboob Alam</span>
        </div>
        """,
        unsafe_allow_html=True
    )