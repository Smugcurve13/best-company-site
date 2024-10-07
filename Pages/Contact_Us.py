import streamlit as st
import pandas as pd
from send_email import send_email

topics = []

topic_file = pd.read_csv('topics.csv')

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
    message = f'''\
Subject: New email from {usermail}

From: {usermail}
Topic: {topic}
{text}
'''
    submit_bt = st.form_submit_button("Submit")
    if submit_bt:
        send_email(message)
        st.info("Your Email was sent successfully")