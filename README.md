# 📄 AI-Enabled Document Question Answering System

<p align="center"> 
  <img src="https://img.shields.io/badge/Version-1.0-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit" />
  <img src="https://img.shields.io/badge/Ollama-Local LLMs-000000?style=for-the-badge&logo=ollama" />
  <img src="https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Production_Ready-brightgreen?style=for-the-badge" /> 
</p>

---

##  Overview

The **AI-Enabled Document Question Answering System** is a production-ready intelligent assistant designed to read documents, extract knowledge, and answer queries using **Local LLMs via Ollama**.

This system performs:

-  PDF/TXT document ingestion  
- Semantic chunking  
-  Embedding generation (via Ollama)  
-  Semantic retrieval using cosine similarity  
-  LLM-powered reasoning with citations  
-  Voice input  
-  Voice output  
-  Query logging + traceability  

It's perfect for **legal analysis, research, compliance, academic work, enterprise documentation, and knowledge extraction**.

---

## Features

###  Local LLM-Powered Q&A  
Runs offline using Ollama models: Llama-3, Mistral, Phi-3, etc.

### Multi-Document Upload  
Handles multiple PDFs / text files.

###  RAG-Based Answering  
Retrieval-Augmented Generation ensures accurate, citation-based answers.

### Voice Input  
Hands-free conversational usage.

### Voice Output  
Reads responses aloud.

### Modern Streamlit UI  
Beautiful, responsive interface.

### SQLite Database  
Stores documents, embeddings, chunks & logs.

---





## System Architecture

```mermaid
flowchart TB

A([Upload PDF or TXT]) --- B([Voice Input - Speech to Text])

A --> C[Document Loader]
C --> D[Text Cleaning and Normalization]

D --> E[Chunking into Semantic Units]
E --> F[Generate Vector Embeddings - Ollama]
F --> G[Save Embeddings and Metadata to SQLite]

G --> H[Semantic Retriever - Cosine Similarity]
H --> I[LLM Query Engine - RAG Pipeline]
I --> J[Generate Answer with Citations]
J --> K[Voice Output - Text to Speech]

classDef blue fill:#61A5FF,stroke:#1A4C8F,stroke-width:2px,color:white;
classDef orange fill:#FFB347,stroke:#A65B00,stroke-width:2px,color:white;
classDef green fill:#7ED957,stroke:#2E8B2D,stroke-width:2px,color:black;

class A,B orange;
class C,D blue;
class E,F,G,H,I green;
class J,K orange;






