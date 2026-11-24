import streamlit as st

# Title of App
st.title("SkyWatch - Global Air Quality Intelligence")

# Assignment Data
# TODO: Fill out your team number, section, and team members

st.header("CS 1301")
st.subheader("Team 63, Web Development - Section D")
st.subheader("Sheikh Ibrahim Waqas, Shrihan Poddar")

# TODO (optional): Add a group photo to the images folder and show it here, for example:
# st.image("images/group_photo.jpg")


# Introduction
# TODO: Write a quick description for all of your pages in this lab below, in the form:
#       1. **Page Name**: Description
#       2. **Page Name**: Description
#       3. **Page Name**: Description

st.write("""
Welcome to SkyWatch! Our website helps users explore air
pollution across different cities and learn about air quality.

Use the sidebar to navigate between the following pages:

1. **SkyWatch:** Explore air pollution forecasts for different
cities and pollutants through interactive charts and statistics.

2. **SkyBot:** Chat with an AI assistant to learn about air
pollution, its causes and its environmental impacts.

3. **AI Agent:** An upcoming feature for Lab 4 that will allow
users to ask questions about actual air quality data.
""")

st.write("Data Source: Open-Meteo Air Quality API")
