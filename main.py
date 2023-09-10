# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st

st.title( "Registration Form" )
with st.form( "form" ):
    name = st.text_input( "Enter your Name : " )
    gender = st.selectbox( "Gender", [ 'Male', 'Female', 'Others' ] )
    age = st.text_input("What is your age : ")
    hobby = st.selectbox("Hobbies",['Programming', 'Singing', 'Dancing', 'Reading', 'Writing', 'Reel Making', 'Outgoing'])
    button = st.form_submit_button( "Done" )

if button :
    st.markdown("Name: {}, Gender: {}, Age {}, Hobby {}".format(name, gender, age, hobby))
