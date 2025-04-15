import streamlit as st

def show_contact():
    st.title("Get in Touch 📬")

    st.markdown("""
    We'd love to hear from you!  
    Whether you're looking to start a new project, collaborate, or just say hi, feel free to reach out.
    """)

    st.markdown("""
    **📧 Email:** [baqr00934879@gmail.com](mailto:baqr00934879@gmail.com)  
    **📞 Phone:** +964 750 857 8727  
    **📍 Location:** Barzan, Erbil, Iraq  
    """)

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send (placeholder)"):
        st.success("Thanks! This is just a demo. In the real version, your message would be sent.")
