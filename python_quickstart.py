import os, time
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

model = genai.GenerativeModel('gemini-pro')

start_time = time.time()
response = model.generate_content("What is the meaning of life?", stream=True)
#print(response.text)
#print(response.candidates)
end_time = time.time()

for chunk in response:
  print(chunk.text)
  print("_"*80)

# Print the elapsed time
print("Execution time:", end_time-start_time, "seconds.")