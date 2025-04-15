import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        /* Dark base theme */
        .stApp {
            background-color: #121212;
            position: relative;
            z-index: 1;
            color: #f0f0f0;
            padding: 1.5rem;
        }

        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
            font-size: 16px;
            line-height: 1.7;
            color: #f0f0f0;
            background-color: #121212;
        }

        /* Sidebar styling */
        section[data-testid="stSidebar"] {
            background-color: #191919 !important;
            color: #f0f0f0;
            border-right: 1px solid #2c2c2c;
        }

        /* Headings */
        h1, h2, h3 {
            font-weight: 700;
            color: #ffffff;
            letter-spacing: 0.5px;
        }

        h1 {
            font-size: 2.2rem;
        }

        h2 {
            font-size: 1.6rem;
        }

        h3 {
            font-size: 1.3rem;
        }

        /* Markdown and text */
        .markdown-text-container {
            font-size: 1.05rem;
            color: #dddddd;
        }

        /* Buttons */
        .stButton>button {
            background-color: #523A28 !important;  /* Royal Oven */
            color: white !important;
            border: none;
            border-radius: 8px;
            padding: 0.6rem 1.3rem;
            font-size: 1rem;
            font-weight: 500;
            transition: background-color 0.3s ease;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
        }

        .stButton>button:hover {
            background-color: #3e2b1e !important;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.6);
        }

        /* Input fields */
        input, textarea {
            background-color: #2a2a2a !important;
            color: #f0f0f0 !important;
            border-radius: 8px !important;
            border: 1px solid #444 !important;
            padding: 0.5rem !important;
        }

        /* Image styling */
        img {
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }

        .element-container {
            margin-bottom: 1.5rem;
        }
        </style>
    """, unsafe_allow_html=True)
