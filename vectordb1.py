from dotenv import load_dotenv
import os
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings
)

load_dotenv(override=True)
print("API KEY FROM ENV:", os.getenv("GOOGLE_API_KEY"))

# Load PDF
pdf_path = Path(__file__).parent / "Introduction to Algorithms, Third Edition.pdf"
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

# Split
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=200
)
split_docs = text_splitter.split_documents(docs)

# Embeddings ✅ updated model
embedder = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

# Qdrant
vector_store = QdrantVectorStore.from_documents(
    documents=split_docs,
    url="http://localhost:6333",
    collection_name="Introduction to Algorithms, Third Edition.pdf",
    embedding=embedder
)

# Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7
)

query = "Explain NodeJS event loop"

retrieved_docs = vector_store.similarity_search(query, k=3)

context = "\n\n".join([doc.page_content for doc in retrieved_docs])

response = llm.invoke(
    f"Answer using the provided context.\n\nContext:\n{context}\n\nQuestion: {query}"
)

print(response.content)