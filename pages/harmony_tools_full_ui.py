
import streamlit as st

from streamlit_extras.switch_page_button import switch_page

if st.button("🏠 Home"):
    switch_page("app_ui_with_logo_and_nav")
# Set layout and page title
st.set_page_config(page_title="Harmony Tools", layout="centered")

# Centered logo and title
st.markdown("""
    <div style='text-align: center; margin-top: 10px; margin-bottom: 0px;'>
        <img src='https://raw.githubusercontent.com/openai/brandkit/main/logo/sw-me-logo.png' width='160'>
    </div>
    <h1 style='text-align:center; margin-top: 0;'>Harmony Tools</h1>
""", unsafe_allow_html=True)

# Custom styles
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
            width: 32px;
            height: 32px;
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
        .bottom-nav {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: #fff;
            border-top: 1px solid #ccc;
            display: flex;
            justify-content: space-around;
            padding: 10px 0;
        }
        .bottom-nav a {
            text-align: center;
            font-size: 14px;
            color: #333;
            text-decoration: none;
        }
        .bottom-nav img {
            width: 24px;
            height: 24px;
            display: block;
            margin: 0 auto 4px;
        }
    </style>
""", unsafe_allow_html=True)

# Tool options with icons
tools = [
    {"title": "Soft & Blended", "desc": "Colors that flow together smoothly", "icon": "https://img.icons8.com/color/48/paint-palette.png", "page": "soft_blended"},
    {"title": "Bold & Contrast", "desc": "Opposites that pop", "icon": "https://img.icons8.com/color/48/contrast.png", "page": "bold_contrast"},
    {"title": "Bright & Balanced", "desc": "Evenly spaced colors with strong energy", "icon": "https://img.icons8.com/color/48/rainbow.png", "page": "bright_balanced"},
    {"title": "Generate from Image", "desc": "Upload a photo and we'll do the rest", "icon": "https://img.icons8.com/color/48/camera--v1.png", "page": "from_image"},
    {"title": "Generate from Color Theory", "desc": "Let us create a harmonious palette for you", "icon": "https://img.icons8.com/color/48/idea.png", "page": "from_theory"}
]

# Render tool boxes
for tool in tools:
    st.markdown(f"""
        <div class='tool-box'>
            <img src='{tool['icon']}' class='tool-icon'/>
            <div class='tool-text'>
                <strong>{tool['title']}</strong><br>
                <span>{tool['desc']}</span>
            </div>
            <a class='tool-link' href='/{tool["page"]}'>→</a>
        </div>
    """, unsafe_allow_html=True)

# Bottom navigation bar
st.markdown("""
<div class='bottom-nav'>
    <a href='/'>
        <img src='https://img.icons8.com/ios-filled/50/000000/home.png'/>
        Home
    </a>
    <a href='/saved'>
        <img src='https://img.icons8.com/ios-filled/50/000000/folder-invoices.png'/>
        Saved
    </a>
    <a href='/create'>
        <img src='https://img.icons8.com/ios-filled/50/000000/edit.png'/>
        Create
    </a>
    <a href='/more'>
        <img src='https://img.icons8.com/ios-filled/50/000000/menu.png'/>
        More
    </a>
</div>
""", unsafe_allow_html=True)
