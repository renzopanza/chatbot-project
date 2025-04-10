import random
import nltk
from nltk.tokenize import word_tokenize

respostas_chatBot = {
    "ação": "Sim! Temos ótimos livros de ação. Você prefere algo mais moderno ou clássico?",
    "terror": "Temos muitos livros de terror. Gosta mais de terror psicológico ou sobrenatural?",
    "romance": "Claro! Nossos romances são bem variados. Você gosta de histórias contemporâneas ou de época?",
    "livro": "Temos vários gêneros. Está procurando algo leve ou mais intenso?",
}

# perguntas_chatBot = [
#     "Qual gênero você mais gosta?",
#     "Você prefere livros longos ou curtos?",
#     "Está procurando por um autor específico?",
#     "Quer recomendações com base em best-sellers?",
# ]

# perguntas_user = input()

def responder(usuario_input):
    tokens_usuario = word_tokenize(usuario_input.lower())
    
    for palavras_chaves in respostas_chatBot:
        if palavras_chaves in tokens_usuario:
            resposta_chat = respostas_chatBot[palavras_chaves]
            # nova_pergunta = random.choice(perguntas_chatBot)
            # return f"{resposta} {nova_pergunta}"
            return f"{resposta_chat}"
    
    return "Não entendi muito bem. Poderia repetir de outra maneira?"

# Loop do chatbot
print("ChatBot: Olá! Eu posso te ajudar a encontrar diversos livro.Qual tipo de livro você procura?")

while True:
    entrada_usuario = input("Você: ")
    resposta_chat = responder(entrada_usuario)
    print("ChatBot:", resposta_chat)

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