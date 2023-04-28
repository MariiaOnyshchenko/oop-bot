class ChatBot:
    __instance = None
    def __new__(cls):
        if (cls.__instance is None):
            cls.__instance = super(ChatBot, cls).__new__(cls)
        return cls.__instance


print ('''Вітаю, мене звати Мудргель. Ви можете задати мені питання з 
наступних тем: математика, фізика, філологія, географія.''')

while (True):  
    user_input = input().lower()

    if user_input == 'вихід': 
        print ("Радий був поспілкуватись, до зустрічі.")
        break    
    matched_intent = None 
    for intent, pattern in keywords_dict.items():

            matched_intent=intent  
    key='fallback' 
    if matched_intent in responses:
        key = matched_intent
    # The chatbot prints the response that matches the selected intent
    print (responses[key]) 