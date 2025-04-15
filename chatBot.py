import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.chat.util import Chat, reflections
from pares import pares_lista

respostas_chatBot = {
    # "oi": "TESTE",
    # "quero" : "Ótimo! Qual gênero você quer?"
    # "ação": "Temos ótimos livros de ação como 'Missão Impossível'.",
    # "romance": "Recomendo 'Orgulho e Preconceito' se você gosta de romance.",
    # "terror": "Ah, livros de terror? 'O Iluminado' é um clássico assustador!",
    # "aventura": "Para aventuras épicas, indico 'As Crônicas de Nárnia'.",
    # "ficção": "Ficção científica? Que tal 'Duna'?",
}

# reflections = {
#     "eu": "você",
#     "meu": "seu",
#     "meus": "seus",
#     "sou": "é",
#     "estou": "está",
#     "fui": "foi",
#     "era": "foi",
#     "você": "eu",
#     "você é": "eu sou",
#     "você está": "eu estou",
# }

pares = pares_lista

chatbot = Chat(pares)

def gerar_resposta(usuario_input):
    tokens_usuario = word_tokenize(usuario_input.lower())
    
    for palavras_chaves in respostas_chatBot:
        if palavras_chaves in tokens_usuario:
            resposta_chat = respostas_chatBot[palavras_chaves]
            return f"{resposta_chat}"

    resposta_padrao = chatbot.respond(usuario_input)
    if resposta_padrao:
        return resposta_padrao
    else:
        return "Desculpe, não entendi. Pode responder de outra forma por favor?"
