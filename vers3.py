import random
import re
import math
import json
from json import JSONEncoder
import logging
import sys
import pickle 

from colorama import Fore, Back, Style
class MyEncoder(JSONEncoder):
    def default (self, obj):
      return obj.__dict__  
class ChatEntry:
    def __init__(self, role, content):
        self.role = role
        self.content = content
class Chat:
    def __add_user_entry(self, content):
        self.entries.append(ChatEntry('user', content)) 
    def __add_system_entry(self, content):
        self.entries.append(ChatEntry('system', content))
    def __init__(self):
        self.entries = []

    def read_input(self):
        input_str= input(f'{Fore.LIGHTMAGENTA_EX}Користувач: ').lower()
        self.__add_user_entry(input_str)
        f.write(f'Користувач: {input_str}\n')
        return input_str
    def write_answer(self, content):
        print(f'{Fore.CYAN}Мудрагель: {content}')
        self.__add_system_entry(content)
        f.write(f'Мудрагель: {content}\n')
    def match_reply(self, content):

        #math
        def math_description(self):
            return f'''Ви обрали тему «Математика». 
Ви можете задати  мені питання з наступних підтем: 
відстань між 2 точками, площа кола, площа прямокутника,
скалярний добуток векторів, координати центра кола за 3 точками.'''

        distance = lambda x1, y1, z1, x2, y2, z2: math.sqrt(pow((x2-x1),2) + pow((y2-y1),2) + pow((z2-z1),2))
        s_rectangle = lambda a, b: a*b
        s_circle = lambda radius: math.pi*(radius**2)
        vectors = lambda A, B, cos_angle: abs(A)*abs(B)*cos_angle
        def center_circle (x1, y1, x2, y2, x3, y3):
            x12 = x1 - x2
            x13 = x1 - x3

            y12 = y1 - y2
            y13 = y1 - y3

            y31 = y3 - y1
            y21 = y2 - y1

            x31 = x3 - x1
            x21 = x2 - x1

            # x1^2 - x3^2
            sx13 = pow(x1, 2) - pow(x3, 2)

            # y1^2 - y3^2
            sy13 = pow(y1, 2) - pow(y3, 2)

            sx21 = pow(x2, 2) - pow(x1, 2)
            sy21 = pow(y2, 2) - pow(y1, 2)

            f = (((sx13) * (x12) + (sy13) *
                (x12) + (sx21) * (x13) +
                (sy21) * (x13)) // (2 *
                ((y31) * (x12) - (y21) * (x13))))
                    
            g = (((sx13) * (y12) + (sy13) * (y12) +
                (sx21) * (y13) + (sy21) * (y13)) //
                (2 * ((x31) * (y12) - (x21) * (y13))))

            return f"Центр = ({-g,},{-f})"
        
        #physics
        def phys_description(self):
            return f'''Ви обрали тему «Фізика». 
Ви можете задати  мені питання з наступних підтем: 
закон всесвітнього тяжіння, Закон Стефана-Больцмана.'''

        gravity = lambda m1, m2, r: ((10**-11)*6.673*m1*m2)/(r**2)
        stef_bolz= lambda A, T: (10**-8)*5.6704*A*(T**4)

        #geography
        def geo_description(self):
            return f'''Ви обрали тему «Географія». 
Ви можете задати  мені питання з наступних підтем: 
найбільший материк, азимут від точки А(х1, у1) до точки В(х2, у2)'''

        def bearing (llat1, llong1, llat2, llong2):
            
            #в радіанах
            lat1 = llat1*math.pi/180.
            lat2 = llat2*math.pi/180.
            long1 = llong1*math.pi/180.
            long2 = llong2*math.pi/180.
            
            #косинуси та синусити широт і різниці довгот 
            cl1 = math.cos(lat1)
            cl2 = math.cos(lat2)
            sl1 = math.sin(lat1)
            sl2 = math.sin(lat2)
            delta = long2 - long1
            cdelta = math.cos(delta)
            sdelta = math.sin(delta)
            
            #обчислення початкового азимуту
            x = (cl1*sl2) - (sl1*cl2*cdelta)
            y = sdelta*cl2
            z = math.degrees(math.atan(-y/x))
            
            if (x < 0):
                z = z+180.
            
            z2 = (z+180.) % 360. - 180.
            z2 = - math.radians(z2)
            anglerad2 = z2 - ((2*math.pi)*math.floor((z2/(2*math.pi))) )
            angledeg = (anglerad2*180.)/math.pi

            return angledeg
        
        def mainland(self):
            return 'Євразія'
        #philology
        def phil_description(self):
            return f'''Ви обрали тему «Філологія». 
Ви можете задати  мені питання з наступних підтем: 
різниця між Present Simple та Present Continuous, відмінки в українській мові, утворення дієслів. '''
        def simpcont(self):
            return '''Present Simple означає певну періодичність, сталість, 
а Present Continuous – це хвилинна дія в даний момент.'''
        def declensions(self):
            return '''Називний, Родовий, Давальний, Знахідний,
Орудний, Місцевий, Кличний.
            '''
        def dative_case(self):
            return '''В давальному відмінку однини іменники мають закінчення 
-ові (-еві, -єві), -у (-ю), -і (-ї, -яті, -аті, -ені). Закінчення 
залежить від роду, відміни та закінчення в Н.в.'''
        

        themes={'математика':{'опис':math_description,'площа кола':s_circle, 'площа прямокутника':s_rectangle,
                        'відстань між 2 точками':distance, 
                        'скалярний добуток векторів':vectors, 'координати центра кола за 3 точками':center_circle}, 
                'фізика':{'опис':phys_description, 'закон всесвітнього тяжіння':gravity, 
                          'закон стефана-больцмана': stef_bolz}, 
                'географія':{'опис':geo_description, 'азимут від точки А(х1, у1) до точки В(х2, у2)':bearing, 'найбільший материк':mainland}, 
                'філологія':{'опис':phil_description, 'різниця між Present Simple та Present Continuous':simpcont, 'відмінки в українській мові':declensions, 'утворення дієслів': dative_case},
                'робота з текстом':{}, 
                'загальне':{}}
        inside_phrases = ['Гм, цікавий вибір. Введіть параметри за необхідності: ', 'Чудовий вибір! Введіть параметри за необхідності: ', 
                     'Вас справді це цікавить? Ну що ж, най буде. Введіть параметри за необхідності: ']
        error_phrases = ['Перепрошую, але я не знаю таких команд:(',
               'Що-що? Не розумію:(', 'Ем... шо?']
        while True:
            if content in themes.keys():
                self.write_answer(themes[content]['опис'](self))
                theme = content
                while True:
                    subtheme = self.read_input()
                    if subtheme in themes[theme].keys():
                        self.write_answer(random.choice(inside_phrases))
                        parameter = self.read_input()
                        if parameter == 'назад':
                            content='назад'
                            break
                        elif parameter == 'вихід':
                            content='вихід'
                            break
                        else:
                            try:
                                self.write_answer(themes[theme][subtheme](*map(float,parameter.split())))
                                continue
                            except:
                                self.write_answer(themes[theme][subtheme](self))
                                continue
                    elif subtheme == 'вихід':
                        content='вихід'
                        break
                    elif subtheme == 'назад':
                        content='назад'
                        break
                    else:
                        self.write_answer(random.choice(error_phrases))
                        continue
            if content=='вихід':
                return self.write_answer('Впевнені? Якщо так, введіть вихід ще раз. ')
            if content=='назад':
                return self.write_answer('''Ви можете задати мені питання з 
наступних тем: математика, фізика, філологія, географія, робота з текстом, загальне.
Будь ласка, введіть назву теми, на яку б ви хотіли поспілкуватись:''')
            else: 
                return self.write_answer(random.choice(error_phrases))
                
    def exit(self):
        farewells=['Був радий поспілкуватись!', 'До зустрічі!',
                'На все добре, гарного дня!', 'Ну нарешті...', 'Чао-какао!']
        content = random.choice(farewells)
        return content
f = open("chat_hist_t.txt", "w", encoding='utf-8')
chat = Chat()

chat.write_answer ('''Вітаю, мене звати Мудрагель. Ви можете задати мені питання з 
наступних тем: математика, фізика, філологія, географія, робота з текстом, загальне.
Будь ласка, введіть назву теми, на яку б ви хотіли поспілкуватись; 
Для виходу введіть "вихід".
Для повернення на вибір вище введіть "назад".''')

while True:
    user_input = chat.read_input()
    if user_input == 'вихід':
        chat.write_answer(chat.exit())
        break
    chat.match_reply(user_input)

with open('chat_hist_j.json', 'w') as file_json:
    json.dump(chat, file_json, cls = MyEncoder)

f.close()