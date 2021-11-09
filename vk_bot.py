import os
import random
import vk_api as vk
from dialogflow import TextInput, QueryInput, SessionsClient
from vk_api.longpoll import VkLongPoll, VkEventType


def detect_intent_text(session_id, text):
    session_client = SessionsClient()
    session = session_client.session_path(os.environ['PROJECT_ID'], session_id)
    print(session)
    text_input = TextInput(text=text, language_code='ru-RU')
    query_input = QueryInput(text=text_input)
    response = session_client.detect_intent(query_input=query_input, session=session)
    return(response.query_result.fulfillment_text)


def echo(event, vk_api):

    vk_api.messages.send(
        user_id=event.user_id,
        message=detect_intent_text(event.text),
        random_id=random.randint(1,1000)
    )


if __name__ == "__main__":
    vk_session = vk.VkApi(token=os.environ['VK_API_KEY'])
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            echo(event, vk_api)