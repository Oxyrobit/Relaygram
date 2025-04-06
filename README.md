# Relaygram

Relaygram is a multilingual Telegram relay bot that forwards messages from one channel to another and saves attached files locally.

## 🧠 Purpose

This project automatically monitors a Telegram channel to:
- Download any attached files
- Forward all new messages (whether they contain files or not) to another channel

It is built with Python using the Telethon library and supports Docker deployment.

## 🌍 Language Support

The interface messages (CLI outputs) are multilingual and controlled via the `LANG` variable in your `.env` file.

- `LANG=fr` for French
- `LANG=en` for English

The default language is French if not specified.

## 🔐 Telegram Authentication

Before using the bot, you need to generate a **persistent Telegram session**.

### Steps:
1. Go to [https://my.telegram.org](https://my.telegram.org)
2. Create an app to get your `API_ID` and `API_HASH`
3. On the first launch, the script will guide you to generate a `StringSession`:
    - Enter your phone number
    - Enter the code you receive by SMS or Telegram
    - Copy the generated session string
    - Paste it into the `.env` file under `SESSION_STRING`

This session will be reused automatically on each launch.

## ⚙️ Execution Modes

You can choose between two modes using the `MODE` variable in `.env`:

### 🧪 Development Mode (`dev`)
- Displays a terminal menu with a list of your channels
- You manually select the source channel to monitor
- The destination channel is defined in `.env`

### 🚀 Production Mode (`prod`)
- Both source and destination channels are set in `.env`
- No user interaction is needed
- Ideal for automated server deployment

## 📁 Project Structure

- `generate_session.py` : generates the StringSession
- `main.py` : main bot script
- `start.py` : entrypoint that checks for session and launches the right script
- `lang.py` : contains multilingual CLI messages
- `downloads/` : where received files are saved
- `.env` : environment configuration (not versioned)
- `.env.example` : configuration template
- `Dockerfile` : defines the Docker image
- `docker-compose.yml` : simplifies containerized execution
- `README.md` : this documentation

## ⚙️ Environment Variables (.env)

Required variables:

- `API_ID` : your Telegram app ID
- `API_HASH` : your Telegram app hash
- `SESSION_STRING` : persistent session string
- `MODE` : either `dev` or `prod`
- `SOURCE_CHANNEL_ID` : source channel ID (used only in prod)
- `TARGET_CHANNEL_ID` : destination channel ID (used in both modes)
- `LANG` : `fr` or `en` (optional)

## 🐳 Useful Docker Commands

### 🔧 Build the Docker image

Run this only once, or after modifying the Dockerfile:

```bash
docker compose build
```

### ▶️ Interactive launch (dev mode)

Run the bot in development mode. You'll be able to choose the source channel manually:

```bash
docker compose run --rm relaygram
```

### 🚀 Automatic launch (prod mode)

Run the bot in production mode using `.env` configuration, with no user interaction:

```bash
docker compose up -d
```

## 📝 Final Notes

- Authentication happens **only once**: the Telegram session is saved.
- You must be a **member of both source and destination channels**.
- Only **new messages** are forwarded – history is not retrieved.
