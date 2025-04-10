import random
import nltk
from nltk.tokenize import word_tokenize

respostas_chatBot = {
    # Nível 1: Gêneros iniciais
    "ação": "Adoro ação! Temos ótimos títulos. Você prefere algo mais moderno ou clássico?",
    "terror": "Terror é emocionante! Gosta mais de psicológico ou sobrenatural?",
    "romance": "Romances são incríveis! Prefere contemporâneo ou de época?",
    "fantasia": "Fantasia é um mundo à parte! Gosta de épico ou leve?",
    "ficção": "Ficção científica é fascinante! Prefere futurista ou distópico?",
    "mistério": "Mistério é intrigante! Gosta de detetives ou tramas modernas?",
    "aventura": "Aventura é pura adrenalina! Prefere épicas ou arriscadas?",
    "drama": "Dramas mexem com a gente! Gosta de reais ou fictícios?",
    "biografia": "Biografias inspiram! Prefere artistas ou líderes?",
    "autoajuda": "Autoajuda é transformador! Busca algo para vida pessoal ou carreira?",
    "comédia": "Comédia é diversão garantida! Gosta de leve ou sarcástico?",
    "infantil": "Infantis são encantadores! É para pequena ou crescidinha?",
    "juvenil": "Juvenis são ótimos! Gosta de romance ou aventura?",
    "história": "História é fascinante! Prefere geral ou específico?",
    "suspense": "Suspense prende a atenção! Gosta de psicológico ou reviravoltas?",
    "clássicos": "Clássicos são eternos! Prefere nacionais ou estrangeiros?",
    "poesia": "Poesia é pura emoção! Gosta de moderna ou tradicional?",

    # Nível 2: Respostas com palavras-chave únicas
    "moderno": "Legal, ação moderna tem muita energia! Gosta de tecnologia ou perseguições?",
    "clássico": "Clássicos de ação são atemporais! Prefere duelos ou explorações?",
    "psicológico": "Terror psicológico é intenso! Gosta de tensão ou mistérios?",
    "sobrenatural": "Sobrenatural dá arrepios! Prefere fantasmas ou criaturas?",
    "contemporâneo": "Romances contemporâneos são atuais! Gosta de dramas ou finais felizes?",
    "época": "Romances de época têm charme! Prefere reis ou revoluções?",
    "épico": "Fantasia épica é grandiosa! Gosta de batalhas ou magia?",
    "leve": "Fantasia leve é descontraída! Prefere humor ou encantamento?",
    "futurista": "Ficção futurista é visionária! Gosta de espaço ou robôs?",
    "distópico": "Distopias são impactantes! Prefere rebeliões ou controle?",
    "detetives": "Detetives são clássicos! Gosta de pistas ou enigmas?",
    "tramas": "Tramas modernas surpreendem! Prefere investigação ou segredos?",
    "épicas": "Aventuras épicas são imensas! Gosta de viagens ou desafios?",
    "arriscadas": "Missões arriscadas são emocionantes! Prefere perigos ou tesouros?",
    "reais": "Dramas reais tocam fundo! Gosta de superação ou tragédias?",
    "fictícios": "Dramas fictícios são criativos! Prefere emoções ou reflexões?",
    "artistas": "Biografias de artistas fascinam! Gosta de música ou pintura?",
    "líderes": "Líderes inspiram! Prefere política ou negócios?",
    "pessoal": "Autoajuda pessoal é prático! Gosta de hábitos ou motivação?",
    "carreira": "Autoajuda para carreira é útil! Prefere liderança ou sucesso?",
    "leve": "Comédia leve relaxa! Gosta de cotidiano ou absurdos?",
    "sarcástico": "Sarcasmo é afiado! Prefere crítica ou ironia?",
    "pequena": "Infantis para pequenos são fofos! Gosta de animais ou contos?",
    "crescidinha": "Para crescidinhas, temos aventuras! Prefere escola ou mundos?",
    "romance": "Romances juvenis são fofos! Gosta de paixões ou amizades?",
    "aventura": "Aventura juvenil é empolgante! Gosta de grupos ou heróis?",
    "geral": "História geral é ampla! Gosta de guerras ou culturas?",
    "específico": "História específica é detalhada! Prefere reis ou revoltas?",
    "psicológico": "Suspense psicológico é profundo! Gosta de mentes ou jogos?",
    "reviravoltas": "Reviravoltas surpreendem! Prefere finais ou viradas?",
    "nacionais": "Clássicos nacionais são ricos! Gosta de realismo ou romantismo?",
    "estrangeiros": "Clássicos estrangeiros são universais! Prefere tragédias ou sátiras?",
    "moderna": "Poesia moderna é livre! Gosta de sentimentos ou experimentos?",
    "tradicional": "Poesia tradicional é elegante! Prefere rimas ou narrativas?",

    # Nível 3: Respostas que fecham o loop com pergunta aberta
    "tecnologia": "Ação com tecnologia é eletrizante! E qual outro gênero de livros você gosta?",
    "perseguições": "Perseguições são pura adrenalina! E qual outro gênero de livros você gosta?",
    "duelos": "Duelos clássicos são intensos! E qual outro gênero de livros você gosta?",
    "explorações": "Explorações são empolgantes! E qual outro gênero de livros você gosta?",
    "tensão": "Tensão psicológica é viciante! E qual outro gênero de livros você gosta?",
    "mistérios": "Mistérios psicológicos intrigam! E qual outro gênero de livros você gosta?",
    "fantasmas": "Fantasmas dão medo! E qual outro gênero de livros você gosta?",
    "criaturas": "Criaturas são assustadoras! E qual outro gênero de livros você gosta?",
    "dramas": "Dramas contemporâneos emocionam! E qual outro gênero de livros você gosta?",
    "finais": "Finais felizes são ótimos! E qual outro gênero de livros você gosta?",
    "reis": "Reis dão um toque majestoso! E qual outro gênero de livros você gosta?",
    "revoluções": "Revoluções são intensas! E qual outro gênero de livros você gosta?",
    "batalhas": "Batalhas épicas são incríveis! E qual outro gênero de livros você gosta?",
    "magia": "Magia encanta! E qual outro gênero de livros você gosta?",
    "humor": "Humor leve é divertido! E qual outro gênero de livros você gosta?",
    "encantamento": "Encantamento é mágico! E qual outro gênero de livros você gosta?",
    "espaço": "Viagens espaciais fascinam! E qual outro gênero de livros você gosta?",
    "robôs": "Robôs são o futuro! E qual outro gênero de livros você gosta?",
    "rebeliões": "Rebeliões são emocionantes! E qual outro gênero de livros você gosta?",
    "controle": "Controle é intrigante! E qual outro gênero de livros você gosta?",
    "pistas": "Pistas são instigantes! E qual outro gênero de livros você gosta?",
    "enigmas": "Enigmas desafiam! E qual outro gênero de livros você gosta?",
    "investigação": "Investigações prendem! E qual outro gênero de livros você gosta?",
    "segredos": "Segredos surpreendem! E qual outro gênero de livros você gosta?",
    "viagens": "Viagens épicas inspiram! E qual outro gênero de livros você gosta?",
    "desafios": "Desafios são empolgantes! E qual outro gênero de livros você gosta?",
    "perigos": "Perigos aceleram o coração! E qual outro gênero de livros você gosta?",
    "tesouros": "Tesouros são emocionantes! E qual outro gênero de livros você gosta?",
    "superação": "Superação emociona! E qual outro gênero de livros você gosta?",
    "tragédias": "Tragédias marcam! E qual outro gênero de livros você gosta?",
    "emoções": "Emoções profundas tocam! E qual outro gênero de livros você gosta?",
    "reflexões": "Reflexões fazem pensar! E qual outro gênero de livros você gosta?",
    "música": "Música inspira! E qual outro gênero de livros você gosta?",
    "pintura": "Pintura é arte pura! E qual outro gênero de livros você gosta?",
    "política": "Política é intensa! E qual outro gênero de livros você gosta?",
    "negócios": "Negócios motivam! E qual outro gênero de livros você gosta?",
    "hábitos": "Hábitos transformam! E qual outro gênero de livros você gosta?",
    "motivação": "Motivação eleva! E qual outro gênero de livros você gosta?",
    "liderança": "Liderança é essencial! E qual outro gênero de livros você gosta?",
    "sucesso": "Sucesso inspira! E qual outro gênero de livros você gosta?",
    "cotidiano": "Cotidiano diverte! E qual outro gênero de livros você gosta?",
    "absurdos": "Absurdos são hilários! E qual outro gênero de livros você gosta?",
    "crítica": "Crítica é afiada! E qual outro gênero de livros você gosta?",
    "ironia": "Ironia é genial! E qual outro gênero de livros você gosta?",
    "animais": "Animais encantam! E qual outro gênero de livros você gosta?",
    "contos": "Contos são mágicos! E qual outro gênero de livros você gosta?",
    "escola": "Escola é divertida! E qual outro gênero de livros você gosta?",
    "mundos": "Mundos novos fascinam! E qual outro gênero de livros você gosta?",
    "paixões": "Paixões juvenis são fofas! E qual outro gênero de livros você gosta?",
    "amizades": "Amizades emocionam! E qual outro gênero de livros você gosta?",
    "grupos": "Grupos são empolgantes! E qual outro gênero de livros você gosta?",
    "heróis": "Heróis inspiram! E qual outro gênero de livros você gosta?",
    "guerras": "Guerras marcam a história! E qual outro gênero de livros você gosta?",
    "culturas": "Culturas enriquecem! E qual outro gênero de livros você gosta?",
    "revoltas": "Revoltas são intensas! E qual outro gênero de livros você gosta?",
    "mentes": "Mentes complexas intrigam! E qual outro gênero de livros você gosta?",
    "jogos": "Jogos mentais desafiam! E qual outro gênero de livros você gosta?",
    "finais": "Finais surpreendentes chocam! E qual outro gênero de livros você gosta?",
    "viradas": "Viradas inesperadas prendem! E qual outro gênero de livros você gosta?",
    "realismo": "Realismo é marcante! E qual outro gênero de livros você gosta?",
    "romantismo": "Romantismo é belo! E qual outro gênero de livros você gosta?",
    "tragédias": "Tragédias são intensas! E qual outro gênero de livros você gosta?",
    "sátiras": "Sátiras divertem! E qual outro gênero de livros você gosta?",
    "sentimentos": "Sentimentos tocam! E qual outro gênero de livros você gosta?",
    "experimentos": "Experimentos inovam! E qual outro gênero de livros você gosta?",
    "rimas": "Rimas encantam! E qual outro gênero de livros você gosta?",
    "narrativas": "Narrativas clássicas fluem! E qual outro gênero de livros você gosta?",
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