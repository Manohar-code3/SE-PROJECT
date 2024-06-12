# import speech_recognition as sr
# import os
# #import distutils
# def say(text):
#     os.system(f"say {text}")
#
# def takecommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#          r.pause_threshold = 1
#          audio = r.listen(source)
#          query = r.recognize_google(audio, language="en-IN")
#          print(f"User said: {query}")
#          return query
# if __name__ == '__main__':
#      print('PyCharm')
#      say("Hello I am Jarvis A.I")
#      print("Listening..")
#      text = takecommand()
#      say(text)

#learn about web driver package an duse it in this project
#for music 30 minutes
import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import google.generativeai as genai
import random

chatStr = " "
def chat(query):
    global chatStr
    print(chatStr)
    genai.configure(api_key="AIzaSyAmg262dKa4jCGyzvwfLyIZN-wYbRtV5DA")
    chatStr += f"Shafiya: {query}\n Jarvis: "
    #chatStr += "Shafiya: " + query + "\n Jarvis:"

    #text = f"OpenAi response for Prompt: {query}\n ********************* \n\n"
    #text = f"{query}"
    # Set up the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 0,
        "max_output_tokens": 8192,
    }
    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                  generation_config=generation_config)
                                  #safety_settings=safety_settings)

    convo = model.start_chat(history=[
        {
            "role": "user",
            "parts": [chatStr]
        },
        # {
        # "role": "model",
        # "parts": [
        #    "## Resignation Email Template\n\n**Subject: Resignation - [Your Name]**\n\nDear [Boss's name],\n\nPlease accept this email as formal notification that I am resigning from my position as [Your job title] at [Company name]. My last day of employment will be [Your last day - typically two weeks from the date you give notice]. \n\nThank you for the opportunity to work at [Company name] for the past [Length of employment]. I've enjoyed my time here and appreciate the opportunities I've had to [Mention something you learned or a positive experience]. \n\n[Optional: Briefly state your reason for leaving, e.g., I am pursuing a new opportunity that aligns more closely with my long-term career goals.]\n\nPlease let me know if there is anything I can do to help ensure a smooth transition during this time. \n\nI wish you and the company all the best in the future.\n\nSincerely,\n\n[Your Name]"]
        # },
    ])
    convo.send_message("YOUR_USER_INPUT")
    say(convo.last.text)
    # response = convo.last.text
    # chatStr += f"{response}\n"
    chatStr += f"{convo.last.text}\n"
    return convo.last.text
    with open(f"Openai/{''.join(query.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(response)

def ai(query):
    genai.configure(api_key="AIzaSyAmg262dKa4jCGyzvwfLyIZN-wYbRtV5DA")
    text = f"OpenAi response for Prompt: {query}\n ********************* \n\n"

    # Set up the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 0,
        "max_output_tokens": 8192,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
    ]

    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    convo = model.start_chat(history=[
        {
            "role": "user",
            "parts": [query]
        },
        #{
            #"role": "model",
            #"parts": [
            #    "## Resignation Email Template\n\n**Subject: Resignation - [Your Name]**\n\nDear [Boss's name],\n\nPlease accept this email as formal notification that I am resigning from my position as [Your job title] at [Company name]. My last day of employment will be [Your last day - typically two weeks from the date you give notice]. \n\nThank you for the opportunity to work at [Company name] for the past [Length of employment]. I've enjoyed my time here and appreciate the opportunities I've had to [Mention something you learned or a positive experience]. \n\n[Optional: Briefly state your reason for leaving, e.g., I am pursuing a new opportunity that aligns more closely with my long-term career goals.]\n\nPlease let me know if there is anything I can do to help ensure a smooth transition during this time. \n\nI wish you and the company all the best in the future.\n\nSincerely,\n\n[Your Name]"]
        #},
    ])

    convo.send_message("YOUR_USER_INPUT")
    print(convo.last.text)
    # text += convo.last.text

    #response = convo.last.text
    text += convo.last.text
    return text

    # if not os.path.exists("Openai"):
    #     os.mkdir("Openai")
    # with open(f"Openai/prompt- {random.randint(1, 23434343224, )}", "w") as f:
    #     f.write(text)

def say(text):
    os.system(f'say "{text}"')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        print("Recognizing...")
        try:
            query = r.recognize_google(audio, language="en-IN")  # Adjust language to en-US for macOS #hi-in for hindi
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

if __name__ == '__main__':
    #print('PyCharm')
    say("Hello, I am Jarvis A.I.")
    while True:
        query = takeCommand()
        #if "Open YouTube".lower() in query.lower():
        #    say("Opening YouTube Mam..")
        #    webbrowser.open("https://youtube.com")
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"],]
        # todo : add more sites
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Mam..")
                webbrowser.open(site[1])
        # todo: add a feature to play a specific song
        if "open music" in query:
            musicPath = "/Users/shafiyabegum/Downloads/tvari-hawaii-vacation-159069.mp3"
            os.system(f"open {musicPath}")
            #import subprocess, sys
            #opener = "open" if sys.platform == "darwin" else "xdg.open"
            #subprocess.call([opener, musicPath])

        elif "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Mam the time is {strfTime}")

        elif "open facetime".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")
            say("opening FaceTime mam..")

        elif "using Artificial Intelligence".lower() in query.lower():
            #ai(prompt=query)
            if query:
                response = ai(query)
                print(response)
                if not os.path.exists("Openai"):
                    os.mkdir("Openai")
                #with open(f"Openai/query- {random.randint(1, 23434343224)}.txt", "w") as f:
                #with open(f"Openai/{query[0:30]}.txt", "w") as f:
                with open(f"Openai/{''.join(query.split('intelligence')[1:]).strip()}.txt", "w") as f:
                    f.write(response)
                    f.write("hi")

        elif "reset chat".lower() in query.lower():
            chatStr =""

        else:
            chat(query)
        #say(query)

