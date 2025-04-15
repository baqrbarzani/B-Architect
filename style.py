import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        /* App background with image */
        .stApp {
            background-image: url("projects/Baqrbarzani.jpg");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            position: relative;
            z-index: 1;
            color: #f0f0f0;
        }

        /* Overlay for better readability */
        .stApp::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            height: 100%;
            width: 100%;
            background: rgba(0, 0, 0, 0.65);  /* dark overlay */
            z-index: -1;
        }

        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
            font-size: 16px;
            line-height: 1.7;
            color: #f0f0f0;
        }

        /* Sidebar */
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

        h1 {
            font-size: 2.2rem;
        }

        h2 {
            font-size: 1.6rem;
        }

        h3 {
            font-size: 1.3rem;
        }

        /* Text content */
