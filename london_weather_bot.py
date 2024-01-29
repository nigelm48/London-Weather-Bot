import tweepy
import requests
from datetime import datetime, timedelta
import time

# Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

# OpenWeatherMap API key
owm_api_key = 'YOUR_OPENWEATHERMAP_API_KEY'

# Tweepy authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_weather():
    # Replace 'YOUR_CITY' with 'London' or any other city you are interested in
    city = 'London'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': owm_api_key, 'units': 'metric'}
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        # Extract relevant weather information
        temperature = data['main']['temp']
        description = data['weather'][0]['description']

        return f"Current weather in {city}: {temperature}°C, {description}"
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

def tweet_weather():
    weather_info = get_weather()
    if weather_info:
        try:
            # Post tweet
            api.update_status(weather_info)
            print(f"Tweeted: {weather_info}")
        except tweepy.TweepError as te:
            print(f"Error tweeting: {te}")

# Tweet weather every hour
while True:
    tweet_weather()
    time.sleep(3600)  # Sleep for 1 hour (3600 seconds)
