# 🤖 Gemini-Powered Telegram AI Bot

[![Hugging Face Space](https://shields.io)](https://huggingface.co)
[![Python Version](https://shields.io)](https://python.org)
[![License: MIT](https://shields.io)](https://opensource.org)

An intelligent, cloud-hosted Telegram chat assistant driven by Google's **Gemini 2.5 Flash** model. This bot handles user inquiries in real-time, displays live typing indicators, and runs permanently 24/7 inside an isolated Docker container on Hugging Face Spaces—100% free.

---

## ✨ Features

*   **⚡ Real-Time AI Generation**: Integrates the official next-gen `google-genai` SDK using `gemini-2.5-flash` for instant, intelligent answers.
*   **💬 Immersive Chat UX**: Triggers a native Telegram `typing...` status action while processing AI requests.
*   **🐋 Cloud-Ready Architecture**: Bundled via Docker using unprivileged user permissions for secure deployment.
*   **📡 Smart Health Verification**: Includes a lightweight concurrent background server thread to pass automated platform uptime checks.
*   **🔒 Secured Credentials**: Zero hardcoded secrets. Fully configured via external system environment variables.

---

## 🛠️ Tech Stack

*   **Language:** Python 3.11
*   **API Framework:** `python-telegram-bot` (Asynchronous Engine)
*   **AI Engine:** Official `google-genai` SDK
*   **Containerization:** Docker
*   **Deployment Host:** Hugging Face Spaces (Docker SDK Tier)

---

## 📂 Project Structure

```text
├── bot.py             # Main asynchronous bot engine & background dummy server
├── Dockerfile         # Non-root user Docker containerization layout
├── requirements.txt   # Pinpoint package dependencies
└── README.md          # Project documentation mapping
```

---

## 🚀 Local Installation & Self-Hosting

### 1. Prerequisites
Ensure you have Python 3.11+ installed on your local Linux, macOS, or Windows machine.

### 2. Obtain Credentials
*   **Telegram Bot Token**: Message [@BotFather](https://t.me) on Telegram and trigger `/newbot`.
*   **Gemini API Key**: Generate a free key via [Google AI Studio](https://google.dev).

### 3. Setup Virtual Environment & Install Packages
```bash
# Clone the repository
git clone https://github.com
cd YOUR_REPOSITORY_NAME

# Setup a clean Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install all necessary dependency libraries
pip install -r requirements.txt
```

### 4. Configure Environment Secrets
Create a hidden `.env` configuration file in the project's root folder:
```text
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5. Launch the Local Script
```bash
python3 bot.py
```

---

## 🌐 Production Deployment (Hugging Face Spaces)

This project is fully structured to deploy seamlessly onto **Hugging Face Spaces** using the **Docker SDK**:

1. Log into [Hugging Face](https://huggingface.co) and create a **New Space**.
2. Select **Docker** as the SDK platform template and choose **Blank**.
3. Navigate to **Settings** > **Variables and secrets**. Add your runtime credentials:
   *   `TELEGRAM_BOT_TOKEN`
   *   `GEMINI_API_KEY`
4. Upload `bot.py`, `Dockerfile`, `requirements.txt`, and `README.md` to the Files repository.
5. Hugging Face will automatically detect the internal configuration, build the environment container, and launch your bot 24/7!

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more details.
