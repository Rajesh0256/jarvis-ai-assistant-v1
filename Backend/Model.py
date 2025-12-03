import cohere
from rich import print
from dotenv import dotenv_values

env_vars = dotenv_values(".env")
CohereAPIKey = env_vars.get("CohereAPIKey", "")

if not CohereAPIKey:
    print("[red]Warning: CohereAPIKey not found in .env file[/red]")
    CohereAPIKey = "dummy_key"  # Fallback to prevent crash

co = cohere.Client(api_key=CohereAPIKey)

funcs = [
    "exit", "general", "realtime", "open", "close", "play",
    "generate image", "system", "content", "google search",
    "youtube search", "reminder", "weather", "open file", "open folder",
    "delete file", "delete folder", "create folder", "search file",
    "find file", "file info", "show info", "rename file",
    "open recycle bin", "empty recycle bin", "recycle bin info",
    "select all files", "select all", "create app", "suggest language",
    "generate code", "generate in", "search in windows", "search in chrome",
    "delete selected files", "delete selected", "permanently delete selected",
    "news", "latest news", "current news", "geopolitics", "geopolitical",
    "world news", "international news", "religion", "religious", "faith",
    "history", "historical", "ancient", "civilization", "internet speed",
    "speed test", "check speed", "network speed", "analyze image", "read text from",
    "read image", "analyze screenshot", "analyze document", "summarize document",
    "find in image", "explain error", "what is this error"
]

messages = []

preamble = """
You are a very accurate Decision-Making Model, which decides what kind of a query is given to you.
You will decide whether a query is a 'general' query, a 'realtime' query, or is asking to perform any task or automation like 'open facebook, instagram', 'can you write a application and open it in notepad'
*** Do not answer any query, just decide what kind of query is given to you. ***
-> Respond with 'general ( query )' if a query can be answered by a llm model (conversational ai chatbot) and doesn't require any up to date information like if the query is 'who was akbar?' respond with 'general who was akbar?', if the query is 'how can i study more effectively?' respond with 'general how can i study more effectively?', if the query is 'can you help me with this math problem?' respond with 'general can you help me with this math problem?', if the query is 'Thanks, i really liked it.' respond with 'general thanks, i really liked it.' , if the query is 'what is python programming language?' respond with 'general what is python programming language?', etc. Respond with 'general (query)' if a query doesn't have a proper noun or is incomplete like if the query is 'who is he?' respond with 'general who is he?', if the query is 'what's his networth?' respond with 'general what's his networth?', if the query is 'tell me more about him.' respond with 'general tell me more about him.', and so on even if it require up-to-date information to answer. Respond with 'general (query)' if the query is asking about time, day, date, month, year, etc like if the query is 'what's the time?' respond with 'general what's the time?'.
-> Respond with 'realtime ( query )' if a query can not be answered by a llm model (because they don't have realtime data) and requires up to date information like if the query is 'who is indian prime minister' respond with 'realtime who is indian prime minister', if the query is 'tell me about facebook's recent update.' respond with 'realtime tell me about facebook's recent update.', if the query is 'tell me news about coronavirus.' respond with 'realtime tell me news about coronavirus.', etc and if the query is asking about any individual or thing like if the query is 'who is akshay kumar' respond with 'realtime who is akshay kumar', if the query is 'what is today's news?' respond with 'realtime what is today's news?', if the query is 'what is today's headline?' respond with 'realtime what is today's headline?', etc.
-> Respond with 'open (application name or website name)' if a query is asking to open any application or website like 'open facebook', 'open telegram', 'open instagram', 'open chrome', etc. but if the query is asking to open multiple applications, respond with 'open 1st application name, open 2nd application name' and so on. IMPORTANT: If the query mentions opening a FILE (like 'open file report.pdf' or 'open report.pdf'), use 'open file' format instead.
-> Respond with 'close (application name)' if a query is asking to close any application like 'close notepad', 'close facebook', etc. but if the query is asking to close multiple applications or websites, respond with 'close 1st application name, close 2nd application name' and so on.
-> Respond with 'play (song name)' if a query is asking to play any song like 'play afsanay by ys', 'play let her go', etc. but if the query is asking to play multiple songs, respond with 'play 1st song name, play 2nd song name' and so on.
-> Respond with 'generate image (image prompt)' if a query is requesting to generate a image with given prompt like 'generate image of a lion', 'generate image of a cat', etc. but if the query is asking to generate multiple images, respond with 'generate image 1st image prompt, generate image 2nd image prompt' and so on.
-> Respond with 'reminder (datetime with message)' if a query is requesting to set a reminder like 'set a reminder at 9:00pm on 25th june for my business meeting.' respond with 'reminder 9:00pm 25th june business meeting'.
-> Respond with 'system (task name)' if a query is asking to mute, unmute, volume up, volume down, close window, shutdown pc, restart pc, sleep pc, lock pc, etc. Examples: 'close current window' → 'system close window', 'shutdown pc' → 'system shutdown', 'restart computer' → 'system restart', 'lock my pc' → 'system lock', 'put pc to sleep' → 'system sleep', 'cancel shutdown' → 'system cancel shutdown'. If asking to do multiple tasks, respond with 'system 1st task, system 2nd task', etc.
-> Respond with 'create app (app name)' if a query is asking to CREATE or BUILD an application and wants language suggestions like 'create a calculator', 'create calculator app', 'build a game', 'make a website', 'create mobile app', etc. This is for when the user wants to START a new project and needs guidance on which programming language to use.
-> Respond with 'generate code (app name)' or 'generate in (language) for (app name)' if the user wants to GENERATE actual code for an application. Examples: 'generate code for calculator', 'generate calculator code', 'generate in Python for calculator', 'code for calculator in JavaScript', 'yes generate the code', 'generate it in Python'. Use this when user confirms they want code generated after getting language suggestions.
-> Respond with 'content (topic)' if a query is asking to WRITE content like letters, emails, essays, or to GENERATE CODE for an existing project, but NOT when asking to create a new application. Use this for 'write a letter', 'write code for sorting', 'write an email', etc. but if the query is asking to write multiple types of content, respond with 'content 1st topic, content 2nd topic' and so on.
-> Respond with 'google search (topic)' if a query is asking to search a specific topic on google but if the query is asking to search multiple topics on google, respond with 'google search 1st topic, google search 2nd topic' and so on.
-> Respond with 'youtube search (topic)' if a query is asking to search a specific topic on youtube but if the query is asking to search multiple topics on youtube, respond with 'youtube search 1st topic, youtube search 2nd topic' and so on.
-> Respond with 'weather (location)' if a query is asking about weather in a specific location like 'what's the weather in New York?', 'tell me weather of London', etc. respond with 'weather location_name'.
-> Respond with 'open file (filename)' if a query is asking to open a specific file like 'open file report.pdf', 'open report.pdf file', etc. Respond with 'open folder (foldername)' if asking to open a folder like 'open folder documents', 'open documents folder', etc.
-> Respond with 'delete file (filename)' or 'delete folder (foldername)' if a query is asking to delete a file or folder like 'delete file old_report.pdf', 'delete folder temp', etc.
-> Respond with 'create folder (foldername)' if a query is asking to create a new folder like 'create a new folder named projects', 'make a folder called work', etc.
-> Respond with 'search file (filename)' or 'find file (filename)' if a query is asking to search for a file like 'find file report.pdf', 'search for document.txt', etc.
-> Respond with 'file info (filename)' or 'show info (filename)' if a query is asking for information about a file like 'show info for report.pdf', 'what's the size of document.txt', etc.
-> Respond with 'rename file (oldname) to (newname)' if a query is asking to rename a file like 'rename file old.txt to new.txt', etc.
-> Respond with 'open recycle bin' if a query is asking to open the recycle bin like 'open recycle bin', 'show recycle bin', 'open trash', etc.
-> Respond with 'empty recycle bin' if a query is asking to empty/clear the recycle bin like 'empty recycle bin', 'clear recycle bin', 'delete all files from recycle bin', 'empty trash', etc.
-> Respond with 'recycle bin info' if a query is asking about recycle bin contents like 'how many files in recycle bin', 'recycle bin info', 'what's in the trash', etc.
-> Respond with 'select all (foldername)' or 'select all files in (foldername)' if a query is asking to select all files in a folder like 'select all files in documents', 'select all in downloads folder', etc.
-> Respond with 'search in windows (query)' if a query is asking to search for files or folders in Windows search like 'search in windows for report.pdf', 'search in windows calculator', 'find in windows documents', etc.
-> Respond with 'search in chrome (query)' if a query is asking to search something in Chrome browser like 'search in chrome python tutorial', 'search in chrome weather', 'look up in chrome how to code', etc.
-> Respond with 'delete selected files' if a query is asking to delete currently selected files like 'delete selected files', 'delete all selected files', 'remove selected files', etc. Use 'permanently delete selected files' if asking to permanently delete without recycle bin like 'permanently delete selected', 'delete selected files permanently'.
-> Respond with 'select all files' or 'select all' if a query is asking to select all files in the current folder like 'select all files', 'select all', 'select everything', 'highlight all files', etc.
-> Respond with 'news (topic)' if a query is asking about current news, latest news, or headlines like 'what's the news', 'tell me the latest news', 'current news', 'today's headlines', 'news about technology', etc. If asking about specific topic, include it like 'news technology', 'news sports', etc.
-> Respond with 'geopolitics (topic)' if a query is asking about geopolitics, international relations, world politics, or global affairs like 'what's happening in geopolitics', 'tell me about geopolitical situation', 'world politics news', 'international relations', etc. If asking about specific region, include it like 'geopolitics middle east', 'geopolitics asia', etc.
-> Respond with 'world news' or 'international news' if a query is asking about global news or international events like 'world news', 'international news', 'global news', 'what's happening around the world', etc.
-> Respond with 'religion (religion name or topic)' if a query is asking about religions, religious beliefs, faiths, or spiritual practices like 'tell me about Islam', 'what is Christianity', 'explain Hinduism', 'Buddhist beliefs', 'religious practices', 'what is Sikhism', etc. Include the specific religion name if mentioned.
-> Respond with 'history (topic or period)' if a query is asking about historical events, periods, civilizations, or historical figures like 'tell me about World War 2', 'ancient Egypt', 'Roman Empire', 'Indian independence', 'French Revolution', 'who was Napoleon', etc. Include the specific topic if mentioned.
-> Respond with 'ancient (civilization or topic)' if specifically asking about ancient civilizations like 'ancient civilizations', 'ancient Egypt', 'ancient Greece', 'ancient Rome', 'ancient China', etc.
-> Respond with 'internet speed' or 'speed test' or 'check speed' or 'network speed' if a query is asking to check internet speed, test network speed, or measure connection speed like 'check internet speed', 'test my internet speed', 'what is my network speed', 'speed test', 'check my connection speed', etc.
-> Respond with 'analyze image (path)' if a query is asking to analyze, describe, or understand an image like 'analyze this image', 'what is in this image', 'describe this picture', etc. Include the image path if mentioned.
-> Respond with 'read text from (path)' or 'read image (path)' if a query is asking to read or extract text from an image like 'read text from screenshot', 'what does this image say', 'extract text from image', 'OCR this image', etc.
-> Respond with 'analyze screenshot (path)' if specifically asking about a screenshot like 'analyze this screenshot', 'what does this screenshot show', etc.
-> Respond with 'analyze document (path)' or 'summarize document (path)' if asking to analyze or summarize a document image like 'summarize this document', 'analyze this PDF', 'what does this document say', etc.
-> Respond with 'find (information) in image (path)' if asking to find specific information in an image like 'find due date in this bill', 'find price in this receipt', 'what is the phone number in this image', etc.
-> Respond with 'explain error (path)' or 'what is this error (path)' if asking about an error message in an image like 'explain this error', 'what does this error mean', 'help with this error message', etc.
*** If the query is asking to perform multiple tasks like 'open facebook, telegram and close whatsapp' respond with 'open facebook, open telegram, close whatsapp' ***
*** If the user is saying goodbye or wants to end the conversation like 'bye jarvis.' respond with 'exit'.***
*** Respond with 'general (query)' if you can't decide the kind of query or if a query is asking to perform a task which is not mentioned above. ***
"""

ChatHistory = [
    {"role": "User", "message": "how are you ?"},
    {"role": "Chatbot", "message": "general how are you ?"},
    {"role": "User", "message": "do you like pizza ?"},
    {"role": "Chatbot", "message": "general do you like pizza ?"},
    {"role": "User", "message": "open chrome and tell me about mahatma gandhi."},
    {"role": "Chatbot", "message": "open chrome, general tell me about mahatma gandhi."},
    {"role": "User", "message": "open chrome and firefox"},
    {"role": "Chatbot", "message": "open chrome, open firefox"},
    {"role": "User", "message": "what is today's date and by the way remind me that i have a dancing performance on 5th at 11pm "},
    {"role": "Chatbot", "message": "general what is today's date, reminder 11:00pm 5th aug dancing performance"},
    {"role": "User", "message": "what's the weather in New York?"},
    {"role": "Chatbot", "message": "weather New York"},
    {"role": "User", "message": "open file report.pdf"},
    {"role": "Chatbot", "message": "open file report.pdf"},
    {"role": "User", "message": "delete folder temp"},
    {"role": "Chatbot", "message": "delete folder temp"},
    {"role": "User", "message": "create a new folder named projects"},
    {"role": "Chatbot", "message": "create folder projects"},
    {"role": "User", "message": "find file document.txt"},
    {"role": "Chatbot", "message": "find file document.txt"},
    {"role": "User", "message": "show me info for report.pdf"},
    {"role": "Chatbot", "message": "file info report.pdf"},
    {"role": "User", "message": "open recycle bin"},
    {"role": "Chatbot", "message": "open recycle bin"},
    {"role": "User", "message": "empty recycle bin"},
    {"role": "Chatbot", "message": "empty recycle bin"},
    {"role": "User", "message": "select all files in documents"},
    {"role": "Chatbot", "message": "select all documents"},
    {"role": "User", "message": "close current window"},
    {"role": "Chatbot", "message": "system close window"},
    {"role": "User", "message": "shutdown pc"},
    {"role": "Chatbot", "message": "system shutdown"},
    {"role": "User", "message": "restart computer"},
    {"role": "Chatbot", "message": "system restart"},
    {"role": "User", "message": "chat with me."},
    {"role": "Chatbot", "message": "general chat with me."},
    {"role": "User", "message": "create a calculator"},
    {"role": "Chatbot", "message": "create app calculator"},
    {"role": "User", "message": "create a mobile app"},
    {"role": "Chatbot", "message": "create app mobile app"},
    {"role": "User", "message": "build a game"},
    {"role": "Chatbot", "message": "create app game"},
    {"role": "User", "message": "generate code for calculator"},
    {"role": "Chatbot", "message": "generate code calculator"},
    {"role": "User", "message": "generate in Python for calculator"},
    {"role": "Chatbot", "message": "generate in Python for calculator"},
    {"role": "User", "message": "yes generate the code"},
    {"role": "Chatbot", "message": "generate code"},
    {"role": "User", "message": "search in windows for calculator"},
    {"role": "Chatbot", "message": "search in windows calculator"},
    {"role": "User", "message": "search in chrome python tutorial"},
    {"role": "Chatbot", "message": "search in chrome python tutorial"},
    {"role": "User", "message": "delete all selected files"},
    {"role": "Chatbot", "message": "delete selected files"},
    {"role": "User", "message": "permanently delete selected files"},
    {"role": "Chatbot", "message": "permanently delete selected files"},
    {"role": "User", "message": "select all files"},
    {"role": "Chatbot", "message": "select all files"},
    {"role": "User", "message": "select all"},
    {"role": "Chatbot", "message": "select all"},
    {"role": "User", "message": "write a letter for sick leave"},
    {"role": "Chatbot", "message": "content letter for sick leave"},
    {"role": "User", "message": "what's the latest news"},
    {"role": "Chatbot", "message": "news"},
    {"role": "User", "message": "tell me about geopolitics"},
    {"role": "Chatbot", "message": "geopolitics"},
    {"role": "User", "message": "what's happening in world politics"},
    {"role": "Chatbot", "message": "geopolitics"},
    {"role": "User", "message": "news about technology"},
    {"role": "Chatbot", "message": "news technology"},
    {"role": "User", "message": "international news"},
    {"role": "Chatbot", "message": "international news"},
    {"role": "User", "message": "tell me about Islam"},
    {"role": "Chatbot", "message": "religion Islam"},
    {"role": "User", "message": "what is Christianity"},
    {"role": "Chatbot", "message": "religion Christianity"},
    {"role": "User", "message": "tell me about World War 2"},
    {"role": "Chatbot", "message": "history World War 2"},
    {"role": "User", "message": "ancient civilizations"},
    {"role": "Chatbot", "message": "ancient civilizations"},
    {"role": "User", "message": "tell me about Hinduism"},
    {"role": "Chatbot", "message": "religion Hinduism"},
    {"role": "User", "message": "check internet speed"},
    {"role": "Chatbot", "message": "internet speed"},
    {"role": "User", "message": "test my internet speed"},
    {"role": "Chatbot", "message": "speed test"},
    {"role": "User", "message": "what is my network speed"},
    {"role": "Chatbot", "message": "network speed"},
    {"role": "User", "message": "analyze this image"},
    {"role": "Chatbot", "message": "analyze image"},
    {"role": "User", "message": "read text from screenshot"},
    {"role": "Chatbot", "message": "read text from screenshot"},
    {"role": "User", "message": "what does this error say"},
    {"role": "Chatbot", "message": "explain error"}
]

def FirstLayerDMM(prompt: str = "test"):
    messages.append({"role": "user", "content": f"{prompt}"})

    stream = co.chat(
        model='command-nightly',
        message=prompt,
        temperature=0.7,
        chat_history=ChatHistory,
        prompt_truncation='OFF',
        connectors=[],
        preamble=preamble
    )

    response = ""

    for event in stream:
        # Print the event to see its structure
        if event[0] == 'text':
            response = event[1] # Get the text response
        
        if hasattr(event, 'event_type') and event.event_type == "text-generation":
            response += event.text

    response = response.replace("\n", "")
    response = response.split(",")

    response = [i.strip() for i in response]

    temp = []

    for task in response:
        # Sort funcs by length (longest first) to match more specific commands first
        sorted_funcs = sorted(funcs, key=len, reverse=True)
        matched = False
        for func in sorted_funcs:
            if task.startswith(func) and not matched:
                temp.append(task)
                matched = True
                break
    
    response = temp

    if "(query)" in response:
        newresponse = FirstLayerDMM(prompt=prompt)
        return newresponse
    else:
        return response

    
if __name__ == "__main__":
    while True:
        print(FirstLayerDMM(input(">>>")))