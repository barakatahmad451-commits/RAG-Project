from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k":3}
)

llm = ChatMistralAI(
    model="mistral-small-latest"
)

prompt = ChatPromptTemplate.from_template("""
Answer the question only from the given context.

Context:
{context}

Question:
{question}
""")


def ask_question(question):

    docs = retriever.invoke(question)

    context = "\n\n".join(doc.page_content for doc in docs)

    chain = prompt | llm

    response = chain.invoke({
        "context": context,
        "question": question
    })

    return response.content