from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def create_vector_store():
    # Load and split the PDF
    loader = PyPDFLoader("src/features/gpt/info.pdf")
    documents = loader.load()

    # Use a free Hugging Face embedding model (no API key needed)
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create FAISS vectorstore
    vectorstore = FAISS.from_documents(documents, embedding_model)
    vectorstore.save_local("legal_vectorstore")
