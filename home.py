import streamlit as st
from style import apply_custom_style

def show_home():
    # Custom style for all pages
    apply_custom_style()

    # Add background image specifically for login area
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('projects/Baqrbarzani.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }

        .stApp::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.65); /* Dark overlay */
            z-index: -1;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Initialize login state
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    st.title("Architectural Studio Portal")

    if not st.session_state.logged_in:
        st.subheader("🔐 Please log in to continue")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username == "admin" and password == "pass123":
                st.session_state.logged_in = True
                st.success("✅ Logged in successfully!")
                st.rerun()
            else:
                st.error("❌ Invalid credentials.")
    else:
        st.success("👋 Welcome back!")
        st.image("projects/barzani.jpg", use_container_width=True)
        st.markdown("""
            ### Creating space with vision and passion.

            At our architectural office, we believe in design that blends creativity with function. 
            We specialize in modern residential, commercial, and urban projects tailored to each client's needs. 

            Explore our work and get in touch — let's build something beautiful together.
        """)

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()
