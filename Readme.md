# 🤖 RAG Chatbot with Streamlit

A Retrieval-Augmented Generation (RAG) chatbot that allows users to upload a **PDF**, provide a **Website URL**, or enter **plain text**, then ask questions based on the uploaded content. The application uses **LangChain**, **ChromaDB**, **Hugging Face Embeddings**, and **Mistral AI** to retrieve relevant information and generate accurate answers.

---

## 🚀 Features

* 📄 Upload PDF documents
* 🌐 Load content from website URLs
* 📝 Ask questions about custom text
* 🔍 Semantic search using vector embeddings
* 🤖 AI-powered responses with Mistral AI
* 💻 Interactive Streamlit web interface

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* ChromaDB
* Hugging Face Embeddings
* Sentence Transformers
* Mistral AI
* PyPDF
* BeautifulSoup4

---

## 📂 Project Structure

```text
Rag_project/
│
├── app.py                 # Streamlit UI
├── vector_db.py           # Vector database creation
├── rag.py                 # Retrieval and LLM pipeline
├── requirements.txt
├── .env
├── .gitignore
└── chroma_db/
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/RAG-Project.git

cd RAG-Project
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv .venv

.venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
MISTRAL_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 📸 Supported Input Types

* PDF Documents
* Website URLs
* Plain Text

---

## 📋 Workflow

1. Select an input type.
2. Upload a PDF, enter a URL, or paste text.
3. Create the vector database.
4. Ask questions about the uploaded content.
5. Receive AI-generated answers based on the retrieved context.

---

## 📦 Requirements

Install all required packages using:

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Improvements

* Chat history
* Multiple document upload
* Source citations
* Conversation memory
* Support for DOCX and TXT files
* Deploy on Streamlit Community Cloud
* Cloud-based vector databases (Pinecone, Qdrant, Weaviate)

---

## 👨‍💻 Author

**Barakat Ahmad**

AI / ML Engineer | Machine Learning | Deep Learning | Generative AI

---

## ⭐ If you found this project useful, consider giving it a star!
