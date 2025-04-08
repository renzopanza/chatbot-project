import nltk
import random
from nltk.chat.util import Chat, reflections
from nltk.tokenize import sent_tokenize, word_tokenize


perguntas = ["Olá! Você tem livros de ação?", "Ola! Eu quero comprar um livro!", "Ola! Você tem livros de terror?"]

respostas = ["Nós temos livros de ação", "Nós temos livros de terror"]


# def tokenizar_perguntas(perguntas):
#     for setencas in perguntas:
#         token = sent_tokenize(setencas)
#         print('FOR para tokenizar por sentença')
#         print(token)
#         print(len(token))

#         for palavras in token:
#             token_palavras = word_tokenize(palavras)

#             print('FOR para tokenizar por palavra')
#             print(token_palavras)
#             print(len(token_palavras))

# def tokenizar_respostas(respostas):
#     for sentencas_respostas in respostas:
#         token_respostas = sent_tokenize(sentencas_respostas)
#         print('FOR para tokenizar por sentença')
#         print(token_respostas)
#         print(len(token_respostas))

#         for palavras_respostas in token_respostas:
#             token_palavras_respostas = word_tokenize(palavras_respostas)
#             print('FOR para tokenizar por palavra')
#             print(token_palavras_respostas)
#             print(len(token_palavras_respostas))

def escolher_resposta(perguntas, respostas):
    for setencas in perguntas:
        token = sent_tokenize(setencas)
        # print('FOR para tokenizar por sentença')
        # print(token)
        # print(len(token))

        for palavras in token:
            token_palavras = word_tokenize(palavras)

            # print('FOR para tokenizar por palavra')
            # print(token_palavras)
            # print(len(token_palavras))

    for sentencas_respostas in respostas:
        token_respostas = sent_tokenize(sentencas_respostas)
        # print('FOR para tokenizar por sentença')
        # print(token_respostas)
        # print(len(token_respostas))

        for palavras_respostas in token_respostas:
            token_palavras_respostas = word_tokenize(palavras_respostas)
            # print('FOR para tokenizar por palavra')
            # print(token_palavras_respostas)
            # print(len(token_palavras_respostas))
    
    # has_any_match = any(palavra in token_palavras_respostas for palavra in token_palavras)
    # print(has_any_match)

    # if has_any_match:
    for palavra in token_palavras_respostas:
        if palavra in token_palavras:
            print(palavra)


escolher_resposta(perguntas, respostas)
# print(type(perguntas))
# print(len(perguntas))