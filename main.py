import os
import requests
import google.generativeai as genai

# Configuration
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
SERPER_API_KEY = os.environ.get("SERPER_API_KEY")
WA_INSTANCE_ID = os.environ.get("WA_INSTANCE_ID")
WA_API_TOKEN = os.environ.get("WA_API_TOKEN")

genai.configure(api_key=GEMINI_API_KEY)

def search_google(query):
    url = "https://google.serper.dev/search"
    payload = {"q": query}
    headers = {
        'X-API-KEY': SERPER_API_KEY,
        'Content-Type': 'application/json'
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def generate_ai_response(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text

def send_whatsapp_message(chat_id, message):
    url = f"https://api.green-api.com/waInstance{WA_INSTANCE_ID}/sendMessage/{WA_API_TOKEN}"
    payload = {
        "chatId": chat_id,
        "message": message
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

if __name__ == "__main__":
    print("Agent AI Social Media active and ready.")
