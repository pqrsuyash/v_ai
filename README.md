# 🎙️ Voice-Activated Gemini Chatbot with Web Scraping

A voice-enabled chatbot using **Gemini 2.5 Flash** (via LangChain), with **speech recognition**, **text-to-speech**, and **website scraping**.

---

## 🚀 Features

- 🎤 Voice input (Google Speech Recognition)  
- 🧠 Gemini integration via LangChain  
- 🗣️ Voice output using pyttsx3  
- 🌐 Web scraping with BeautifulSoup  
- 💾 Saves scraped content for context  

---

## 📦 Requirements

Install dependencies:

---
pip install requests beautifulsoup4 python-dotenv pyttsx3 SpeechRecognition langchain-google-genai
Create a .env file with your API key:

env
api_key=YOUR_GOOGLE_GEMINI_API_KEY

---
## ⚙️ Usage
Set the website URL in the script:

---
scrape_website("https://example.com")
Run the script:
python main.py
Speak your queries. Say exit, quit, or stop to end the session.

---
## 📄 Files
---
main.py – Main script

.env – API key file

scraped_content.txt – Saved website text

---
## 📌 Notes
Works best with text-heavy websites

Requires a working microphone

Get your Gemini API key from Google AI Studio
