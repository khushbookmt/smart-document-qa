# 📚 Smart Document Q&A — RAG-Based PDF Question Answering System

Smart Document Q&A is an AI-powered document question-answering application built using **Retrieval-Augmented Generation (RAG)**. It allows users to upload PDF documents and ask questions in natural language.

The application extracts text from uploaded PDFs, divides it into smaller chunks, generates semantic embeddings, and retrieves relevant information using FAISS. Google's Gemini API then generates answers based on the retrieved document context.

This project demonstrates the complete RAG pipeline, from PDF processing and vector embeddings to semantic retrieval and LLM-powered answer generation.

## 🎥 Demo

<!-- Add your updated project screenshot or deployed application link here -->

## ✨ Features

- 📄 **Multi-PDF Upload:** Upload and process multiple PDF documents.
- ✂️ **Text Chunking:** Splits documents into overlapping chunks to preserve context.
- 🧠 **Semantic Embeddings:** Generates embeddings using Google's Gemini embedding model.
- ⚡ **Vector Search:** Uses FAISS (`IndexFlatL2`) to retrieve relevant document chunks.
- 💬 **Context-Grounded Answers:** Uses Gemini to generate answers based on retrieved document content.
- 🖥️ **Interactive Interface:** Simple and user-friendly Streamlit interface.
- 💾 **Vector Store Persistence:** Supports saving and reloading FAISS indexes and document chunks.

## 🏗️ How It Works

```text
             PDF Documents
                   |
                   v
          Extract Text (PyMuPDF)
                   |
                   v
        Split Text into Chunks
             (LangChain)
                   |
                   v
       Generate Embeddings
             (Gemini API)
                   |
                   v
          Build FAISS Index
                   |
                   v
           User Question
                   |
                   v
        Embed the Question
                   |
                   v
       Retrieve Relevant Chunks
               (FAISS)
                   |
                   v
       Generate Context-Based Answer
               (Gemini)
                   |
                   v
             Final Answer
```

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Frontend / UI | Streamlit |
| Programming Language | Python |
| LLM | Google Gemini API |
| Embeddings | Gemini Embedding Model |
| Vector Database | FAISS |
| Text Chunking | LangChain |
| PDF Processing | PyMuPDF |
| Environment Management | python-dotenv |

## 📁 Project Structure

```text
smart-document-qa/
│
├── app.py
│
├── utils/
│   ├── pdf_reader.py
│   ├── chunking.py
│   ├── embedding.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── storage.py
│   └── llm.py
│
├── step1_pdf_reader.py
├── step2_chunking.py
├── step3_embedding.py
├── step4_vector_store.py
├── step5_retriever.py
├── step6_rag.py
├── step7_build_index.py
├── step8_chat.py
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/khushbookmt/smart-document-qa.git
cd smart-document-qa
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows:**
```bash
.venv\Scripts\activate
```

**macOS / Linux:**
```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API Key

Create a `.env` file in the project's root directory and add:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

Get your API key from [Google AI Studio](https://aistudio.google.com/).

**Important:** Never upload your `.env` file or expose your API key publicly.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🧩 Understanding the RAG Pipeline Step by Step

The project also contains individual Python scripts demonstrating the different stages of the RAG workflow.

| Step | File | Concept |
|---|---|---|
| 1 | `step1_pdf_reader.py` | Extracting text from PDF files |
| 2 | `step2_chunking.py` | Splitting text into overlapping chunks |
| 3 | `step3_embedding.py` | Generating vector embeddings |
| 4 | `step4_vector_store.py` | Creating a FAISS vector index |
| 5 | `step5_retriever.py` | Retrieving relevant document chunks |
| 6 | `step6_rag.py` | Combining retrieval and generation |
| 7 | `step7_build_index.py` | Building and saving the vector index |
| 8 | `step8_chat.py` | Querying documents through a terminal interface |

Run an individual script using:

```bash
python step1_pdf_reader.py
```

## 🔮 Future Improvements

- [ ] Deploy the application using Streamlit Community Cloud.
- [ ] Support additional document formats such as DOCX and TXT.
- [ ] Display source citations and PDF page references.
- [ ] Improve conversation memory for follow-up questions.
- [ ] Enhance retrieval quality and error handling.

## 👤 Project Credits

**Maintained and adapted by Khushboo**

- GitHub: [@khushbookmt](https://github.com/khushbookmt)
- Project Repository: [Smart Document Q&A](https://github.com/khushbookmt/smart-document-qa)


This project is open source and available for learning purposes.
