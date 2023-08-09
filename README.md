# Weather Forecast Web Application

## Overview

The Weather Forecast Web Application is a Streamlit-based project that allows users to retrieve weather forecasts for a specific location. By interacting with the interface, users can view temperature and sky condition data for the upcoming days.

## Features

- **Dynamic Visualization**: The application dynamically displays weather forecasts using interactive graphs and images.

- **User Input**: Users can input the desired location and number of forecast days, along with the option to view temperature or sky conditions.

- **Data Fetching**: The backend (`backend.py`) interacts with the OpenWeatherMap API to fetch weather data.

## File Structure

- `main.py`: The main application file built with Streamlit. It includes user input components and graph/image visualization based on the selected options.

- `backend.py`: The backend logic that fetches weather data from the OpenWeatherMap API based on user input.

- `images/`: Contains images related to different sky conditions.

## How to Run

1. Install the required dependencies using `pip install streamlit plotly requests`.

2. Run the Streamlit app: `streamlit run main.py`.

3. Access the application in your web browser at `http://localhost:8501`.

4. Enter a location, select the forecast days and data type, and observe the weather visualization.

## Dependencies

- Python 3.x
- Streamlit
- Plotly Express
- Requests

## Notes

- Ensure you have an API key from OpenWeatherMap. Replace `API_KEY` in `backend.py` with your own API key.

- The `images/` directory should contain image files corresponding to different sky conditions.

- This project serves as an example of creating interactive web applications using Streamlit.

## Conclusion

Experience the Weather Forecast Web Application to view temperature and sky condition forecasts effortlessly. This project demonstrates the potential of combining APIs, data visualization, and user-friendly interfaces.

---