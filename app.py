import streamlit as st
import os
from PIL import Image

from style import apply_custom_style
from contact import show_contact

# Apply custom theme styling
apply_custom_style()

# Set page configuration
st.set_page_config(page_title="Architectural Studio", layout="wide")

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Contact"])

# --- Home Page ---
if page == "Home":
    st.title("Welcome to Our Architectural Studio 🏛️")
    st.markdown("""
    We design spaces that inspire.  
    Our architectural studio specializes in modern, sustainable, and functional design for residential, commercial, and public spaces.
    """)

    if os.path.exists("cover.jpg"):
        st.image("cover.jpg", use_column_width=True, caption="Our recent project")
    else:
        st.warning("Add a 'cover.jpg' image in your project folder to display here.")

# --- Projects Page ---
elif page == "Projects":
    st.title("Our Projects 🏗️")

    project_folder = "projects"
    if os.path.exists(project_folder):
        images = [img for img in os.listdir(project_folder) if img.lower().endswith((".png", ".jpg", ".jpeg"))]
        
        if images:
            cols = st.columns(3)
            for idx, img in enumerate(images):
                with cols[idx % 3]:
                    image_path = os.path.join(project_folder, img)
                    st.image(image_path, caption=img.replace("_", " ").split(".")[0], use_column_width=True)
        else:
            st.info("No images found in the 'projects' folder.")
    else:
        st.warning("No 'projects' folder found. Create one and add your project images.")

# --- Contact Page ---
elif page == "Contact":
    show_contact()
