from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

YourBuddy=ChatBot('Bot')
#YourBuddy.set_trainer(ListTrainer)

'''
for files in os.listdir('C:/Users/pc/Desktop/chatterbot-corpus-master\chatterbot_corpus\data\english/'):
    data=open('C:/Users/pc/Desktop/chatterbot-corpus-master\chatterbot_corpus\data\english/'+files,'r').readlines()
    YourBuddy.train(data)
  '''
'''
trainer = ChatterBotCorpusTrainer(YourBuddy)
trainer.train("chatterbot.corpus.english")  
'''
while(True):
    message=input('You:')
    if(message.strip() != 'Bye' or message.strip()!='bye' or message.strip()!='BYE'):
        reply=YourBuddy.get_response(message)
        print('YourBuddy: ',reply)
    if(message.strip() == 'Bye' or message.strip()=='bye' or message.strip()=='BYE'):
        print('YourBuddy: Bye')
        break
        
    
    
    