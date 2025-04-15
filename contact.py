import streamlit as st

def show_contact():
    st.title("Contact Us")
    st.markdown("We're excited to hear from you! Feel free to reach out.")

    st.markdown("""
        **Email:** baqr00934879@gmail.com  
        **Phone:** +964 750 857 8727  
        **Location:** Barzan, Erbil, Iraq
    """)

    with st.form(key='contact_form'):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        if st.form_submit_button("Send"):
            st.success("Thank you! Your message has been sent.")
