import nltk
import random
from nltk.chat.util import Chat, reflections
from nltk.tokenize import sent_tokenize, word_tokenize
import unicodedata

respostas = ["Nós temos livros de ação", "Nós temos livros de terror"] ## pelo pares

perguntas_user = input()

def tokenizar_perguntas_usuario(perguntas_user, respostas):
    token_sentenca = sent_tokenize(perguntas_user)
    print(token_sentenca)

    for token in token_sentenca:
        token_palavra_pergunta = word_tokenize(token)
        print(token_palavra_pergunta)

    # for sentencas_respostas in respostas:
    #     token_respostas = sent_tokenize(sentencas_respostas)

    #     for palavras_respostas in token_respostas:
    #         token_palavras_respostas = word_tokenize(palavras_respostas)

    if {"quero", "livro"}.issubset(token_palavra_pergunta):
        return "Entendi! Me explique mais a respeito do gênero e do livro!"
    elif{"terror"}.issubset(token_palavra_pergunta):
        return "Nós temos livros de terror! Qual tipo de terror você curte?"
    return None

tokenizar_perguntas_usuario(perguntas_user, respostas)

while True:
    resposta_token = tokenizar_perguntas_usuario(perguntas_user, respostas)
    if resposta_token:
        print("ChatBot: ", resposta_token)
    else:
        print("ChatBot: Desculpe, não entendi.")