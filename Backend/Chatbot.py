import json  # Ensure the import is used
from json import load, dump
from dotenv import dotenv_values
import requests
import datetime
from groq import Groq
import google.generativeai as genai
import mtranslate as mt

env_vars = dotenv_values(".env")

Username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")
GroqAPIKey = env_vars.get("GroqAPIKey")
GeminiAPIKey = env_vars.get("GeminiAPIKey")
InputLanguage = env_vars.get("InputLanguage")

client = Groq(api_key=GroqAPIKey)
genai.configure(api_key=GeminiAPIKey)
gemini_model = genai.GenerativeModel('gemini-1.5-flash')

messages = []

System = f"""Hello, I am {Username}, You are {Assistantname}, a friendly and efficient AI assistant.

PERSONALITY:
- Talk like a helpful human friend, not a robot
- Be conversational, warm, and natural
- Use casual language when appropriate
- Provide COMPLETE answers - don't cut off mid-sentence
- Be direct and clear

RULES:
- Reply in the same language as the user's query
- Don't mention time/date unless specifically asked
- Don't provide notes, disclaimers, or mention your training data
- Don't be overly formal - be friendly and relatable
- ALWAYS finish your complete thought - never stop mid-sentence
- Don't mention "homescreen", "interface", or "UI elements" unless specifically asked
- Focus on answering the actual question completely
"""

SystemChatBot = [
    {"role": "system", "content": System}
]

try:
    with open(r"Data\ChatLog.json", "r") as f:
        messages = load(f)
except FileNotFoundError:
    with open(r"Data\ChatLog.json", "w") as f:
        dump([], f)
except json.JSONDecodeError:
    print("ChatLog.json is empty or corrupted. Initializing with an empty list.")
    with open(r"Data\ChatLog.json", "w") as f:
        dump([], f)

def RealtimeInformation():
    current_date_time = datetime.datetime.now()
    day = current_date_time.strftime("%A")
    date = current_date_time.strftime("%d")
    month = current_date_time.strftime("%B")
    year = current_date_time.strftime("%Y")
    hour = current_date_time.strftime("%H")
    minute = current_date_time.strftime("%M")
    second = current_date_time.strftime("%S")

    data = f"Please use this real-time information if needed:\n"
    data += f"Day: {day}\nDate: {date}\nMonth: {month}\nYear: {year}\n"
    data += f"Time: {hour} hours, {minute} minutes, {second} seconds.\n"
    return data

def AnswerModifier(Answer):
    lines = Answer.split('\n')
    non_empty_lines = [line for line in lines if line.strip()]
    modified_answer = '\n'.join(non_empty_lines)
    return modified_answer

def ChatBot(Query):
    """ This function sends the user's query to the chatbot and returns the AI's response """

    try:
        with open(r"Data\ChatLog.json", "r") as f:
            messages = load(f)

        messages.append({"role": "user", "content": f"{Query}"})

        # Using latest Llama 4 Scout model for better responses
        completion = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=SystemChatBot + [{"role": "system", "content": RealtimeInformation()}] + messages,
            max_tokens=2048,  # Increased for complete responses
            temperature=0.8,  # Slightly higher for more natural conversation
            top_p=1,
            stream=True,
            stop=None
        )

        Answer = ""

        for chunk in completion:
            if chunk.choices[0].delta.content:
                Answer += chunk.choices[0].delta.content

        Answer = Answer.replace("</s>", "")

        # Translate response back to input language if not English
        if InputLanguage and InputLanguage.lower() != "en" and "en" not in InputLanguage.lower():
            Answer = mt.translate(Answer, InputLanguage[:2], "en")

        messages.append({"role": "assistant", "content": Answer})

        with open(r"Data\ChatLog.json", "w") as f:
            dump(messages, f, indent=4)

        return Answer  # Return the answer to the main function

    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")
        with open(r"Data\ChatLog.json", "w") as f:
            dump([], f, indent=4)
        return "Connection error, please try again."
    except Exception as e:
        print(f"Error: {e}")
        with open(r"Data\ChatLog.json", "w") as f:
            dump([], f, indent=4)
        return "An error occurred, please try again."

if __name__ == "__main__":
    while True:
        user_input = input("Enter Your Question: ")
        response = ChatBot(user_input)
        print(response)  # Print the response to the user