# **AI-Powered Insurance Policy ChatBot**

## Introduction
<p align = "justify">Understanding insurance policies can often be overwhelming due to the complex language and lengthy documentation. This project introduces an <i><b>AI-powered Insurance Policy ChatBot</b></i> that simplifies policy exploration by allowing users to ask questions in natural language and receive precise, context-aware responses drawn directly from real insurance documents. Whether it’s a query about coverage, claims, exclusions, or eligibility, the chatbot intelligently navigates through multiple documents using state-of-the-art <i><b>Large Language Models (LLMs)</b></i> and <i><b>Vector-based Search</b></i> to deliver the most relevant answers. Designed with a user-friendly <i><b>Streamlit</b></i> interface, the system supports various insurance categories such as Health, Motor, Travel, and Cyber, making policy information accessible and understandable for all users. </p>

## Knowledge Base
<p align = "justify"> This chatbot was specifically developed for understanding and querying the insurance policies offered by <i><b>State Bank of India (SBI) General Insurance</b></i>. The knowledge base was built using official policy documents downloaded from the <a href="https://www.sbigeneral.in/downloads">SBI General Insurance Downloads Portal</a>. These documents include detailed wordings for various insurance types such as Motor, Health, Personal Accident, Travel, Home, Cyber, and more.

Each document was processed and embedded into a vector database, enabling the chatbot to deliver precise, context-aware responses directly derived from the original policy content. This ensures that users receive trustworthy and up-to-date information aligned with the policies issued by SBI. </p>

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
