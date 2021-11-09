import os
import json
import dialogflow
from dotenv import load_dotenv


load_dotenv()

def create_intent(display_name, training_phrases_parts, message_texts):
    """Create an intent of the given intent type."""
    intents_client = dialogflow.IntentsClient()
    parent = dialogflow.AgentsClient.project_path(os.environ['PROJECT_ID'])

    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.types.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.types.Intent.Message.Text(text=message_texts)
    message = dialogflow.types.Intent.Message(text=text)

    intent = dialogflow.types.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    response = intents_client.create_intent(parent, intent)

    print("Intent created: {}".format(response))


with open('training_phrases.json') as json_file:
    training_phrases = json.load(json_file)

for phrase in training_phrases:
    create_intent('igraglagolov', phrase, training_phrases[phrase]['questions'], message_texts=training_phrases[phrase]['answer'])

