import os
import requests
from dotenv import load_dotenv


load_dotenv()


URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if api_key:
        response = requests.get(URL + f"key={api_key}&q={FILTERING}")
        response_json = response.json()
        location = (f"{response_json['location']['name']}/"
                    f"{response_json['location']['country']}")
        time = response_json['location']['localtime']
        weather = (f"Weather: {response_json['current']['temp_c']} Celsius, "
                   f"{response_json['current']['condition']['text']}")
        print(f"{location} {time} {weather}")
    else:
        print("Error: API Key is missing")


if __name__ == "__main__":
    get_weather()
