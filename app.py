import streamlit as st
import os
from PIL import Image

# Set page config FIRST
st.set_page_config(page_title="Architectural Studio", layout="wide")

from style import apply_custom_style
from contact import show_contact
from home import show_home

# Apply styling
apply_custom_style()

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Contact"])

# Route pages
if page == "Home":
    show_home()

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
            st.info("You have no images yet. Add project images to the 'projects/' folder.")
    else:
        st.info("Project gallery coming soon! Create a 'projects/' folder and add images when you're ready.")

elif page == "Contact":
    show_contact()
