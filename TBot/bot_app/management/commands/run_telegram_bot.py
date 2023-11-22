import telebot
from bot_app.models import Osvencim
from django.core.management.base import BaseCommand

bot = telebot.TeleBot("6529671014:AAHai1uc2ujLgIJq8cZyxshcOJkAfFiozGE")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'message')

@bot.message_handler(commands=['choise'])
def choise(message):
    choises = Osvencim.objects.all()
    for choise in choises:
        bot.send_message(message.chat.id, choise.type_of_execution)

class Command(BaseCommand):
    def handle(self, *args, **options):
        print('starting bot...')
        bot.polling()
        print('bot stoped')