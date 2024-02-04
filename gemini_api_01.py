import os
import google.generativeai as genai
from google.api_core import retry
import numpy as np


@retry.Retry()
def retry_chat(**kwargs):
  return genai.chat(**kwargs)

@retry.Retry()
def retry_reply(self, arg):
  return self.reply(arg)

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

models = [m for m in genai.list_models() if 'generateMessage' in m.supported_generation_methods]
model = models[0].name
print(model)

question = """
I have 77 houses, each with 31 cats.
Each cat owns 14 mittens, and 6 hats.
Each mitten was knit from 141m of yarn, each hat from 55m.
How much yarn was needed to make all the items?
At the end write out a single expression to compute the answer.

Think about it step by step, and show your work.
"""

response = retry_chat(
    model=model,
    context="You are an expert at solving word problems.",
    messages=question,
)

print(response.last)