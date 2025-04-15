import streamlit as st

def show_home():
    st.title("Welcome to B-Architect Studio")
    st.markdown("### Designing spaces that inspire.")

    st.image("projects/Architecture.jpg", use_container_width=True)

    st.markdown("""
        We are a passionate architectural office based in Erbil, Iraq. Our mission is to craft creative, sustainable, and people-focused spaces.

        **What we do:**
        - Architectural Design
        - Urban Planning
        - Interior Design
        - Concept Development

        Our work blends functionality, aesthetics, and innovation — tailored to every client.
    """)
