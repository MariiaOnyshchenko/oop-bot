import random
import re
import json
from json import JSONEncoder
class ChatBot:
    responses={
    'вставні фрази':['Гм, цікавий вибір.', 'Чудовий вибір!', 
                     'Вас справді це цікавить? Ну що ж, най буде.'],
    'помилки':['Перепрошую, але я не знаю таких команд:(',
               'Що-що? Не розумію:('],
    'прощання':['Був радий поспілкуватись!', 'До зустрічі!',
                'На все добре, гарного дня!']}
    
    themes={'math':{'площа кола':s_circle, 'площа прямокутника':s_rectangle,
                    }, 
            'physics':{}, 
            'geography':{}, 
            'philology':{},
            'text':{}, 
            'general':{}}
    
    __instance = None
    def __new__(cls):
        if (cls.__instance is None):
            cls.__instance = super(ChatBot, cls).__new__(cls)
        return cls.__instance
    
    def greetings (self):
      print ('''Вітаю, мене звати Мудрагель. Ви можете задати мені питання з 
наступних тем: математика, фізика, філологія, географія, робота з текстом, загальне.
Будь ласка, введіть назву теми, на яку б ви хотіли поспілкуватись; 
Для виходу введіть "вихід".
Для повернення на вибір вище, введіть "назад".''')
      
    def exit(self, reply):
        if reply == 'вихід':
            print (random.choice(self.responses['прощання']))

    def chat(self):
        reply = input().lower()
        while not self.exit(reply):
            reply = input().lower()
    

a1 = ChatBot() 

class MyEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__  
MyEncoder().encode(a1)
json.dumps(a1, cls=MyEncoder)

with open("sample.json", "w") as outfile:
    outfile.write(a1)

  
