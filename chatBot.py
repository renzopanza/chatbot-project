import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.chat.util import Chat, reflections
from pares import pares_lista

# Dicionário para respostas personalizadas com tokens (você pode preencher com palavras-chave depois)
respostas_chatBot = {
    "ação": "Temos ótimos livros de ação como 'Missão Impossível'.",
    "romance": "Recomendo 'Orgulho e Preconceito' se você gosta de romance.",
    "terror": "Ah, livros de terror? 'O Iluminado' é um clássico assustador!",
    "aventura": "Para aventuras épicas, indico 'As Crônicas de Nárnia'.",
    # "ficção": "Ficção científica? Que tal 'Duna'?",
}

pares = pares_lista

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

chatbot = Chat(pares)

def gerar_resposta(usuario_input):
    tokens_usuario = word_tokenize(usuario_input.lower())
    
    # Verifica por palavras-chave
    for palavras_chaves in respostas_chatBot:
        if palavras_chaves in tokens_usuario:
            resposta_chat = respostas_chatBot[palavras_chaves]
            return f"{resposta_chat}"

    # Caso não encontre palavras-chave, tenta usar os pares
    resposta_padrao = chatbot.respond(usuario_input)
    if resposta_padrao:
        return resposta_padrao
    else:
        return "Desculpe, não entendi. Pode responder de outra forma por favor?"
