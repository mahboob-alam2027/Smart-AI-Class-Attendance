import streamlit as st

from supabase import create_client, Client

supabase: Client = create_client(
    st.secrets["SUPABSE_URL"],
    st.secrets["SUPABSE_KEY"]
)