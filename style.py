import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        /* Global font and background */
        html, body, [class*="css"]  {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f9f9f9;
            color: #1c1c1e;
            line-height: 1.6;
        }

        /* App background */
        .stApp {
            background-color: #fdfdfd;
            padding: 1rem;
        }

        /* Sidebar styling */
        .css-1d391kg {
            background-color: #fff !important;
            border-right: 1px solid #e0e0e0;
        }

        /* Title and headers */
        h1, h2, h3 {
            color: #2e2e2e;
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
        }

        /* Image border radius */
        img {
            border-radius: 8px;
        }

        /* Spacing for images/cards */
        .element-container {
            margin-bottom: 1.5rem;
        }
        </style>
    """, unsafe_allow_html=True)
