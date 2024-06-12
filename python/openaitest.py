# import os
# #import openai
# from config import apikey
# from openai import OpenAI
# client = OpenAI()
# OpenAI.api_key = apikey
# OpenAI.api_key = os.getenv("OPENAI_API_KEY")
# response = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     prompt="Write an email to my boss for resignation?",
#     temperature=1,
#     max_tokens=256,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
# )
#
# print(response)

#

# import openai
# from config import apikey
#
#
# openai.api_key = apikey
#
# response = openai.Completion.create(
#     model="gpt-3.5-turbo",
#     prompt="what is the color of apple?",
#     temperature=1,
#     max_tokens=256,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
# )
# print(response)

import os
# import openai
# from config import apikey
#
# openai.api_key = apikey
#
# response = openai.Completion.create(
#   model="gpt-3.5-turbo",
#   prompt="Write an email to my boss for resignation?",
#   temperature=0.7,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )
#
# print(response)
# '''
# {
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "logprobs": null,
#       "text": "\n\nSubject: Resignation\n\nDear [Name],\n\nI am writing to inform you of my intention to resign from my current position at [Company]. My last day of work will be [date].\n\nI have enjoyed my time at [Company], and I am grateful for the opportunity to work here. I have learned a great deal during my time in this position, and I am grateful for the experience.\n\nIf I can be of any assistance during this transition, please do not hesitate to ask.\n\nThank you for your understanding.\n\nSincerely,\n[Your Name]"
#     }
#   ],
#   "created": 1683815400,
#   "id": "cmpl-7F1aqg7BkzIY8vBnCxYQh8Xp4wO85",
#   "model": "text-davinci-003",
#   "object": "text_completion",
#   "usage": {
#     "completion_tokens": 125,
#     "prompt_tokens": 9,
#     "total_tokens": 134
#   }
# }
# '''

"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="AIzaSyAmg262dKa4jCGyzvwfLyIZN-wYbRtV5DA")

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
    "parts": ["What is the color od apple"]
  },
  # {
  #   "role": "model",
  #   "parts": ["## Resignation Email Template\n\n**Subject: Resignation - [Your Name]**\n\nDear [Boss's name],\n\nPlease accept this email as formal notification that I am resigning from my position as [Your job title] at [Company name]. My last day of employment will be [Your last day - typically two weeks from the date you give notice]. \n\nThank you for the opportunity to work at [Company name] for the past [Length of employment]. I've enjoyed my time here and appreciate the opportunities I've had to [Mention something you learned or a positive experience]. \n\n[Optional: Briefly state your reason for leaving, e.g., I am pursuing a new opportunity that aligns more closely with my long-term career goals.]\n\nPlease let me know if there is anything I can do to help ensure a smooth transition during this time. \n\nI wish you and the company all the best in the future.\n\nSincerely,\n\n[Your Name]"]
  # },
])

convo.send_message("YOUR_USER_INPUT")
print(convo.last.text)
