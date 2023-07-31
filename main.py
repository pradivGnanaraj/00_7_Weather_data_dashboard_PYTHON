import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, select box and sub header
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} in {place}")

# Fake data testing
# def get_data(days):
#     dates = ["2023-29-07", "2023-30-07", "2023-31-07"]
#     temperatures = [10, 11, 15]
#     temperatures = [days * i for i in temperatures]
#     return dates, temperatures

# data = get_data(place, days, option)
if place:
    # Get the temperature/sky data
    try:
        filtered_data = get_data(place, days)

        # Create a temperature plot
        if option == "Temperature":
            temperatures = filtered_data = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            # number of images euqls the number of conditions
            images = {"Clear" : "images/clear.png",
                      "Clouds" : "images/clouds.png",
                      "Rain" : "images/rain.png",
                      "Snow" : "images/snow.png"}
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
    except KeyError:
        st.write("Oops..! That place does not exist!")
