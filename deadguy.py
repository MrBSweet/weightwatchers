import requests
import webbrowser
import streamlit as st
from datetime import datetime

def get_city_from_zip(zip_code):
    # Use the zippopotam.us API to convert ZIP code to city
    url = f'http://api.zippopotam.us/us/{zip_code}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        city = data['places'][0]['place name']
        return city
    else:
        return None

def search_obituary(name, city):
    current_year = datetime.now().year
    query = f"{name} {city} obituary {current_year}"
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

# Streamlit UI
st.title("Obituary Search Tool")

name = st.text_input("Enter the billing name:")
zip_code = st.text_input("Enter the billing ZIP code:")

if st.button("Search"):
    if name and zip_code:
        city = get_city_from_zip(zip_code)
        if city:
            st.write(f"Searching for obituaries for {name} in {city}...")
            search_obituary(name, city)
        else:
            st.error("Unable to find city for the provided ZIP code.")
    else:
        st.warning("Please enter both name and ZIP code.")
