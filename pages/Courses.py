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
st.markdown("Python")
st.markdown("JAVA")

choice = st.sidebar.selectbox("Courses", ["Python", "JAVA"])
if choice == "Python":
    st.subheader("Python")
elif choice == "JAVA":
    st.subheader("Java")
else:
    st.subheader("Select Course from Side Bar")


