import streamlit as st
import tempfile
from vector_db import create_vector_database
from rag import ask_question

st.set_page_config(
    page_title="RAG Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 RAG Chatbot")
st.write("Upload a PDF, Website URL or Text and ask questions.")

# Sidebar
st.sidebar.title("Knowledge Source")

option = st.sidebar.radio(
    "Choose Input Type",
    ["PDF", "Website", "Text"]
)

vectorstore = None

# ---------------- PDF ----------------

if option == "PDF":

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file:

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:

            tmp.write(uploaded_file.read())
            pdf_path = tmp.name

        if st.button("Create Vector Database"):

            with st.spinner("Processing PDF..."):

                vectorstore = create_vector_database(
                    "pdf",
                    pdf_path
                )

            st.success("Vector Database Created!")

# ---------------- URL ----------------

elif option == "Website":

    url = st.text_input("Enter Website URL")

    if st.button("Create Vector Database"):

        with st.spinner("Loading Website..."):

            vectorstore = create_vector_database(
                "url",
                url
            )

        st.success("Vector Database Created!")

# ---------------- TEXT ----------------

else:

    text = st.text_area(
        "Paste your text",
        height=300
    )

    if st.button("Create Vector Database"):

        with st.spinner("Creating Database..."):

            vectorstore = create_vector_database(
                "text",
                text
            )

        st.success("Vector Database Created!")

st.divider()

question = st.text_input("Ask a Question")

if st.button("Ask"):

    if question == "":
        st.warning("Please enter a question.")

    else:

        answer = ask_question(question)

        st.markdown("### Answer")

        st.write(answer)