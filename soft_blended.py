import streamlit as st
from utils import display_logo_centered
import pandas as pd
import random

# Display logo
display_logo_centered("swatchme_logo.png", width=160)

st.markdown("<h1 style='text-align: center;'>Soft & Blended Palette</h1>", unsafe_allow_html=True)

# Load marker data
df = pd.read_csv("marker_data.csv")

# User selections
marker_set = st.selectbox("Choose a marker set", df["Set"].unique())
filtered_df = df[df["Set"] == marker_set]

num_colors = st.slider("Number of colors", 3, 10, 5)

if st.button("🎨 Generate Palette"):
    soft_palette = filtered_df.sample(n=num_colors)
    st.markdown("<div style='margin-top: 20px;'>", unsafe_allow_html=True)
    for _, row in soft_palette.iterrows():
        st.markdown(
            f"""
            <div style='display: inline-block; margin-right: 12px; text-align: center;'>
                <div style='width: 60px; height: 60px; border-radius: 12px; background-color: {row["Hex"]}; border: 1px solid #ccc;'></div>
                <div style='margin-top: 6px;'>{row["Code"]}</div>
            </div>
            """, unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)

st.button("🔄 Regenerate")
st.button("💾 Save")
st.button("📤 Share")

st.markdown("<p style='text-align: center; margin-top: 30px;'>This palette uses <strong>Analogous colors</strong><br>This reminds us of <em>“Country Garden”</em></p>", unsafe_allow_html=True)
