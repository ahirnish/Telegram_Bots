#!/usr/bin/python3

from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, MessageHandler, Filters, InlineQueryHandler
import logging
from telegram.ext import CommandHandler
from py_translator import Translator

updater = Updater(token='666459298:AAE0ZjLvafCHULiGRCf1sBDXbiZGOYMSoOc')
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#-------------------------------------------------------------------------------------------------

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hi {}! I'm a bot, please let me translate for you!".format(update.message.chat.first_name))
    bot.send_message(chat_id=update.message.chat_id, text="Click /help for usage.")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def help_text(bot, update):
    message = "Usage:\n/spanish <text in English to be converted to Spanish>\n/english <text in Spanish to be converted to English>"
    bot.send_message(chat_id=update.message.chat_id, text=message)

help_handler = CommandHandler('help', help_text)
dispatcher.add_handler(help_handler)

#-------------------------------------------------------------------------------------------------

def translate_to_spanish(bot, update, args):
    try:
        text = ' '.join(args)
        translated_text = Translator().translate(text=text, dest='es').text
        bot.send_message(chat_id=update.message.chat_id, text=translated_text)
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text="Some error occured during translation.")

translate_to_spanish_handler = CommandHandler('spanish', translate_to_spanish, pass_args=True)
dispatcher.add_handler(translate_to_spanish_handler)

#-------------------------------------------------------------------------------------------------

def translate_to_english(bot, update, args):
    try:
        text = ' '.join(args)
        translated_text = Translator().translate(text=text, dest='en').text
        bot.send_message(chat_id=update.message.chat_id, text=translated_text)
    except Exception as e:
        print(e)
        bot.send_message(chat_id=update.message.chat_id, text="Some error occured during translation.")

translate_to_english_handler = CommandHandler('english', translate_to_english, pass_args=True)
dispatcher.add_handler(translate_to_english_handler)

#-------------------------------------------------------------------------------------------------

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

#-------------------------------------------------------------------------------------------------

updater.start_polling()
print("Started polling...")
