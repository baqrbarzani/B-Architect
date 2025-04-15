import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        /* Overall background and font */
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f4f1ee;  /* Soft warm beige */
            color: #2a2a2a;  /* Clean dark gray text */
            font-size: 16px;
            line-height: 1.7;
        }

        .stApp {
            background-color: #fefefe;
            padding: 1.5rem;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #f3ede9 !important;
            color: #2a2a2a;
            border-right: 1px solid #dcd3ca;
        }

        /* Headings */
        h1, h2, h3 {
            font-weight: 700;
            color: #1e1e1e;
            letter-spacing: 0.5px;
            margin-top: 1rem;
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

        /* Paragraphs and markdown text */
        .markdown-text-container {
            font-size: 1.05rem;
            color: #3c3c3c;
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
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.12);
        }

        .stButton>button:hover {
            background-color: #3e2b1e !important;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }

        /* Input fields and text area */
        input, textarea {
            background-color: #fff !important;
            border-radius: 8px !important;
            border: 1px solid #ccc !important;
            padding: 0.5rem !important;
            font-size: 1rem !important;
            color: #2a2a2a !important;
        }

        /* Image styling */
        img {
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }

        /* Block spacing */
        .element-container {
            margin-bottom: 1.5rem;
        }
        </style>
    """, unsafe_allow_html=True)
