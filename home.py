import streamlit as st
from style import apply_custom_style

def show_home():
    apply_custom_style()
    
    st.title("Welcome to Our Architectural Studio")
    st.markdown("### Creating space with vision and passion.")

    st.image("projects/barzani.jpg", use_container_width=True)

    st.markdown("""
        At our architectural office, we believe in design that blends creativity with function. 
        We specialize in modern residential, commercial, and urban projects tailored to each client's needs. 
        
        Explore our work and get in touch — let's build something beautiful together.
    """)
