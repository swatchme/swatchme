
import streamlit as st
from PIL import Image
import os

st.set_page_config(layout="centered", page_title="Swatch Me")

# Load UI mockup assets from a local folder
ui_dir = "ui_assets"
screens = {
    "Welcome": "2C78E8E2-D050-4419-8A72-0493B2101AD0.png",
    "Login": "F97B8B10-C445-4DFF-ACAA-FCE8C85C7A6A.png",
    "Pro Screen": "90AE9A48-7A5F-48B8-81E8-09E4E96D07AC.png",
    "Marker Set Picker": "069B1FA2-5DA9-40E0-B2AB-BB929FCCB8CA.png",
    "Harmony Tools": "FB770EE2-DD53-4A26-B0E5-7DECAE814A1F.png",
    "Soft & Blended": "E9BF887F-20CD-488B-99B8-FA58CF01AD65.png",
    "From Image": "8B01A569-5C62-40B1-9876-0292EE9F7E7C.png",
    "Image Result": "6BB602DA-A8F7-437D-BEE4-14774AAEE38C.png",
    "Saved Palettes": "7B6FA14C-5456-42B4-A168-FA36E0F7FF51.png",
    "Saved Palettes Alt": "71872EAD-AF8D-4980-9E27-D28D9FE525FD.png"
}

st.title("📱 Swatch Me Prototype")

choice = st.sidebar.selectbox("Choose a screen to preview", list(screens.keys()))

image_path = os.path.join(ui_dir, screens[choice])
image = Image.open(image_path)
st.image(image, use_column_width=True)
