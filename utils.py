import base64
import streamlit as st
from pathlib import Path

def load_logo_base64(filename="swatchme_logo.png"):
    """Load and encode logo as base64, from app root directory."""
    logo_path = Path(__file__).resolve().parent / filename
    with open(logo_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def display_logo_centered(filename="swatchme_logo.png", width=160):
    """Display the logo centered on the page."""
    logo_base64 = load_logo_base64(filename)
    st.markdown(
        f"""
        <div style='text-align: center; margin-top: 20px; margin-bottom: -10px;'>
            <img src='data:image/png;base64,{logo_base64}' width='{width}'/>
        </div>
        """,
        unsafe_allow_html=True
    )
