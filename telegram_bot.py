import os
import logging
from dialogflow_v2 import SessionsClient
from dialogflow_v2.types import TextInput, QueryInput
from telegram import Update
from telegram.ext import Updater, CommandHandler,\
    MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv


load_dotenv()


def detect_intent_text(session_id, text):
    session_client = SessionsClient()
    session = session_client.session_path(os.environ['PROJECT_ID'], session_id)
    text_input = TextInput(text=text, language_code='ru')
    query_input = QueryInput(text=text_input)
    response = session_client.detect_intent(query_input=query_input,
                                            session=session)
    return(response.query_result.fulfillment_text)


def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Здравствуйте, {user.mention_markdown_v2()}\!'
    )


def help_command(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext):
    """Echo the user message."""
    try:
        update.message.reply_text(detect_intent_text(
            update.message.chat_id, update.message.text
        ))
    except Exception as error:
        print(f'Problems with DiagFlow: {error}')


updater = Updater(os.environ['TELEGRAM_TOKEN'])
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help_command))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
updater.start_polling()
updater.idle()
