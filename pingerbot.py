#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time
from random import randint, choice
from time import sleep
import telebot
#from os import environ

#TeleBot = telebot.TeleBot(environ['token'])
TeleBot = telebot.TeleBot('779667318:AAFO_3Ptkf2Y7uYstagrckMrBqpt9criQEo')

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
            user.warn_ping(self)
            self.last_ping_check = cur_time
        
        if self.last_answer_time < self.last_ping_check and cur_time - self.last_ping_check > self.ping_length:
            self.emergency_level += 1
            self.last_answer_time
            self.user.warn_emergency(self)
            for pinger in self.pingers:
                pinger.warn_ping_not_given(self)


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

    def warn_ping(self, situation):
        TeleBot.send_message(self.chat_id, 'Ping time for {}!'.format(self.name))

    def warn_ping_not_given(self, situation):
        TeleBot.send_message(self.chat_id, 'Person is having trouble in {}!'.format(self.name))
        self.send_emergency_text(situation)

    def warn_emergency(self, situation):
        TeleBot.send_message(self.user.chat_id, 'Emergency was sent for {}!'.format(self.name))
        self.send_emergency_text(situation)

    def send_emergency_text(self, situation):
        if self.emergency_level >= len(self.emergency_texts):
            TeleBot.send_message(pinger.chat_id, 'Maximum emergency for {}!'.format(situation.name))
        else:
            TeleBot.send_message(pinger.chat_id, situation.emergency_texts[situation.emergency_level])


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
            TeleBot.send_message(chat.id, 'Hola!')
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
    
    
            
    