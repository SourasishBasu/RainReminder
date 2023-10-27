import requests
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console and set the environment variables in your local environment.
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

weather_codes = []
flag = 0

parameters = {
    "q": "City,Country",  # Example: "London,UK"
    "days": 1,
    "alerts": "no",
    "aqi": "no",
    "key": os.environ["WEATHER_API_KEY"]
}

url = "http://api.weatherapi.com/v1/forecast.json" 

# Receive hourly weather forecast info for my location
response = requests.get(url, params=parameters)
data = response.json()

# Parsing the json to extract the weather codes of next 12 hours from the data
for i in range(0, 12):
    weather_codes.append(data["forecast"]["forecastday"][0]["hour"][i]["condition"]["code"])

# Checking codes to find whether possibility of rain in 12 hours
for j in range(len(weather_codes)):
    if weather_codes[j] > 1030 and weather_codes[j] not in [1135, 1147]:
        flag = 1
        break

# Sending SMS via Twilio API if it rains
if flag == 1:
    msg = "Its going to rain today. Remember to bring your umbrella!"
    message = client.messages \
        .create(
        body=f"{msg}",
        from_='TWILIO_PHONE_NUMBER',
        to='YOUR_VERIFIED_PHONE_NUMBER')
