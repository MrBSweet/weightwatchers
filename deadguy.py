import requests
import webbrowser
import streamlit as st
from datetime import datetime

def get_city_from_zip(zip_code):
    try:
        url = f'http://api.zippopotam.us/us/{zip_code}'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        city = data['places'][0]['place name']
        return city
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching city for ZIP code: {e}")
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
        st.write(f"Fetching city for ZIP code {zip_code}...")
        city = get_city_from_zip(zip_code)
        if city:
            st.write(f"Searching for obituaries for {name} in {city}...")
            search_obituary(name, city)
        else:
            st.error("Unable to find city for the provided ZIP code.")
    else:
        st.warning("Please enter both name and ZIP code.")
