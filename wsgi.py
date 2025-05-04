import telebot

from main import bot
from flask import Flask, request
import os

app = Flask(__name__)

# Webhook endpoint
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_data = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_data)
        bot.process_new_updates([update])
        return '', 200
    return 'Invalid content type', 403

# Health check endpoint
@app.route('/')
def health_check():
    return "Bot is running!", 200