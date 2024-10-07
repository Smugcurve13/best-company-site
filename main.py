import streamlit as st
import pandas as pd

st.set_page_config(layout = 'wide')

st.title("The Best Company")
content = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed in mauris lectus. Vestibulum bibendum tellus nibh,
sit amet pulvinar justo ullamcorper ac. Mauris neque ligula, accumsan nec tincidunt sed, maximus sed magna. Duis 
vehicula, est non mollis ullamcorper, quam orci facilisis nibh, at egestas justo nulla nec elit. Sed ut porta nisl.
Vestibulum eget interdum leo. Nullam quis rhoncus tortor. Maecenas auctor volutpat quam, nec tristique mauris 
aliquam varius. Duis fermentum risus turpis, sed ornare dolor hendrerit eu.
'''
st.write(content)
st.header("Our Team")

col1,col2,col3 = st.columns(3)

df = pd.read_csv('data-best.csv')
with col1:
    for index,row in df[:4].iterrows():
        name = f"{row['first name']} {row['last name']}"
        st.subheader(name.title())
        st.write(row['role'])
        st.image("images-best/" + row['image'])

with col2:
    for index,row in df[4:8].iterrows():
        name = f"{row['first name']} {row['last name']}"
        st.subheader(name.title())
        st.write(row['role'])
        st.image("images-best/" + row['image'])

with col3:
    for index,row in df[8:12].iterrows():
        name = f"{row['first name']} {row['last name']}"
        st.subheader(name.title())
        st.write(row['role'])
        st.image("images-best/" + row['image'])





