import vertexai
from vertexai.language_models import TextGenerationModel

def streaming_prediction(
  project_id: str,
  location: str,
) -> str:
  """Streaming Text Example with a Large Language Model"""

vertexai.init(project=project_id, location=location)

text_generation_model = TextGenerationModel.from_pretrained("text-bison")
parameters = {
  "temperature": temperature,  # Temperature controls the degree of randomness in token selection.
  "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
  "top_p": 0.8,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
  "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
}

responses = text_generation_model.predict_streaming(prompt="Give me ten interview questions for the role of program manager.", **parameters)
for response in responses:
  print(response)
