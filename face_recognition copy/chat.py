from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


bot = ChatBot('Buddy', logic_adapters = [
                 {
                     'import_path': 'chatterbot.logic.BestMatch',
                     'default_response': 'I am sorry, I do not understand. I am still learning. Please contact doctor from our chat window for further assistance.',
                     'maximum_similarity_threshold': 0.90
                 }
             ],
             read_only = True,
             preprocessors=['chatterbot.preprocessors.clean_whitespace',
'chatterbot.preprocessors.unescape_html',
'chatterbot.preprocessors.convert_to_ascii'])

trainer = ListTrainer(bot)

trainer.train([
"Hi, can I help you",
    "Who are you?",
    "I am your virtual assistant. Ask me any questions...",
    "Where do you operate?",
    "We operate from Singapore",
    "What payment methods do you accept?",
    "We accept debit cards and major credit cards",
    "I would like to speak to your customer service agent",
    "please call +65 3333 3333. Our operating hours are from 9am to 5pm, Monday to Friday"



])
trainer.train([
    "What payment methods do you offer?",
    "We accept debit cards and major credit cards",
    "How to contact customer service agent",
    "please call +65 3333 3333. Our operating hours are from 9am to 5pm, Monday to Friday"
    
])
conv = open('Output.txt','r').readlines()
trainer.train(conv)


trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')

name = input('Enter Your Name: ')
print ('Welcome to Doctris Chatbot Service! Let me know how can I help you')

while True:
    
    request = input(name+':')
    
    if request=="Bye" or request=='bye':
        print('Bot: Bye')
        break
    else:
        response=bot.get_response(request)
        print('Bot: ', response)
"""

response = bot.get_response ("From where do you work?")
print(response)
"""

