import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        /* Background image */
        .stApp {
            background-image: url("projects/Baqrbarzani.jpg");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            position: relative;
            z-index: 1;
            color: #f0f0f0;
        }

        /* Dark overlay for readability */
        .stApp::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            height: 100%;
            width: 100%;
            background: rgba(0, 0, 0, 0.7);  /* 70% dark overlay */
            z-index: -1;
        }

        /* Base layout and fonts */
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
            font-size: 16px;
            line-height: 1.7;
            color: #f0f0f0;
        }

        /* Sidebar */
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

        /* Markdown content */
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

        /* Inputs and textareas */
        input, textarea {
            background-color: #2a2a2a !important;
            color: #f0f0f0 !important;
            border-radius: 8px !important;
            border: 1px solid #444 !important;
            padding: 0.5rem !important;
        }

        /* Image elements */
        img {
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }

        .element-container {
            margin-bottom: 1.5rem;
        }
        </style>
    """, unsafe_allow_html=True)
