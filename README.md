# ***🛡️ AI-Powered Insurance Policy ChatBot***

## Introduction
Understanding insurance policies can often be overwhelming due to the complex language and lengthy documentation. This project introduces an AI-powered Insurance Policy ChatBot that simplifies policy exploration by allowing users to ask questions in natural language and receive precise, context-aware responses drawn directly from real insurance documents. Whether it’s a query about coverage, claims, exclusions, or eligibility, the chatbot intelligently navigates through multiple documents using state-of-the-art ***Large Language Models (LLMs)*** and vector-based search to deliver the most relevant answers. Designed with a user-friendly ***Streamlit*** interface, the system supports various insurance categories such as Health, Motor, Travel, and Cyber, making policy information accessible and understandable for all users.

## Features
- Chat interface to ask policy-related questions.
- It supports multiple insurance types (health, motor, travel, etc.).
- Uses Google Gemini 1.5 Flash for fast and detailed responses.
- Document-based Q&A powered by FAISS vector search.
- Automatic PDF text extraction and chunking.
- Custom prompt engineering for relevant contextual answers.
- Chat history display (excludes the most recent message).
- Full conversation download option.
- LinkedIn and GitHub profile links in the sidebar.

## Folder Structure
```
.
├── app.py                 # Streamlit UI file
├── backend.py             # Backend logic for query processing
├── pdfs/                  # Contains subfolders with PDFs for each insurance type
│   ├── Health_Insurance/
│   ├── Motor_Insurance/
│   └── ...
```

## How It Works
- User Input: A question is typed into the chat box.
- PDF Processing: PDFs under the selected category are loaded, and text is extracted.
- Chunking & Embedding: The extracted text is split and embedded using Google Generative AI embeddings.
- Similarity Search: FAISS retrieves relevant chunks based on semantic similarity.
- Response Generation: Gemini generates a contextual answer using a custom prompt.
- Chat History: Previous chats are shown (excluding the latest), and the full history is downloadable.

## Requirements
- Python 3.8+
- Streamlit
- PyPDF2
- LangChain
- FAISS
- Google Generative AI SDK

## Setup
- Clone the repository.
- Install dependencies using pip install -r requirements.txt.
- Set up your Google Generative AI API key in the sidebar.
- Add relevant PDF documents into the corresponding folders inside /pdfs or use the ones given.

### Run the app with:
> 
> ```streamlit run app.py```
