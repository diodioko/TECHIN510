import streamlit as st
from annotated_text import annotated_text

st.title('👋🏻 Hi!This is Jiayi')
st.title('_A UX/Prodcut Designer base in Seattle_')


col1, col2 = st.columns(2)

with col1:
   st.header("")
   st.image('./images/profile3.png')

with col2:
   st.header("")



annotated_text(
    "This is",
    ("Jiayi", "", "#8ef"),
    ", ",
    " a ",
    ("dynamic problem solver", "", "#faa"),
    " with ",
    ("4-year", "", "#afa"),
    " working experience in design fields ",
    ". ",
    "Experience in",
    ("UX/Product design", "", "#fea"),
    " across ",
    ("Mobile, Web, and HMI ", "", "#faa"),
    "interfaces",
    ". ",
    "Passionate about improving life through innovative design, bridging ",
    ("creativity ", "", "#afa"),
    "and ",
    ("functionality", "", "#fea"),
    ". ",

)

st.header('Education', divider='rainbow')

multi = '''University of Washington, September 2023 - June 2025

Royal Danish Academy, September 2019 - June 2021

Shanghai Institute of Technology, September 2013 - June 2017
'''
st.markdown(multi)



st.header('Work Experience', divider='rainbow')

multi = '''Product Designer, August 2023 - February 2024

UX Design Intern, April 2023 - August 2023

UI/UX Designer, July 2022 - October 2022

Interior Designer, October 2021 - October 2022

Assistant Designer, July 2017 - July 2019
'''
st.markdown(multi)


st.header('Hobbies and Interests', divider='rainbow')

col1, col2 = st.columns(2)

with col1:
   st.header("Ceramic")
   st.image('./images/ceramic copy.jpg')

with col2:
   st.header("Music")
   st.image('./images/music2.png')



st.header('Projects', divider='rainbow')

st.markdown(
    """

- [Intelligent Parking Experience for EV Drivers](https://www.jiayi-xia.com/hmi)
- [Safe&Quick onboarding @ Sanctify](https://www.jiayi-xia.com/fintech)
- [Multi-platform Livechat @Ford](https://www.jiayi-xia.com/ford)
"""
)
