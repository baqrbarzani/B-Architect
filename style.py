import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        html, body, [class*="css"]  {
            font-family: 'Segoe UI', sans-serif;
            color: #1c1c1e;
        }
        .stApp {
            background-color: #fff;
        }
        .css-1v3fvcr, .stButton>button {
            background-color: #523A28 !important; /* Royal Oven color */
            color: white !important;
            border-radius: 8px;
        }
        .stButton>button:hover {
            background-color: #3e2b1e !important;
        }
        </style>
    """, unsafe_allow_html=True)
