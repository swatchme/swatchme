import streamlit as st
from utils import display_logo_centered
display_logo_centered("swatchme_logo.png", width=300)
# Page title
st.markdown("<h1 style='text-align: center;'>Harmony Tools</h1>", unsafe_allow_html=True)

# Custom styling
st.markdown("""
    <style>
        .tool-box {
            border: 1px solid #e8e8e8;
            border-radius: 14px;
            padding: 18px 22px;
            margin-bottom: 18px;
            display: flex;
            align-items: center;
            transition: all 0.2s ease;
        }
        .tool-box:hover {
            background-color: #f9f9f9;
        }
        .tool-icon {
            font-size: 28px;
            margin-right: 18px;
        }
        .tool-text strong {
            font-size: 18px;
        }
        .tool-text span {
            font-size: 14px;
            color: #666;
        }
        .tool-link {
            margin-left: auto;
            font-size: 20px;
            text-decoration: none;
            color: #555;
        }
    </style>
""", unsafe_allow_html=True)

# Tool options
tools = [
    {"title": "Soft & Blended", "desc": "Colors that flow together smoothly", "emoji": "🟢", "page": "soft_blended"},
    {"title": "Bold & Contrast", "desc": "Opposites that pop", "emoji": "🔴", "page": "bold_contrast"},
    {"title": "Bright & Balanced", "desc": "Evenly spaced colors with strong energy", "emoji": "🌈", "page": "bright_balanced"},
    {"title": "Generate from Image", "desc": "Upload a photo and we'll do the rest", "emoji": "📷", "page": "from_image"},
    {"title": "Generate from Color Theory", "desc": "Let us create a harmonious palette for you", "emoji": "🧠", "page": "from_theory"}
]

# Display each tool
for tool in tools:
    st.markdown(f"""
        <div class='tool-box'>
            <div class='tool-icon'>{tool['emoji']}</div>
            <div class='tool-text'>
                <strong>{tool['title']}</strong><br>
                <span>{tool['desc']}</span>
            </div>
        </div>
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
