import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.chat.util import Chat,reflections
from pares import pares_lista

pares = pares_lista
chatbot = Chat(pares)

def obter_resposta(mensagem):
    if mensagem.lower() == "sair":
        return "Adeus! Se precisar de algo relacionado a livros novamente pode contar comigo!"
    resposta_token = responder_personalizada(mensagem)
    if resposta_token:
        return resposta_token
    resposta_padrao = chatbot.respond(mensagem)
    if resposta_padrao:
        return resposta_padrao
    else:
        return "Desculpe, não entendi. Pode responder de outra forma por favor?"

def responder_personalizada(usuario_input):
    tokens_usuario = word_tokenize(usuario_input.lower())