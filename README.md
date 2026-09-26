# 🌤️ Telegram Weather Bot

A simple Python weather bot that fetches weather forecasts from the **OpenWeather API** and sends them to a Telegram chat automatically.

The bot is designed to run with **GitHub Actions**, so it can send a daily weather forecast without requiring a computer or server to stay online.

## ✨ Features

* 🌤️ Fetches weather forecasts using OpenWeather API
* 📅 Displays the date and day of the week
* 🕐 Displays forecast time
* 🌡️ Displays temperature in Celsius
* ☁️ Displays weather conditions in Persian
* 🍃 Displays wind speed
* 🤖 Sends the forecast directly to Telegram
* ⏰ Runs automatically every day using GitHub Actions
* 🔐 Uses GitHub Secrets to protect API keys and credentials

## 🛠️ Technologies

* Python
* Requests
* OpenWeather API
* Telegram Bot API
* GitHub Actions

## 📁 Project Structure

```text
weather-telegram-bot/
│
├── weather.py
└── .github/
    └── workflows/
        └── weather.yml
```

## 🔐 Environment Variables

The project uses the following environment variables:

```text
OPENWEATHER_API_KEY
TELEGRAM_BOT_TOKEN
TELEGRAM_CHAT_ID
LATITUDE
LONGITUDE
```

These values should be stored as **GitHub Actions Secrets** and should not be hard-coded in the source code.

## ⏰ Automation

GitHub Actions runs the script automatically every day at **06:00 Iran time**.

It can also be triggered manually using:

**GitHub → Actions → Daily Weather → Run workflow**

## 🚀 How It Works

```text
GitHub Actions
      ↓
   weather.py
      ↓
 OpenWeather API
      ↓
 Weather Forecast
      ↓
 Telegram Bot API
      ↓
 Telegram Chat
```

## 📌 Example

The bot sends a message similar to:

```text
🌤️ پیش‌بینی هوا:

📅 تاریخ: 2026-09-26
🗓️ روز: شنبه
🕐 ساعت: 06:00
🌡️ دما: 18°C
☁️ وضعیت: آسمان صاف
🍃 سرعت باد: 2.4 m/s
━━━━━━━━━━━━━━
```

## 🎯 Purpose

This project was created as a practical Python project to learn:

* Working with APIs
* Handling JSON data
* Environment variables
* Telegram Bot API
* GitHub Actions
* Automating Python scripts

## 📄 License

This project is open-source and available under the MIT License.
