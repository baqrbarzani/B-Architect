import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        /* Set background image with dark overlay */
        .stApp {
            background-image: url("projects/barzani.jpg");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            position: relative;
            color: #f0f0f0;
        }

        .stApp::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            height: 100%;
            width: 100%;
            background-color: rgba(0, 0, 0, 0.65); /* Dark overlay */
            z-index: -1;
        }

        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
            font-size: 16px;
            line-height: 1.6;
            color: #f0f0f0;
        }

        /* Sidebar styling */
        section[data-testid="stSidebar"] {
            background-color: #1e1e1e !important;
            color: #f0f0f0;
            border-right: 1px solid #333;
        }

        /* Headings */
        h1, h2, h3 {
            font-weight: 700;
            color: #ffffff;
            letter-spacing: 0.5px;
        }

        h1 { font-size: 2.2rem; }
        h2 { font-size: 1.6rem; }
        h3 { font-size: 1.3rem; }

        /* Markdown text */
        .markdown-text-container {
            font-size: 1.05rem;
            color: #dddddd;
        }

        /* Buttons */
        .stButton>button {
            background-color: #523A28 !important;
            color: white !important;
            border: none;
            border-radius: 8px;
            padding: 0.6rem 1.3rem;
            font-size: 1rem;
            font-weight: 500;
            transition: 0.3s ease;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.4);
        }

        .stButton>button:hover {
            background-color: #3e2b1e !important;
        }

        /* Inputs */
        input, textarea {
            background-color: #2a2a2a !important;
            color: #f0f0f0 !important;
            border-radius: 8px !important;
            border: 1px solid #444 !important;
            padding: 0.5rem !important;
        }

        /* Images inside content */
        img {
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }

        .element-container {
            margin-bottom: 1.5rem;
        }
        </style>
    """, unsafe_allow_html=True)
