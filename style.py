import streamlit as st

def apply_custom_style():
    st.markdown("""
        <style>
        /* Background image for all pages */
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
            background: rgba(0, 0, 0, 0.7);  /* 70% dark */
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
