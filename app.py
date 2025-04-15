import streamlit as st
import os
from PIL import Image

# Set page config FIRST
st.set_page_config(page_title="Architectural Studio", layout="wide")

from style import apply_custom_style
from contact import show_contact
from home import show_home
from project import show_projects

# Apply styling
apply_custom_style()

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Contact"])

# Route pages
if page == "Home":
    show_home()

elif page == "Projects":
    show_projects()

elif page == "Contact":
    show_contact()
