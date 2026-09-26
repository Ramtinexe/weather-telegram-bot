import os
import requests


# =========================
# SETTINGS
# =========================

MY_LATITUDE = 32.635109
MY_LONGITUDE = 51.367641

MY_API_KEY = os.environ["OPENWEATHER_API_KEY"]
MY_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
MY_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]


# =========================
# GET WEATHER
# =========================

weather_params = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": MY_API_KEY,
    "cnt": 8,
    "units": "metric",
    "lang": "fa"
}

response = requests.get(
    "https://api.openweathermap.org/data/2.5/forecast",
    params=weather_params,
    timeout=30
)

response.raise_for_status()

data = response.json()


# =========================
# CREATE MESSAGE
# =========================

message = "🌤️ پیش‌بینی هوای امروز:\n\n"

for item in data["list"]:

    time = item["dt_txt"]
    temperature = round(item["main"]["temp"])
    weather = item["weather"][0]["description"]
    wind_speed = item["wind"]["speed"]

    message += (
        f"🕐 زمان: {time}\n"
        f"🌡️ دما: {temperature}°C\n"
        f"☁️ وضعیت: {weather}\n"
        f"🍃 سرعت باد: {wind_speed} m/s\n"
        f"━━━━━━━━━━━━━━\n"
    )


# =========================
# SEND TO TELEGRAM
# =========================

telegram_url = (
    f"https://api.telegram.org/bot{MY_BOT_TOKEN}/sendMessage"
)

telegram_params = {
    "chat_id": MY_CHAT_ID,
    "text": message
}

telegram_response = requests.post(
    telegram_url,
    params=telegram_params,
    timeout=30
)

telegram_response.raise_for_status()

print("✅ Weather sent successfully!")