import streamlit as st
from PIL import Image
import os

# Set page configuration
st.set_page_config(page_title="Architectural Studio", layout="wide")

# --- Sidebar ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Contact"])

# --- Home Page ---
if page == "Home":
    st.title("Welcome to Our Architectural Studio 🏛️")
    st.markdown("""
    We design spaces that inspire.  
    Our architectural studio specializes in modern, sustainable, and functional design for residential, commercial, and public spaces.
    """)

    st.image("cover.jpg", use_column_width=True, caption="Our recent project")

# --- Projects Page ---
elif page == "Projects":
    st.title("Our Projects 🏗️")

    project_folder = "projects"
    if os.path.exists(project_folder):
        images = [img for img in os.listdir(project_folder) if img.endswith((".png", ".jpg", ".jpeg"))]
        
        for img in images:
            image_path = os.path.join(project_folder, img)
            st.image(image_path, caption=img.replace("_", " ").split(".")[0], use_column_width=True)
    else:
        st.warning("No project folder found. Create a folder named 'projects' and add your images.")

# --- Contact Page ---
elif page == "Contact":
    st.title("Get in Touch 📬")

    st.markdown("""
    **Email:** contact@yourstudio.com  
    **Phone:** +1-234-567-890  
    **Instagram:** [@yourstudio](https://instagram.com/yourstudio)  
    **Location:** 123 Design St, Architecture City, Country
    """)

    st.text_input("Your Name")
    st.text_input("Your Email")
    st.text_area("Your Message")
    st.button("Send (non-functional placeholder)")

