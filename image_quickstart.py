import PIL.Image
import os
import textwrap

import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro-vision')

img = PIL.Image.open('voice-ai.jpg')

response = model.generate_content(img)
print(model.count_tokens(img))

#display(to_markdown(response.text))
print(response.text)