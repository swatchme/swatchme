
import streamlit as st

# Set page config
st.set_page_config(page_title="Swatch Me Home", layout="centered")
from utils import display_logo_centered

display_logo_centered("swatchme_logo.png", width=300)
# Centered logo
import streamlit as st
st.markdown("<h2 style='text-align: center;'>My Palettes</h2>", unsafe_allow_html=True)
# Demo palette data
palettes = [
    {
        "title": "Spring Fling",
        "colors": ["#4DA5A7", "#FEC04F", "#FEC04F", "#4DA5A7"],
        "codes": ["GY6", "Y120", "Y120", "P3"]
    },
    {
        "title": "Sunny Day",
        "colors": ["#AFB2EB", "#FEC04F", "#FFA07A", "#FF7F73"],
        "codes": ["Y2", "PB8", "YO2", "Coral Blush"]
    }
]

for palette in palettes:
    swatches = ''.join([f"<div style='width:20px;height:20px;background-color:{c};border-radius:4px;margin:2px;display:inline-block;'></div>" for c in palette["colors"]])
    codes = " ".join(palette["codes"])
    st.markdown(f"""
<div style='border:1px solid #DDD;padding:15px;border-radius:12px;margin-bottom:16px;'>
    <div style='font-weight:600;font-size:16px;margin-bottom:6px;'>{palette["title"]}</div>
    <div style='margin-bottom:6px;'>{swatches}</div>
    <div style='font-size:13px;color:#444;'>{codes}</div>
</div>
""", unsafe_allow_html=True)

# Create Palette button
st.markdown("""<a href="/create_palette" target="_self">
    <div style="
        background-color: #FF7F73;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 24px;
        position: fixed;
        bottom: 80px;
        right: 30px;
        z-index: 100;
        text-align: center;
        width: fit-content;
    ">
        ➕ Create Palette
    </div>
</a>
""", unsafe_allow_html=True)
# Bottom navigation bar
st.markdown("""
<style>
.navbar {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    height: 60px;
    background: #F8F8F8;
    border-top: 1px solid #E0E0E0;
    display: flex;
    justify-content: space-around;
    align-items: center;
    z-index: 9999;
}
.navbar img {
    height: 28px;
}
.navbar div {
    font-size: 12px;
    color: #222;
    text-align: center;
}
</style>
<div class='navbar'>
    <a href="/app_ui_with_logo_and_nav" target="_self" style="text-decoration: none;">
        <div><img src='https://cdn-icons-png.flaticon.com/512/1946/1946436.png' width='28'><br>Home</div>
    </a>
    <a href="/saved_palettes" target="_self" style="text-decoration: none;">
        <div><img src='https://cdn-icons-png.flaticon.com/512/716/716784.png' width='28'><br>Saved</div>
    </a>
    <a href="/create_palette" target="_self" style="text-decoration: none;">
        <div><img src='https://cdn-icons-png.flaticon.com/512/1827/1827933.png' width='28'><br>Create</div>
    </a>
    <a href="/more" target="_self" style="text-decoration: none;">
        <div><img src='https://cdn-icons-png.flaticon.com/512/1828/1828859.png' width='28'><br>More</div>
    </a>
</div>
""", unsafe_allow_html=True)
