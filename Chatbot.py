from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Criação do chatbot
chatbot = ChatBot('MeuBot')

# Treinamento do chatbot com o conjunto de dados em inglês
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

# Função para interação com o usuário
def chat_with_user():
    print("Olá! Eu sou o seu bot. Você pode digitar 'sair' a qualquer momento para encerrar o chat.")
    
    while True:
        user_input = input("Você: ")
        
        if user_input.lower() == 'sair':
            print("Até logo!")
            break

        response = chatbot.get_response(user_input)
        print("Bot:", response)

# Inicia a interação
chat_with_user()
