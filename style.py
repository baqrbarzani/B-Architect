import streamlit as st

def apply_custom_style():
    royal_oven = "#C1440E"  # Deep, warm orange-red (Royal Oven)

    st.markdown(f"""
        <style>
            /* Set main background and text color */
            body {{
                background-color: #ffffff;
                color: #000000;
            }}

            /* Customize headers */
            h1, h2, h3, h4 {{
                color: {royal_oven};
            }}

            /* Buttons */
            .stButton>button {{
                background-color: {royal_oven};
                color: white;
                border: none;
                border-radius: 8px;
                padding: 0.5em 1em;
                font-weight: bold;
            }}

            .stButton>button:hover {{
                background-color: #A03000;
            }}

            /* Sidebar */
            .css-1d391kg {{" /* Streamlit sidebar class (may change over time) */
                background-color: #fff3ed;
            }}

            /* Links */
            a {{
                color: {royal_oven};
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
        </style>
    """, unsafe_allow_html=True)
