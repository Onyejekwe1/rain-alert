import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "OWM API KEY"
account_sid = "TWILIO SID"
auth_token = "TWILIO TOKEN"


weather_params = {
    "lat": 6.524379,
    "lon": 3.379206,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_forecast in weather_slice:
    weather_code = hour_forecast["weather"][0]["id"]
    print(hour_forecast["weather"][0]["id"])
    if int(weather_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain!",
        from_='+15012907360',
        to='+2347034258855'
    )

    print(message.sid)

