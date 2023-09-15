import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(
    page_title="Courses",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.sidebar.header("Course Offered")
st.title("Courses")
components.html("<html><body><ul><li>Python</li><li>JAVA</li></ul></body></html>")


