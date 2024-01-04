import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part

def generate():
  model = GenerativeModel("gemini-pro")
  responses = model.generate_content(
    """hi, what is newton theory""",
    generation_config={
        "max_output_tokens": 2048,
        "temperature": 0.9,
        "top_p": 1
    },
  stream=True,
  )
  
  for response in responses:
      print(response.candidates[0].content.parts[0].text)


generate()
