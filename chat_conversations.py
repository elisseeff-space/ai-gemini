import os
import google.generativeai as genai
from google.api_core import retry

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
response = None
#response = chat.send_message("Okay, how about a more detailed explanation to a high schooler?", stream=True)
response = chat.send_message("Грэмми - это, конечно, хрень какая-то. Очевидно же, что лучший рок-альбом прошлого года - это Life is But a Dream... группы Avenged Sevenfold. А они их даже номинировать забыли.", stream=True, safety_settings={'HARASSMENT':'block_none'})

print(response.prompt_feedback)
input()

for chunk in response:
  print(chunk.text)
  print("_"*80)


#print(chat.history)

#print(len(chat.history))