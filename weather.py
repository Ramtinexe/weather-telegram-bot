import os
import requests
from datetime import datetime


# -----------------------------
# Settings
# -----------------------------

MY_LATITUDE = 32.637654
MY_LONGITUDE = 51.370705

MY_API_KEY = os.environ["OPENWEATHER_API_KEY"]
MY_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
MY_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]


# -----------------------------
# Get weather data
# -----------------------------

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


# -----------------------------
# Persian day names
# -----------------------------

day_names = {
    "Saturday": "شنبه",
    "Sunday": "یکشنبه",
    "Monday": "دوشنبه",
    "Tuesday": "سه‌شنبه",
    "Wednesday": "چهارشنبه",
    "Thursday": "پنجشنبه",
    "Friday": "جمعه"
}


# -----------------------------
# Create Telegram message
# -----------------------------

message = "🌤️ پیش‌بینی هوا:\n\n"

for item in data["list"]:

    date_time = datetime.strptime(
        item["dt_txt"],
        "%Y-%m-%d %H:%M:%S"
    )

    day_name = day_names[date_time.strftime("%A")]

    date = date_time.strftime("%Y-%m-%d")
    time = date_time.strftime("%H:%M")

    temperature = round(item["main"]["temp"])
    weather = item["weather"][0]["description"]
    wind_speed = item["wind"]["speed"]

    message += (
        f"📅 تاریخ: {date}\n"
        f"🗓️ روز: {day_name}\n"
        f"🕐 ساعت: {time}\n"
        f"🌡️ دما: {temperature}°C\n"
        f"☁️ وضعیت: {weather}\n"
        f"🍃 سرعت باد: {wind_speed} m/s\n"
        f"━━━━━━━━━━━━━━\n"
    )


# -----------------------------
# Send message to Telegram
# -----------------------------

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



