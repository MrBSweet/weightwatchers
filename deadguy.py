import requests
import webbrowser
from datetime import datetime

def get_city_from_zip(zip_code):
    # Replace 'your_api_key' with an actual API key from a service that provides ZIP code to city conversion
    api_key = 'your_api_key'
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

if __name__ == "__main__":
    name = input("Enter the billing name: ")
    zip_code = input("Enter the billing ZIP code: ")

    city = get_city_from_zip(zip_code)
    if city:
        search_obituary(name, city)
    else:
        print("Unable to find city for the provided ZIP code.")
