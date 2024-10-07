import streamlit as st
import csv
import pandas as pd

topics = []

topic_file = pd.read_csv('topics.csv')
file_reader = csv.reader(topic_file)
for topic in topic_file['topic']:
    topics.append(topic)
topics = tuple(topics)
    


st.header("Contact Us")

with st.form(key='email_form'):
    usermail = st.text_input("Your Email Address")
    topic = st.selectbox(
        "What topic do you want to discuss",
        topics
    )
    text = st.text_area("Text")
    submit_bt = st.form_submit_button("Submit")
    if submit_bt:
        st.info("Your Email was sent successfully")