import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.chat.util import Chat,reflections
from pares import pares_lista


respostas_chatBot = { # >>>> aqui vamos precisar de tokens mais especificos(como "não sei","estou indeciso" etc), deixando o os gêneros literarios para serem tratados nos pares
    
    # "ação": "Sim! Temos ótimos livros de ação. Você prefere algo mais moderno ou clássico?",
    # "terror": "Temos muitos livros de terror. Gosta mais de terror psicológico ou sobrenatural?",
    # "romance": "Claro! Nossos romances são bem variados. Você gosta de histórias contemporâneas ou de época?",
    # "livro": "Temos vários gêneros. Está procurando algo leve ou mais intenso?",
}

# perguntas_chatBot = [
#     "Qual gênero você mais gosta?",
#     "Você prefere livros longos ou curtos?",
#     "Está procurando por um autor específico?",
#     "Quer recomendações com base em best-sellers?",
# ]

# perguntas_user = input()

def responder_personalizada(usuario_input): # >>>> essa função permanece quase igual(agora ela retorna None se não houver resposta adequada nos tokens). Ela vai controlar as respostas com tokens quando tivermos
    tokens_usuario = word_tokenize(usuario_input.lower())
    
    for palavras_chaves in respostas_chatBot:
        if palavras_chaves in tokens_usuario:
            resposta_chat = respostas_chatBot[palavras_chaves]
            # nova_pergunta = random.choice(perguntas_chatBot)
            # return f"{resposta} {nova_pergunta}"
            return f"{resposta_chat}"
    
    return None

# Loop do chatbot
print("ChatBot: Olá! Eu posso te ajudar a encontrar diversos livro.Qual gênero literário você procura?")

# while True:
#     entrada_usuario = input("Você: ")
#     resposta_chat = responder(entrada_usuario)
#     print("ChatBot:", resposta_chat)

reflections = { # >>>> por mais que não usemos agora, coloquei aqui para poder instanciar um objeto 'Chat' do nltk, que recebe reflections como parametro
    "eu":"você",
    "meu":"seu",
    "meus":"seus",
    "sou":"é",
    "estou":"está",
    "fui":"foi",
    "era":"foi",
    "você":"eu",
    "você é":"eu sou",
    "você está":"eu estou",
}

pares = pares_lista

chatbot = Chat(pares, reflections)

while True:
    entrada_usuario = input("Voce: ")
    if entrada_usuario == "sair":
        print("ChatBook: Adeus! Se precisar de algo relacionado a livros novamente pode contar comigo!")
        break
    resposta_token = responder_personalizada(entrada_usuario)
    if resposta_token: # >>>> prioriza respostas com token. Caso não tenha nenhuma entra no else e usa os pares
        print("ChatBook: ", resposta_token)
    else:
        resposta_padrao = chatbot.respond(entrada_usuario)
        if resposta_padrao:
            print("ChatBook: ", resposta_padrao)
        else:
            print("ChatBook: Desculpe, não entendi. Pode responder de outra forma por favor?")

# def tokenizar_perguntas_usuario(perguntas_user, respostas):
#     token_sentenca = sent_tokenize(perguntas_user)
#     print(token_sentenca)

#     for token in token_sentenca:
#         token_palavra_pergunta = word_tokenize(token)
#         print(token_palavra_pergunta)

#     # for sentencas_respostas in respostas:
#     #     token_respostas = sent_tokenize(sentencas_respostas)

#     #     for palavras_respostas in token_respostas:
#     #         token_palavras_respostas = word_tokenize(palavras_respostas)

#     if {"quero", "livro"}.issubset(token_palavra_pergunta):
#         return "Entendi! Me explique mais a respeito do gênero e do livro!"
#     elif{"terror"}.issubset(token_palavra_pergunta):
#         return "Nós temos livros de terror! Qual tipo de terror você curte?"
#     return None

# tokenizar_perguntas_usuario(perguntas_user, respostas)

# while True:
#     resposta_token = tokenizar_perguntas_usuario(perguntas_user, respostas)
#     if resposta_token:
#         print("ChatBot: ", resposta_token)
#     else:
#         print("ChatBot: Desculpe, não entendi.")