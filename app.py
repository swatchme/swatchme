import streamlit as st

st.set_page_config(page_title="Swatch Me", layout="centered")

# Redirect to the real homepage in pages/
st.markdown("""
    <meta http-equiv="refresh" content="0; url=/app_ui_with_logo_and_nav" />
    <p>Redirecting to home...</p>
""", unsafe_allow_html=True)
