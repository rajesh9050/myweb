# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sqlite3
import streamlit as st
# Create a function that connect to database
def create_database():
    conn = sqlite3.connect('registration.db')
    c = conn.cursor()
    c.execute("""
    SELECT name FROM sqlite_master WHERE type='table' AND name='name'
     """)
    if not c.fetchone():
        c.execute('''CREATE TABLE IF NOT EXISTS registration(name text, gender text, age text, hobby text)''')
        conn.commit()
    conn.close()
# Create a function that add record in database
def add_record(name, gender, age, hobby):
    conn = sqlite3.connect('registration.db')
    c = conn.cursor()
    c.execute("INSERT INTO registration VALUES(?,?,?,?)", (name, gender, age, hobby))
    conn.commit()
    conn.close()

def main():
    # Set page preferences
    st.set_page_config(
        page_title="Registration Form",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    # Set sidebar values
    st.sidebar.header("Registration Page")
    st.title("Registration Form")
    create_database()
    # use values in form and submit them
    with st.form("form",clear_on_submit=True):
        name = st.text_input("Enter your Name : ")
        gender = st.selectbox("Gender", ['Male', 'Female', 'Others'])
        age = st.text_input("What is your age : ")
        hobby = st.selectbox("Hobbies", ['Programming', 'Singing', 'Dancing', 'Reading', 'Writing', 'Reel Making', 'Outgoing'])
        button = st.form_submit_button("Done")
    # if button clicked write the values to our database record
    if button:
        add_record(name, gender, age, hobby)
        # print the values on screen and a thanks message to the user
        st.markdown("Name: {}, Gender: {}, Age {}, Hobby {}".format(name, gender, age, hobby))
        st.write("Thank you! for your registration.")

if __name__ == '__main__':
    main()
