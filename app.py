import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
import pyttsx3
import speech_recognition as sr

# Load .env
load_dotenv()
api_key = os.getenv("api_key")

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key,
    temperature=0.3
)

# Initialize Text-to-Speech
engine = pyttsx3.init()

# File to store scraped content
CHAT_HISTORY_FILE = "scraped_content.txt"

# Load previous scraped content
def load_chat_history():
    if os.path.exists(CHAT_HISTORY_FILE):
        with open(CHAT_HISTORY_FILE, "r", encoding="utf-8") as file:
            return file.read()
    return ""

# Scrape website and save text to file
def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        for script in soup(["script", "style"]):
            script.decompose()

        text = soup.get_text(separator='\n', strip=True)

        with open(CHAT_HISTORY_FILE, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Scraping complete. Content saved to '{CHAT_HISTORY_FILE}'")

    except Exception as e:
        print("Failed to scrape:", e)

# Speak output
def speak(text):
    print("Gemini:", text)
    engine.say(text)
    engine.runAndWait()

# Take input from microphone
def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print("You:", text)
            return text
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that.")
            return ""
        except sr.RequestError:
            speak("Speech service error.")
            return ""

# 🔧 Website to scrape
scrape_website("")

# Chat loop
while True:
    user_input = get_voice_input()

    if not user_input:
        continue

    if user_input.lower() in ['exit', 'quit', 'stop']:
        speak("Goodbye!")
        break

    chat_history = load_chat_history()
    full_prompt = f"{chat_history}\nUser: {user_input}\nGemini:"

    response = llm.invoke(full_prompt)
    speak(response.content)
