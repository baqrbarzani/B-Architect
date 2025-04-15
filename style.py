import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        /* Global styling */
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f9f9f9;
            color: #1c1c1e;  /* Dark text */
            line-height: 1.6;
        }

        /* App background */
        .stApp {
            background-color: #ffffff;
            padding: 1rem;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #f3f3f3 !important;
            border-right: 1px solid #e0e0e0;
        }

        /* Title and headers */
        h1, h2, h3 {
            color: #2b2b2b;
        }

        /* Buttons */
        .stButton>button {
            background-color: #523A28 !important;  /* Royal Oven */
            color: white !important;
            border: none;
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
            font-size: 1rem;
            transition: background-color 0.3s ease;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }

        .stButton>button:hover {
            background-color: #3e2b1e !important;
            box-shadow: 0 3px 8px rgba(0,0,0,0.15);
        }

        /* Inputs & Text Area */
        input, textarea {
            border-radius: 8px !important;
            border: 1px solid #ccc !important;
            padding: 0.5rem !important;
            color: #1c1c1e !important;
            background-color: #fff !important;
        }

        /* Image style */
        img {
            border-radius: 8px;
        }

        /* Adjust spacing */
        .element-container {
            margin-bottom: 1.5rem;
        }
        </style>
    """, unsafe_allow_html=True)
