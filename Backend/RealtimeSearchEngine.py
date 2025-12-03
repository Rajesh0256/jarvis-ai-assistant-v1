from googlesearch import search
from groq import Groq
from json import load, dump
import datetime
from dotenv import dotenv_values
import requests
from bs4 import BeautifulSoup

env_vars = dotenv_values(".env")

Username = env_vars.get("Username", "User")
Assistantname = env_vars.get("Assistantname", "Jarvis")
GroqAPIKey = env_vars.get("GroqAPIKey", "")

if not GroqAPIKey:
    print("Warning: GroqAPIKey not found in .env file")
    GroqAPIKey = "dummy_key"

client = Groq(api_key=GroqAPIKey)

System = f"""Hello, I am {Username}, You are a very accurate and advanced AI chatbot named {Assistantname} which has real-time up-to-date information from the internet.

IMPORTANT INSTRUCTIONS:
1. You MUST use the search results provided between [start] and [end] tags to answer questions
2. The search results contain current, real-time information - USE THEM!
3. Extract relevant information from the titles and descriptions in the search results
4. If the answer is clearly mentioned in the search results, provide it confidently
5. Provide answers in a professional way with proper grammar
6. Be concise and direct - don't say you don't have information if it's in the search results
7. If multiple search results mention the same fact, that confirms it's correct

*** ALWAYS check the search results first before saying you don't have information ***
*** The search results are provided specifically to help you answer the question ***"""

import os

# Ensure Data directory exists
os.makedirs("Data", exist_ok=True)

try:
    with open(r"Data\ChatLog.json", "r") as f:
        messages = load(f)
except:
    with open(r"Data\ChatLog.json", "w") as f:
        dump([], f)

def GoogleSearch(query):
    """Search using multiple methods with fallback"""
    
    # Method 1: Try googlesearch-python library
    try:
        results = list(search(query, advanced=True, num_results=5))
        if results:
            Answer = f"The search results for '{query}' are :\n[start]\n"
            for i in results:
                Answer += f"Title: {i.title}\nDescription: {i.description}\n\n"
            Answer += "[end]"
            return Answer
    except Exception as e:
        print(f"googlesearch-python failed: {e}")
    
    # Method 2: Try DuckDuckGo HTML scraping (no API key needed)
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        url = f"https://html.duckduckgo.com/html/?q={query.replace(' ', '+')}"
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            results = soup.find_all('div', class_='result__body', limit=5)
            
            if results:
                Answer = f"The search results for '{query}' are :\n[start]\n"
                for result in results:
                    title_elem = result.find('a', class_='result__a')
                    snippet_elem = result.find('a', class_='result__snippet')
                    
                    if title_elem:
                        title = title_elem.get_text(strip=True)
                        snippet = snippet_elem.get_text(strip=True) if snippet_elem else ""
                        Answer += f"Title: {title}\nDescription: {snippet}\n\n"
                
                Answer += "[end]"
                return Answer
    except Exception as e:
        print(f"DuckDuckGo search failed: {e}")
    
    # Method 3: Use Wikipedia API for factual queries
    try:
        wiki_url = f"https://en.wikipedia.org/w/api.php"
        params = {
            'action': 'opensearch',
            'search': query,
            'limit': 3,
            'format': 'json'
        }
        response = requests.get(wiki_url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if len(data) > 2 and data[2]:  # Check if descriptions exist
                Answer = f"The search results for '{query}' are :\n[start]\n"
                for i in range(len(data[1])):
                    if i < len(data[2]):
                        Answer += f"Title: {data[1][i]}\nDescription: {data[2][i]}\n\n"
                Answer += "[end]"
                return Answer
    except Exception as e:
        print(f"Wikipedia search failed: {e}")
    
    # If all methods fail, return a message
    return f"The search results for '{query}' are :\n[start]\nUnable to fetch search results at this time. Please check your internet connection.\n[end]"

def AnswerModifier(Answer):
    lines = Answer.split('\n')
    non_empty_lines = [line for line in lines if line.strip()]
    modified_answer = '\n'.join(non_empty_lines)
    return modified_answer

SystemChatBot = [
    {"role": "system", "content": System},
    {"role": "user", "content": "Hi"},
    {"role": "assistant", "content": "Hello, Sir, how can I help you?"}
]

def Information():
    data = ""
    current_date_time = datetime.datetime.now()
    day = current_date_time.strftime("%A")
    date = current_date_time.strftime("%d")
    month = current_date_time.strftime("%B")
    year = current_date_time.strftime("%Y")
    hour = current_date_time.strftime("%H")
    minute = current_date_time.strftime("%M")
    second = current_date_time.strftime("%S")
    data += f"Use This Real-time Information if needed:\n"
    data += f"Day: {day}\n"
    data += f"Date: {date}\n"
    data += f"Month: {month}\n"
    data += f"Year: {year}\n"
    data += f"Time: {hour} hours: {minute} minutes: {second} seconds.\n"
    return data

def RealtimeSearchEngine(prompt):
    global SystemChatBot, messages

    with open(r"Data\ChatLog.json", "r") as f:
        messages = load(f)
    messages.append({"role": "user", "content": f"{prompt}"})

    SystemChatBot.append({"role": "system", "content": GoogleSearch(prompt)})

    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=SystemChatBot + [{"role": "system", "content": Information()}] + messages,
        max_tokens=2048,
        temperature=0.7,
        top_p=1,
        stream=True,
        stop=None
    )

    Answer = ""

    for chunk in completion:
        if chunk.choices[0].delta.content:
            Answer += chunk.choices[0].delta.content

    Answer = Answer.strip().replace("</s>", "")
    messages.append({"role": "assistant", "content": Answer})

    with open(r"Data\ChatLog.json", "w") as f:
        dump(messages, f, indent=4)

    SystemChatBot.pop()
    return AnswerModifier(Answer=Answer)

if __name__ == "__main__":
    while True:
        prompt = input("Enter Your Query: ")
        print(RealtimeSearchEngine(prompt))