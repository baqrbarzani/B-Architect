import streamlit as st
import os

def show_home():
    st.title("Welcome to Our Architectural Studio 🏛️")
    st.markdown("""
    We design spaces that inspire.  
    Our architectural studio specializes in modern, sustainable, and functional design for residential, commercial, and public spaces.
    """)

    # Optional cover image
    if os.path.exists("cover.jpg"):
        st.image("cover.jpg", use_column_width=True, caption="Our recent project")
