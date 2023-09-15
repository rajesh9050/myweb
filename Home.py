import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Rajesh Chouhan",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.header("Home Page")
st.title("Rajesh Chouhan")
image = Image.open('myphoto.webp')
st.image(image, caption="Rajesh Chouhan", width=225)
st.markdown("To know more click on about page")
