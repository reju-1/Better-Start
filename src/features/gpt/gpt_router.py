from fastapi import APIRouter
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFaceHub
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from .gpt_service import create_vector_store

router = APIRouter(prefix="/gpt")
create_vector_store()

# Load vectorstore with HuggingFaceEmbeddings
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vectorstore = FAISS.load_local("legal_vectorstore", embedding_model)
retriever = vectorstore.as_retriever()

# Use a Hugging Face hosted LLM (optional; needs HuggingFace token) OR local setup
# Replace `repo_id` with a model that supports text generation (e.g. "tiiuae/falcon-7b-instruct")
llm = HuggingFaceHub(repo_id="google/flan-t5-base", model_kwargs={"temperature": 0.5})

# Setup QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True,
)


@router.get("/legal-gpt")
def chat_legal_gpt(query: str):
    result = qa_chain.run(query)
    return {"response": result}
