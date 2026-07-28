# 📚 Ask to Zuzu — PDF Q&A Chatbot using RAG (Gemini + FAISS)

Ask to Zuzu is a Retrieval-Augmented Generation (RAG) chatbot that lets you upload any PDF and ask natural language questions about it. The app retrieves the most relevant sections of the document and uses Google's Gemini model to generate accurate, context-grounded answers — reducing hallucination and keeping responses grounded in your actual data.

Built as a hands-on project to understand the complete RAG pipeline: from raw PDF text to vector search to LLM-generated answers.

> 🧩 **Built step by step, from scratch.** This project wasn't written in one go — it was built incrementally, one concept at a time (PDF reading → chunking → embeddings → vector search → LLM answer generation), with each step tested independently before moving to the next. The `step1_*.py` to `step8_*.py` files in this repo are that exact journey, kept intentionally so anyone can follow the same path.
>
> 👶 **Beginner-friendly by design.** If you're new to RAG or LLM applications, you don't need to jump straight into `app.py`. Start from `step1_pdf_reader.py` and move forward one file at a time — each script builds on the last and shows exactly one new concept, making this a good reference for anyone learning RAG for the first time.

---

## 🎥 Demo
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4e176ebd-270a-4859-9056-45b9daa7ccd4" />



---

## ✨ Features

- 📄 **Multi-PDF upload** — process one or several PDFs at once
- ✂️ **Smart chunking** — splits documents into overlapping chunks for better context retention
- 🧠 **Semantic embeddings** — powered by Google's `gemini-embedding-001` model
- ⚡ **Fast vector search** — FAISS (`IndexFlatL2`) for similarity-based retrieval
- 💬 **Context-grounded answers** — powered by `gemini-flash-latest`, with a strict "answer only from context" instruction to reduce hallucination
- 🖥️ **Simple Streamlit UI** — upload PDFs on one side, chat on the other
- 💾 **Persistent vector store** — save and reload FAISS index + chunks without re-processing PDFs every time

---

## 🏗️ How It Works

```
                 ┌─────────────┐
                 │   PDF(s)    │
                 └──────┬──────┘
                        ▼
              Extract text (PyMuPDF)
                        ▼
           Split into chunks (LangChain)
                        ▼
        Generate embeddings (Gemini API)
                        ▼
          Build FAISS vector index
                        ▼
     ┌──────────────────────────────────┐
     │   User asks a question           │
     └──────────────────┬───────────────┘
                        ▼
           Embed the question (Gemini)
                        ▼
        Retrieve top-k similar chunks (FAISS)
                        ▼
      Generate answer from context (Gemini)
                        ▼
                  💬 Final Answer
```

---

## 🛠️ Tech Stack

| Component        | Technology                          |
|-------------------|--------------------------------------|
| UI                | Streamlit                            |
| LLM & Embeddings  | Google Gemini API (`gemini-embedding-001`, `gemini-flash-latest`) |
| Vector Search     | FAISS                                |
| Text Chunking     | LangChain (`RecursiveCharacterTextSplitter`) |
| PDF Parsing       | PyMuPDF (`fitz`)                     |
| Config Management | python-dotenv                        |

---

## 📁 Project Structure

```
Multimodel_Rag/
├── app.py                     # Streamlit app (main entry point)
├── utils/
│   ├── pdf_reader.py          # Extract text from PDFs
│   ├── chunking.py            # Split text into chunks
│   ├── embedding.py           # Generate embeddings via Gemini
│   ├── vector_store.py        # Build FAISS index
│   ├── retriever.py           # Retrieve top-k relevant chunks
│   ├── storage.py             # Save/load FAISS index + chunks
│   └── llm.py                 # Generate final answer via Gemini
├── step1_pdf_reader.py         │
├── step2_chunking.py           │
├── step3_embedding.py          │  Development journey —
├── step4_vector_store.py       │  incremental scripts used
├── step5_retriever.py          │  while building the pipeline
├── step6_rag.py                │  step by step
├── step7_build_index.py        │
├── step8_chat.py               │
├── requirements.txt
├── .env.example                # Sample env file (no real key)
└── sample.pdf                  # Example PDF for testing
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/aankitsharma/ask-to-zuzu-rag-chatbot.git
cd ask-to-zuzu-rag-chatbot
```

### 2. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API key
Copy `.env.example` to `.env` and add your Gemini API key:
```
GOOGLE_API_KEY=your_google_gemini_api_key_here
```
> Get a free API key from [Google AI Studio](https://aistudio.google.com/).

### 5. Run the app
```bash
streamlit run app.py
```

---

## 👶 New to RAG? Learn It Step by Step

This repo doubles as a learning path. Instead of jumping into the full app, walk through these files in order — each one adds exactly one new concept on top of the last:

| Step | File | What you'll learn |
|------|------|--------------------|
| 1 | `step1_pdf_reader.py` | Extracting raw text from a PDF |
| 2 | `step2_chunking.py` | Splitting long text into overlapping chunks |
| 3 | `step3_embedding.py` | Turning text chunks into vector embeddings |
| 4 | `step4_vector_store.py` | Storing embeddings in a FAISS index |
| 5 | `step5_retriever.py` | Retrieving the most relevant chunks for a query |
| 6 | `step6_rag.py` | Combining retrieval with LLM answer generation |
| 7 | `step7_build_index.py` | Saving the vector store to disk (so you don't rebuild it every time) |
| 8 | `step8_chat.py` | Loading the saved index and chatting in a terminal loop |

Run any step directly:
```bash
python step1_pdf_reader.py
```
Read the code, run it, see the output — then move to the next step. By step 8, you'll understand every moving part behind `app.py`.

---

## 🧪 Command-Line Alternative

Prefer working from the terminal? You can also build and query the index without the UI:

```bash
python step7_build_index.py   # builds and saves the FAISS index
python step8_chat.py          # chat with your document in the terminal
```

---

## 🔮 Future Improvements

- [ ] Support for multiple file types (DOCX, TXT)
- [ ] Source citation (show which chunk/page an answer came from)
- [ ] Conversation memory for follow-up questions
- [ ] Deploy on Streamlit Community Cloud

---

## 👤 Author

**Aankit Sharma**
Transitioning from a 12+ year career in BFSI/Relationship Management into Data Analytics & Data Science.

- GitHub: [@aankitsharma](https://github.com/aankitsharma)
- LinkedIn: [Aankit Sharma](https://linkedin.com/in/aankit-sharma-373784409)

---

## 📄 License

This project is open source and available for learning purposes.
