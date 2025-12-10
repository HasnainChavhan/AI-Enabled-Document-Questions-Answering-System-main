**📄 AI-Enabled Document Question Answering System**

A Fast, Accurate & Voice-Enabled Document Intelligence Platform powered by LLMs

**🚀 Overview**

The AI-Enabled Document Question Answering System is a production-ready intelligent document assistant capable of:

Reading large PDF/TXT documents

Breaking them into meaningful semantic chunks

Generating vector embeddings (Ollama / Local LLMs)

Answering user queries with citations

Providing a Streamlit-based web interface

Supporting voice input & text-to-speech output

Maintaining query logs for audit and reviews

This project is optimized for real-world enterprise workflows, such as legal document analysis, knowledge extraction, compliance, research summarization, and automated document intelligence.

**✨ Key Features**
🧠 1. Local LLM-Powered Question Answering

Uses Ollama models (e.g., llama3, mistral, phi3)

Ensures privacy — all processing remains on your machine

Produces high-accuracy, citation-backed answers

📂 2. Multi-Document Support

Upload one or multiple:

PDF files

Plain text files

Each document is processed, chunked, stored, and indexed automatically.

🔍 3. Semantic Search + Context Retrieval

Built using:

Vector embeddings

Cosine similarity

Retrieval-Augmented Generation (RAG) pipeline

Allows precise, context-aware query responses.

🎤 4. Voice Input + AI Voice Output

Ask questions using your microphone.
Get responses via text-to-speech.

Useful for:

Hands-free operation

Visually impaired users

Fast research workflows

🖥️ 5. Modern Streamlit Web UI

A clean, responsive dashboard featuring:

Document upload page

Chat interface

File manager




Query logs

Config settings

🛡️ 6. Lightweight SQLite Database

Stores:

Document metadata

Chunk embeddings

User interactions

**🏗️ Project Structure**

AI-Enabled-Document-QA/
│── app.py                   # Main Streamlit application
│── voice_functions.py       # Speech-to-text and TTS utilities
│── app.db                   # SQLite database for document + logs
│── requirements.txt         # Python dependencies
│── .env                     # Environment variables
│── OLLAMA_SETUP.md          # Local LLM installation guide
│
├── pages/                   # Streamlit multipage interface
├── uploaded_docs/           # Stored user documents
├── venv/ (excluded)         # Local virtual environment
└── __pycache__/ (excluded)

**Installation & Setup**
1. Clone the Repository
git clone https://github.com/your-username/AI-Document-QA.git
cd AI-Document-QA

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Install & Run Ollama

➡️ Full setup guide is available in OLLAMA_SETUP.md

Run:

ollama pull llama3
ollama run llama3


You may replace llama3 with any preferred model.

5. Start the Application
streamlit run app.py


Open the UI in your browser at:
👉 http://localhost:8501

🧩 How It Works (Technical Architecture)
1. Document Loader

Extracts raw text from PDF/TXT files

Cleans and normalizes content

2. Chunker

Splits documents into overlapping text chunks

Prevents context loss

Optimized for LLM reasoning

3. Embedding Generator

Uses Ollama embedding models

Produces vector representations

Saves them in SQLite

4. Semantic Retriever

Finds top-k relevant chunks using cosine similarity

5. LLM Query Engine

Sends context + query to the model

Generates answer with quotations & citations

6. Voice Interface

Converts speech → text (STT)

Converts generated answer → speech (TTS)

**🧪 Example Usage**
Upload a Document

Upload a PDF (e.g., "Contract.pdf").

Ask a Question

"What are the termination clauses in this document?"

Get Answer

The system retrieves relevant context and responds with citations.

📦 Deployment Options
⭐ Local Development (default)

Uses Streamlit + Ollama locally.

☁️ Cloud Deployment (Advanced)

Docker containerization

FastAPI backend + Streamlit frontend

GPU inference using vLLM or llama.cpp

(Ask if you want deployment files generated for you.)

**🛠️ Tech Stack**
Layer	Technology
UI	Streamlit
Backend	Python
Embeddings	Ollama
LLM	Local models (Llama, Mistral, Phi, etc.)
Database	SQLite
Voice	SpeechRecognition, gTTS / pyttsx3
Document Parsing	PyPDF2, LangChain loaders

**📘 Roadmap (Upcoming Features)**

 Multi-user authentication

 Admin dashboard & analytics

 File versioning

 Document summarization mode

 PDF highlighting of referenced sections

 Chat history with export

 Cloud-ready architecture guide

**🤝 Contributing**

Contributions are welcome!
You can improve documentation, UI, or back-end logic.

**🛡️ License**

This project is released under the MIT License.
You are free to use, modify, and distribute it.

**👤 Author**

Hasnain Chavhan
AI & DS Engineer • Machine Learning • GenAI • MLOps
Feel free to reach out for collaboration or suggestions.

**⭐ Support the Project**

If this project helps you, consider starring the repo 🌟
