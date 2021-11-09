import os
import json
import dialogflow_v2


def create_intent(display_name, training_phrases_parts, message_texts):
    """Create an intent of the given intent type."""
    intents_client = dialogflow_v2.IntentsClient()
    print(dir(dialogflow_v2.AgentsClient))
    parent = dialogflow_v2.AgentsClient.project_path(os.environ['PROJECT_ID'])

    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow_v2.types.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow_v2.types.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow_v2.types.Intent.Message.Text(text=message_texts)
    message = dialogflow_v2.types.Intent.Message(text=text)

    intent = dialogflow_v2.types.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    response = intents_client.create_intent(parent, intent)

    print("Intent created: {}".format(response))


with open('training_phrases.json') as json_file:
    training_phrases = json.load(json_file)

for phrase in training_phrases:
    create_intent(phrase, training_phrases[phrase]['questions'], training_phrases[phrase]['answer'])

