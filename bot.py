import telebot # библиотека telebot
import time
from config import token # импорт токена

bot = telebot.TeleBot(token) 
#тут нужно новую функцию
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот для управления чатом.")

@bot.message_handler(commands=['ban'])
def ban_user(message):
    if message.reply_to_message:
        chat_id = message.chat.id
         # Это я изменил
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status 
         
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно забанить администратора.")
        else:
            bot.ban_chat_member(chat_id, user_id) # 
            bot.reply_to(message, f"Пользователь @{message.reply_to_message.from_user.username} был забанен.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите забанить.")

@bot.message_handler(content_types=['new_chat_members'])
def make_some(message):
    bot.send_message(message.chat.id, 'Я принял нового пользователя!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)

@bot.message_handler(commands=['admin'])
def admin_user(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status 
        #print("Тут все норм")
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно дать администратора администратору.")
            #print("Тут да")
        else:
            #bot.get_chat_administrators(chat_id, user_id) 
            
            bot.reply_to(message, f"Пользователь @{message.reply_to_message.from_user.username} был назначен админом.")
            bot.get_chat_administrators(chat_id)
            
    else:
            bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите забанить.")
            #print("Тут тоже работает")
bot.infinity_polling(none_stop=True)
