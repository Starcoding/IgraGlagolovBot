import os
import random

import vk_api as vk
from dotenv import load_dotenv
from vk_api.longpoll import VkEventType, VkLongPoll

from dialogflow_api import detect_intent_text

load_dotenv()


def answer_to_user(event, vk_api):
    if detect_intent_text(event.user_id, event.text, 'vk'):
        vk_api.messages.send(user_id=event.user_id,
                             message=detect_intent_text(f'vk-{event.user_id}',
                                                        event.text),
                             random_id=random.randint(1, 1000))

def main():
    vk_session = vk.VkApi(token=os.environ['VK_API_KEY'])
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            answer_to_user(event, vk_api)

if __name__ == '__main__':
    main()
