import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import google.generativeai as genai
import random
from flask import Flask, request, jsonify
from flask_cors import CORS
import serial
import time

chatStr = " "

def chat(query):
    global chatStr
    print(chatStr)
    genai.configure(api_key="AIzaSyAmg262dKa4jCGyzvwfLyIZN-wYbRtV5DA")
    chatStr += f"Shafiya: {query}\n Jarvis: "
    #chatStr += "Shafiya: " + query + "\n Jarvis:"

    #text = f"OpenAi response for Prompt: {query}\n ******* \n\n"
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
        #    "## Resignation Email Template\n\n*Subject: Resignation - [Your Name]*\n\nDear [Boss's name],\n\nPlease accept this email as formal notification that I am resigning from my position as [Your job title] at [Company name]. My last day of employment will be [Your last day - typically two weeks from the date you give notice]. \n\nThank you for the opportunity to work at [Company name] for the past [Length of employment]. I've enjoyed my time here and appreciate the opportunities I've had to [Mention something you learned or a positive experience]. \n\n[Optional: Briefly state your reason for leaving, e.g., I am pursuing a new opportunity that aligns more closely with my long-term career goals.]\n\nPlease let me know if there is anything I can do to help ensure a smooth transition during this time. \n\nI wish you and the company all the best in the future.\n\nSincerely,\n\n[Your Name]"]
        # },
    ])
    convo.send_message("YOUR_USER_INPUT")
    # say(convo.last.text)
    # response = convo.last.text
    # chatStr += f"{response}\n"
    chatStr += f"{convo.last.text}\n"
    return convo.last.text
    with open(f"Openai/{''.join(query.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(response)

# ser = serial.Serial('COM3', 9600)
# time.sleep(2)

# Green = 6
# #Orange = 4
# Red = 5

app = Flask(__name__)
CORS(app, origins='http://localhost:59597')
@app.route('/process_voice_input', methods=['POST'])
# @app.route('/lights', methods=['POST'])

# def send_voice_command(command):
#     ser.write(command.encode('utf-8'))


# def lights():
#     data = request.json

#     while True:
#         if ser.in_waiting > 0:
#             # voice = ser.readline().decode('utf-8').strip()
#             voice = data.get('voiceInput')
#             print(voice)

#             if voice == "green":
#                 send_voice_command("green")
#             elif voice == "green off":
#                 send_voice_command("green off")

#             if voice == "orange":
#                 send_voice_command("orange")
#             elif voice == "orange off":
#                 send_voice_command("orange off")

#             if voice == "red":
#                 send_voice_command("red")
#             elif voice == "red off":
#                 send_voice_command("red off")

# # Close serial connection
#     ser.close()

def process_voice_input():
    print("started")
    data = request.json
    print(data)
    voice_input = data.get('voiceInput')
    query = voice_input.upper()
    response = chat(query)
   
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)