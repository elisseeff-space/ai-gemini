#from google.cloud import aiplatform
from google.cloud import aiplatform, aiplatform_v1beta1
import vertexai
import vertexai.preview
from vertexai.preview.generative_models import GenerativeModel, ChatSession
from vertexai.language_models import ChatModel, InputOutputTextPair

# TODO(developer): Update and un-comment below lines
project_id = "PROJECT_ID"
location = "us-central1"
vertexai.init(project='ai-elis-project', location=location)

model = GenerativeModel("gemini-pro")
chat = model.start_chat()

def get_chat_response(chat: ChatSession, prompt: str) -> str:
    response = chat.send_message(prompt)
    return response.text

prompt = "Hello."
print(get_chat_response(chat, prompt))

prompt = "What are all the colors in a rainbow?"
print(get_chat_response(chat, prompt))

prompt = "Why does it appear when it rains?"
print(get_chat_response(chat, prompt))