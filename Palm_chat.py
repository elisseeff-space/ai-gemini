import google.generativeai as genai
import os, time

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

# Create a new conversation
response = genai.chat(messages='Hi! Do you like Python?')

# Last contains the model's response:
print(response.last)

response = response.reply("Just chillin'")

print(response.last)

print(response.messages)