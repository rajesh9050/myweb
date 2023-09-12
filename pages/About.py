import streamlit as st
from PIL import Image
st.set_page_config(
    page_title="About",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.sidebar.header("About")

st.title("Rajesh Chouhan")
image = Image.open('aboutphoto.jpg')
st.image(image)
# st.image("/home/rajesh/PycharmProjects/myweb/pages/aboutphoto.jpg",)
st.markdown("M.Sc. Computer Science (Software)")
st.markdown("Web Development, Software Development, App Development")
st.markdown("Computer Languages: C, C++, C#, Java, Python, etc.")
