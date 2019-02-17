import time
from random import randint, choice
from time import sleep
import telebot
from os import environ

TeleBot = telebot.TeleBot(environ['token'])

PING = 1
PONG = -1

USERS = {}

class Situation:
    max_id = -1
    def __init__(self, user, danger_status, start_time, end_time, ping_freq, ping_length, emergency_texts=[], name='NoName'):
        self.user = user
        self.danger_status = danger_status
        self.start_time = start_time
        self.end_time = end_time
        self.ping_freq = ping_freq
        self.ping_length = ping_length
        
        self.pingers = []
        
        self.emergency_texts = emergency_texts
        self.emergency_level = 0
        
        self.last_ping_check = time.time()
        self.last_answer_time = time.time()
        self.last_user_answer_time = time.time()
        self.last_answer_type = PING
        
        self.name = name
        
    def check(self):
        cur_time = time.time()
        
        if cur_time - self.last_ping_check > self.ping_freq:
            TeleBot.send_message(self.user.chat_id, 'Check time for {}!'.format(self.name))
            self.last_ping_check = cur_time
        
        if self.last_answer_time - self.last_ping_check < 0 and cur_time - self.last_ping_check > self.ping_length:
            self.emergency_level += 1
            self.last_answer_time
            TeleBot.send_message(self.user.chat_id, 'Emergency for {}!'.format(self.name))
            for pinger in self.pingers:
                if self.emergency_level >= len(self.emergency_texts):
                    TeleBot.send_message(pinger.chat_id, 'Maximum emergency for {}!'.format(self.name))
                else:
                    TeleBot.send_message(pinger.chat_id, self.emergency_texts[self.emergency_level])


class User:
    max_id = -1
    def __init__(self, chat_id, tg_login):
        User.max_id += 1
        self.id = User.max_id
        self.chat_id = chat_id
        self.tg_login = login
        
        self.situations = []
        self.friends = []
        self.pingers = []
        self.extreme_pingers = []


def user_by_id(user_id):
    if user_id in USERS:
        return USERS[user_id]
    else:
        return None
    

def register_user(user, chat):
    if not user is None:
        return 0
    else:
        USERS[chat.id] = User(char.id, chat.first_name)


@TeleBot.message_handler(func=lambda x: True)
def message_handler(message):
    if TO_STOP:
        print('ok')
        exit(0)

    chat = message.chat
    text = message.text
    user = user_by_id(chat.id)
    print('{}: {}'.format(chat.first_name, text))
    
    if user is None:
        if text != '/start':
            TeleBot.send_message(chat.id, 'Напишите мне, пожалуйста, /start, чтобы я добавил вас в список пользователей')
            return 0
        else:
            register_user(user, chat)
    elif text == '/start':
        return 0
    

def main():
    global USERS
    USERS = {}
    TeleBot.polling(interval=1)


if __name__ == "__main__":
    main()
    
    
            
    