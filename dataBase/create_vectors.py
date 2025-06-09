from PyPDF2 import PdfReader
from transformers import LlamaTokenizerFast
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

def from_pdf_extract_text(pdf_path: str) -> str:
    try:
        pdf = PdfReader(pdf_path)
        return "".join(p.extract_text() or "" for p in pdf.pages)
    except Exception as e:
        print(f"Erro ao ler o PDF: {e}")
        return ""

pdf_path = './dataBase/pdf_datasets/GenerosLiterariosVisaoGeral.pdf'
if not os.path.exists(pdf_path):
    print("O arquivo PDF não foi encontrado")
    exit(1)

db = from_pdf_extract_text(pdf_path)
if not db:
    print("Nenhum texto foi extraído do PDF")
    exit(1)

try:
    llama_tokenizer_fast = LlamaTokenizerFast.from_pretrained("hf-internal-testing/llama-tokenizer", clean_up_tokenization_spaces=True)
except Exception as e:
    print(f"Erro ao carregar o tokenizer: {e}")
    exit(1)

def llama_tokens(text: str) -> int:
    return len(llama_tokenizer_fast.encode(text))

chunk_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=40, length_function=llama_tokens)
chunks = chunk_splitter.create_documents([db])

if len(chunks) == 0:
    print("Nenhum chunk foi criado. Verifique o texto extraído e o tokenizer")
    exit(1)

try:
    vectors_embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
except Exception as e:
    print(f"Erro ao carregar o modelo de embeddings: {e}")
    exit(1)

try:
    vectors = FAISS.from_documents(chunks, vectors_embedding)
    save_dir = "./dataBase/vectors"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    vectors.save_local(save_dir)
    print("Índice FAISS salvo com sucesso")
except Exception as e:
    print(f"Erro ao criar ou salvar o índice FAISS: {e}")