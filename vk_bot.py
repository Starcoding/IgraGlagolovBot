import os
import random
import vk_api as vk
from dialogflow_v2 import SessionsClient
from dialogflow_v2.types import TextInput, QueryInput
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv


load_dotenv()


def detect_intent_text(session_id, text):
    session_client = SessionsClient()
    session = session_client.session_path(os.environ['PROJECT_ID'], session_id)
    text_input = TextInput(text=text, language_code='ru')
    query_input = QueryInput(text=text_input)
    response = session_client.detect_intent(query_input=query_input,
                                            session=session)
    if not response.query_result.intent.is_fallback:
        return response.query_result.fulfillment_text
    else:
        return False


def answer_to_user(event, vk_api):
    if detect_intent_text(event.user_id, event.text):
        vk_api.messages.send(user_id=event.user_id,
                             message=detect_intent_text(
                                 event.user_id, event.text),
                             random_id=random.randint(1, 1000))


vk_session = vk.VkApi(token=os.environ['VK_API_KEY'])
vk_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        answer_to_user(event, vk_api)
