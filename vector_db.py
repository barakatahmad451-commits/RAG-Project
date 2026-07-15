from dotenv import load_dotenv

from langchain_community.document_loaders import (
    PyPDFLoader,
    WebBaseLoader,
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

# Load environment variables
load_dotenv()


def create_vector_database(input_type, data):
    """
    Creates a Chroma vector database from PDF, URL, or Text.

    Parameters:
        input_type (str): 'pdf', 'url', or 'text'
        data (str): Path to PDF, URL, or plain text

    Returns:
        Chroma vector store
    """

    # -------------------------
    # Load Documents
    # -------------------------
    if input_type == "pdf":
        loader = PyPDFLoader(data)
        docs = loader.load()

    elif input_type == "url":
        loader = WebBaseLoader(data)
        docs = loader.load()

    elif input_type == "text":
        docs = [Document(page_content=data)]

    else:
        raise ValueError("Unsupported input type")

    # -------------------------
    # Split Documents
    # -------------------------
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    # -------------------------
    # Embedding Model
    # -------------------------
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # -------------------------
    # Create Chroma DB
    # -------------------------
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="chroma_db"
    )

    return vectorstore