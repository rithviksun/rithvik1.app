import streamlit as st
import requests
from gtts import gTTS
from io import BytesIO

st.set_page_config(page_title="Ai Weather Bot", page_icon="⛅")

st.title("⛅ Ai Weather Bot")
st.write("Enter any city and get live weather + AI advice")


@st.cache_data
def get_city(city: str):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    data = requests.get(url, timeout=10).json()
    if "results" in data and data["results"]:
        return data["results"][0]
    return None


@st.cache_data
def get_weather(lat: float, lon: float):
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        "&current=temperature_2m,weathercode,windspeed_10m"
        "&daily=precipitation_probability_max"
    )
    return requests.get(url, timeout=10).json()


def advice(temp: float, rain: float) -> str:
    if temp > 30:
        return "It is hot today. Drink water and stay cool."
    if temp < 10:
        return "It is cold today. Wear warm clothes."
    if rain > 50:
        return "It is likely to rain today. Carry an umbrella."
    return "The weather is moderate today. Enjoy your day!"


def speak(text: str):
    audio = BytesIO()
    tts = gTTS(text=text, lang="en")
    tts.write_to_fp(audio)
    return audio


city = st.text_input("Enter city:", "New York")

if st.button("Check Weather"):
    place = get_city(city)
    if not place:
        st.error("City not found.")
        st.stop()

    lat = place["latitude"]
    lon = place["longitude"]
    weather = get_weather(lat, lon)

    temp_c = weather["current"]["temperature_2m"]
    temp_f = round((temp_c * 9 / 5) + 32, 1)
    wind = weather["current"]["windspeed_10m"]
    rain = weather["daily"]["precipitation_probability_max"][0]

    msg = advice(temp_c, rain)
    st.success(
        f"""
        {city}
        Temperature: {temp_c}°C / {temp_f}°F
        Wind Speed: {wind} km/h
        Rain Probability: {rain}%
        Advice: {msg}
        """
    )

    speech = f"""
    The temperature in {city} is {temp_c} degrees Celsius, which is {temp_f} degrees Fahrenheit.
    The wind speed is {wind} kilometers per hour,
    and the probability of rain is {rain} percent. Advice: {msg}
    """
    audio = speak(speech)
    st.audio(audio, format="audio/mp3")
