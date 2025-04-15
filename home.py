import streamlit as st
import os

def show_home():
    # Banner Image
    banner_path = "projects/Architecture.jpg"
    if os.path.exists(banner_path):
        st.image(banner_path, use_container_width=True, caption="Timeless Architectural Vision")

    # Intro Text
    st.title("Welcome to Our Architectural Studio 🏛️")
    st.markdown("""
    We design spaces that inspire.  
    Our architectural studio specializes in modern, sustainable, and functional design for residential, commercial, and public spaces.
    """)
