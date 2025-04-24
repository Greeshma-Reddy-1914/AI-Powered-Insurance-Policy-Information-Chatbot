import streamlit as st
from datetime import datetime
import pandas as pd
import base64
from backend import process_query, CATEGORY_FOLDERS  # This imports the backend logic

# Page config
st.set_page_config(page_title="Insurance ChatBot", layout="wide")

# Sidebar - API key and category selection
st.sidebar.header("Insurance ChatBot Setup")

# Always visible contact links at the bottom of the sidebar (before API key check)
st.sidebar.markdown("""
    <div style='position: fixed; bottom: 20px; left: 20px; display: flex; gap: 10px;'>
        <a href='https://www.linkedin.com/in/greeshmareddy07/' target='_blank'>
            <img src='https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white'>
        </a>
        <a href='https://github.com/Greeshma-Reddy-1914' target='_blank'>
            <img src='https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white'>
        </a>
    </div>
""", unsafe_allow_html=True)

# API key input
api_key = st.sidebar.text_input("🔐 Enter your Google API Key:", type="password")
if not api_key:
    st.sidebar.warning("Please enter your Google API key to continue.")
    st.stop()

# Insurance category selection
selected_category = st.sidebar.selectbox(
    "📂 Choose an Insurance Category:",
    list(CATEGORY_FOLDERS.keys())
)

# Main UI
st.title("💬 AI-Powered Insurance Policy Assistant")
st.write("Ask any question related to your selected insurance category.")

# Session state initialization
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

user_question = st.text_input("💬 Your Question:")

if user_question:
    with st.spinner("Generating response..."):
        result = process_query(api_key, CATEGORY_FOLDERS[selected_category], user_question)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.conversation_history.append(
        (user_question, result, selected_category, timestamp)
    )

    st.markdown(f"**You:** {user_question}")
    st.markdown(f"**Bot:** {result}")

# Show previous chat history, excluding the most recent question
if st.session_state.conversation_history:
    st.subheader("📜 Chat History")
    for question, answer, category, timestamp in reversed(st.session_state.conversation_history[:-1]):
        st.markdown(f"""
            **You ({timestamp} - {category}):** {question}  
            **Bot:** {answer}
        """)

    # Download history (includes all questions up to the most recent one)
    df = pd.DataFrame(st.session_state.conversation_history, columns=["Question", "Answer", "Category", "Timestamp"])
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    download_link = f'<a href="data:file/csv;base64,{b64}" download="chat_history.csv"><button>Download Chat History</button></a>'
    st.markdown(download_link, unsafe_allow_html=True)
