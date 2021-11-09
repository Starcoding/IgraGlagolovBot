import os

from dialogflow_v2 import SessionsClient
from dialogflow_v2.types import QueryInput, TextInput
from dotenv import load_dotenv


def detect_intent_text(session_id, text, platform='other'):
    load_dotenv()
    session_client = SessionsClient()
    session = session_client.session_path(os.environ['PROJECT_ID'], session_id)
    text_input = TextInput(text=text, language_code='ru')
    query_input = QueryInput(text=text_input)
    response = session_client.detect_intent(query_input=query_input,
                                            session=session)
    if response.query_result.intent.is_fallback and platform == 'vk':
        return False
    else:
        return response.query_result.fulfillment_text
