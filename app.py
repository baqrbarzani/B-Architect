import streamlit as st
from home import show_home
from contact import show_contact
from project import show_projects
from style import apply_custom_style

st.set_page_config(page_title="B-Architect Studio", layout="wide")
apply_custom_style()

# Navigation
pages = {
    "Home": show_home,
    "Projects": show_projects,
    "Contact": show_contact
}

selected_page = st.sidebar.radio("Navigate", list(pages.keys()))
pages[selected_page]()
