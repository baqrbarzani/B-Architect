import streamlit as st

def apply_custom_style():
    st.markdown(
        """
        <style>
        /* Set background image for the entire app */
        .stApp {
            background-image: url('projects/Baqrbarzani.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: white;
        }

        /* Optional: Add a dark overlay for readability */
        .stApp::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.6);
            z-index: -1;
        }

        /* General text styling for better readability */
        h1, h2, h3, h4, h5, h6, p, label, div {
            color: white !important;
        }

        .stButton > button {
            background-color: #556B8D;
            color: white;
            border-radius: 8px;
            padding: 0.5em 1em;
            border: none;
        }

        .stTextInput > div > div > input {
            background-color: #222;
            color: white;
            border-radius: 8px;
        }

        .stTextArea textarea {
            background-color: #222;
            color: white;
            border-radius: 8px;
        }

        .stImage img {
            border-radius: 16px;
            box-shadow: 0px 0px 12px rgba(0, 0, 0, 0.5);
        }
        </style>
        """, unsafe_allow_html=True
    )
