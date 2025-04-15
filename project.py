import streamlit as st
import os

def show_projects():
    st.title("Our Projects")
    st.markdown("Explore some of our recent architectural designs.")

    project_folder = "projects"
    image_files = [f for f in os.listdir(project_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg')) and f != "Architecture.jpg"]

    cols = st.columns(3)
    for i, image in enumerate(image_files):
        with cols[i % 3]:
            st.image(os.path.join(project_folder, image), caption=image.split('.')[0], use_container_width=True)
