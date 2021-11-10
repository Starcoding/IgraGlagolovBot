import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (CallbackContext, CommandHandler, Filters,
                          MessageHandler, Updater)

from dialogflow_api import detect_intent_text


def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Здравствуйте, {user.mention_markdown_v2()}\!'
    )


def help_command(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def answer_to_user(update: Update, context: CallbackContext):
    """Answer to user with DialogFlow responce"""
    _, reply_text = detect_intent_text(
        f'tg-{update.message.chat_id}', update.message.text
    )
    update.message.reply_text(reply_text)


def error_handler(update: Update, context: CallbackContext):
    print(f'Update: {update}.\nError: {context.error}.')


def main():
    load_dotenv()
    updater = Updater(os.environ['TELEGRAM_TOKEN'])
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_error_handler(error_handler)
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, answer_to_user))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
