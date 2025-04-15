import streamlit as st
from style import apply_custom_style

def show_contact():
    apply_custom_style()

    st.title("Contact Us")

    st.markdown("### Get in touch with us for your next project.")

    st.markdown("""
    **Email:** baqr00934879@gmail.com  
    **Phone:** +964 750 857 8727  
    **Location:** Barzan, Erbil, Iraq
    """)

    st.markdown("### Our Location")
    st.image("projects/location.jpg", caption="Barzan, Erbil, Iraq", use_container_width=True)
