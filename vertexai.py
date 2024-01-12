def init_sample(
    project: Optional[str] = None,
    location: Optional[str] = None,
    experiment: Optional[str] = None,
    staging_bucket: Optional[str] = None,
    credentials: Optional[auth_credentials.Credentials] = None,
    encryption_spec_key_name: Optional[str] = None,
    service_account: Optional[str] = None,
):

    from google.cloud import aiplatform

    aiplatform.init(
        project=project,
        location=location,
        experiment=experiment,
        staging_bucket=staging_bucket,
        credentials=credentials,
        encryption_spec_key_name=encryption_spec_key_name,
        service_account=service_account,
    )


#from google.cloud import aiplatform
from google.cloud import aiplatform, aiplatform_v1beta1
import vertexai
import vertexai.preview
from vertexai.preview.generative_models import GenerativeModel, ChatSession
from vertexai.language_models import ChatModel, InputOutputTextPair

# TODO(developer): Update and un-comment below lines
#project_id = "PROJECT_ID"
project_id = "ai-elis-project"
location = "us-central1"
aipl = aiplatform.init(project=project_id, location=location)

model = aipl.GenerativeModel("gemini-pro")
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