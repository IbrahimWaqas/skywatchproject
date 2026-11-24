# Lab 3: API data page
# TODO: Rename this file to fit your page. Keep the number at the front, since it sets the
#       page's order in the sidebar (for example, 2_Pokedex.py).
#
# This page shows data from your API, processed with your own Python code. No AI on this page.
# It should have:
#   - at least 2 meaningful user inputs (for example st.selectbox, st.text_input, st.slider)
#   - at least 2 dynamic visuals that change based on the user's input: charts, displays of
#     images, or other visualizations (see the example website for examples!)

import altair as alt
from datetime import datetime
import requests
import streamlit as st

st.title("SkyWatch")
st.subheader("Global Air Quality Intelligence")

st.write("Explore air pollution levels across the world.")

cities = {
    "Atlanta": (33.75, -84.39),
    "Lahore": (31.52, 74.36),
    "New York": (40.71, -74.01),
    "London": (51.51, -0.13),
    "Dubai": (25.20, 55.27),
    "Tokyo": (35.68, 139.69),
    "Beijing": (39.90, 116.41),
    "Paris": (48.86, 2.35),
    "Karachi": (24.86, 67.01),
    "New Delhi": (28.61, 77.21)
}

pollutants = {
    "PM2.5": "pm2_5",
    "PM10": "pm10",
    "Carbon Monoxide": "carbon_monoxide",
    "Nitrogen Dioxide": "nitrogen_dioxide",
    "Sulphur Dioxide": "sulphur_dioxide",
    "Ozone": "ozone"
}

city = st.selectbox("Select a city", list(cities.keys()))
pollutant = st.selectbox("Select a pollutant", list(pollutants.keys()))

latitude, longitude = cities[city]
pollutant_code = pollutants[pollutant]

url = "https://air-quality-api.open-meteo.com/v1/air-quality"

params = {
    "latitude": latitude,
    "longitude": longitude,
    "hourly": pollutant_code,
    "forecast_days": 5,
    "timezone": "auto"
}

response = requests.get(url, params=params)
data = response.json()

times = data["hourly"]["time"]
values = data["hourly"][pollutant_code]
unit = data["hourly_units"][pollutant_code]

valid_values = []

for value in values:
    if value is not None:
        valid_values.append(value)

if len(valid_values) == 0:
    st.error("No data available.")
    st.stop()

average = sum(valid_values) / len(valid_values)
minimum = min(valid_values)
maximum = max(valid_values)

st.header(f"Air Quality in {city}")
st.write(f"Pollutant: {pollutant}")
st.write(f"Unit: {unit}")

col1, col2, col3 = st.columns(3)

col1.metric("Average", round(average, 2))
col2.metric("Minimum", round(minimum, 2))
col3.metric("Maximum", round(maximum, 2))

daily_data = {}

for i in range(len(times)):
    date = datetime.fromisoformat(times[i]).strftime("%b %d")

    if values[i] is not None:
        if date not in daily_data:
            daily_data[date] = []

        daily_data[date].append(values[i])

dates = []
daily_averages = []
daily_maximums = []

for date in daily_data:
    readings = daily_data[date]

    dates.append(date)
    daily_averages.append(sum(readings) / len(readings))
    daily_maximums.append(max(readings))

st.subheader("Daily Maximum Pollution")

st.line_chart(
    {"Date": dates, "Maximum": daily_maximums},
    x="Date",
    y="Maximum"
)

st.subheader("Daily Average Pollution")

st.bar_chart(
    {"Date": dates, "Average": daily_averages},
    x="Date",
    y="Average"
)

st.caption("Data source: Open-Meteo and CAMS.")
st.caption("All readings are model-based forecasts.")