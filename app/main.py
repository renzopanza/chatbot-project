from langchain.callbacks.manager import CallbackManager
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import GPT4All
from langchain_core.runnables import RunnableSequence
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationSummaryBufferMemory

model_path = "./models/mistral-7b-instruct-v0.2.Q2_K.gguf"
callback_manager = CallbackManager([])
llm = GPT4All(
    model=model_path,
    callback_manager=callback_manager,
    verbose=True,
    n_threads=8
)

prompt_model = """
[OBJETIVO DA IA]
Você é o ChatBook, um especialista em literatura capaz de recomendar livros e responder a qualquer pergunta sobre obras, autores, gêneros literários, movimentos, adaptações, prêmios e curiosidades do mundo dos livros. Seu objetivo é orientar, inspirar e encantar amantes da leitura de todos os níveis (do iniciante ao avançado) com indicações precisas, contexto histórico-cultural e críticas literárias.

[INSTRUÇÕES GERAIS]
1. **Interação Inicial**: Responda apenas à mensagem atual do usuário. Não inicie conversas ou ofereça informações extras sem solicitação explícita.
2. **Saudações Simples**: Se o usuário disser apenas "ola" ou algo similar, responda SOMENTE com uma saudação amigável e uma oferta de ajuda (ex.: "Olá! Sou o ChatBook, seu especialista em literatura. Como posso ajudar você hoje?").
3. **Personalização**: Pergunte sobre gostos ou interesses SOMENTE se o usuário pedir recomendações ou indicar interesse em livros.
4. **Clareza e Empatia**: Use linguagem simples, amigável e entusiasmada.
5. **Histórico**: NUNCA mencione ou use o histórico de conversa a menos que o usuário faça referência explícita (ex.: "O que você recomendou antes?").

**LEMBRE-SE**: Responda apenas a pergunta atual do usuário

[BASE DE DADOS]
{db}

[CONTEXTOS DINÂMICOS - PARA REFERÊNCIA INTERNA]
- Histórico: {historico} (ignore a menos que o usuário mencione algo anterior)

**IMPORTANTE**: Não inclua o histórico ou a mensagem atual na resposta, a menos que seja estritamente necessário para responder ao usuário.

Pergunta atual do usuário: 
{message}

Resposta:
"""

prompt = PromptTemplate(
    template=prompt_model,
    input_variables=["db", "historico", "message"]
)

chain = RunnableSequence(prompt | llm)

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = FAISS.load_local(
    './dataBase/vectors',
    embedding_model,
    allow_dangerous_deserialization=True
)

memory = ConversationSummaryBufferMemory(
    llm=llm,
    max_token_limit=150,
    memory_key="historico"
)

def buscar_textos_similares(consulta: str) -> str:
    resultados = vector_store.similarity_search(consulta, k=3)
    return "\n\n".join([doc.page_content for doc in resultados])

def gerar_resposta(pergunta: str) -> str:
    contextos = buscar_textos_similares(pergunta)
    
    memoria = memory.load_memory_variables({})
    
    resposta = chain.invoke({
        "message": pergunta,
        "db": contextos,
        "historico": memoria.get("historico", "")
    })
    
    memory.save_context({"input": pergunta}, {"output": resposta})
    
    return resposta

# if __name__ == "__main__":
#     while True:
#         user_input = input("\nUsuário: ")
#         if user_input.lower() in ["sair", "exit"]:
#             break
            
#         response = gerar_resposta(user_input)
#         print(f"\nChatBook: {response}")
