import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        /* Set background image */
        .stApp {
            background-image: url("projects/Baqrbarzani.jpg");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: #f0f0f0;
            padding: 1.5rem;
        }

        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
            background-color: rgba(18, 18, 18, 0.85);  /* dark overlay */
            font-size: 16px;
            line-height: 1.7;
        }

        /* Add dark overlay */
        .stApp::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(18, 18, 18, 0.85);  /* Dark overlay on image */
            z-index: -1;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #191919 !important;
            color: #f0f0f0;
            border-right: 1px solid #2c2c2c;
        }

        h1, h2, h3 {
            color: #ffffff;
        }

        .markdown-text-container {
            font-size: 1.05rem;
            color: #dddddd;
        }

        .stButton>button {
            background-color: #523A28 !important;
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

        input, textarea {
            background-color: #2a2a2a !important;
            color: #f0f0f0 !important;
            border-radius: 8px !important;
            border: 1px solid #444 !important;
            padding: 0.5rem !important;
        }

        img {
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }

        .element-container {
            margin-bottom: 1.5rem;
        }
        </style>
    """, unsafe_allow_html=True)
