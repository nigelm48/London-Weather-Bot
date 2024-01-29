def get_weather():
    # Replace 'YOUR_CITY' with 'London' or any other city you are interested in
    city = 'London'
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': owm_api_key, 'units': 'metric'}
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        # Print the entire response for debugging
        print(data)

        # Extract relevant weather information
        temperature = data['main']['temp']
        description = data['weather'][0]['description']

        return f"Current weather in {city}: {temperature}°C, {description}"
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None
