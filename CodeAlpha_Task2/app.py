import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

faqs = pd.read_excel('faqs.xlsx')
questions_list = faqs['Question'].tolist()

def clean_text(text):
    return text.lower()

cleaned_questions = [clean_text(q) for q in questions_list]

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(cleaned_questions)

st.set_page_config(page_title="CodeAlpha FAQ Chatbot", page_icon="🤖")

with st.sidebar:
    st.header("About")
    st.write("AI-powered FAQ chatbot built for the CodeAlpha AI Internship — Task 2.")
    st.write("Made by Muhammad Jan")
    st.write("Uses TF-IDF and Cosine Similarity to match your question with the most relevant FAQ.")

st.title("🤖 CodeAlpha Internship FAQ Chatbot")
st.write("Apna sawal poochain CodeAlpha AI Internship ke bare mein.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

col1, col2, col3 = st.columns([3, 1, 1])

with col1:
    user_question = st.text_input("Apna sawal yahan likhein:", key="user_input")

with col2:
    ask_clicked = st.button("Ask")

with col3:
    clear_clicked = st.button("Clear Chat")

if ask_clicked and user_question:
    cleaned_input = clean_text(user_question)
    user_vector = vectorizer.transform([cleaned_input])
    similarities = cosine_similarity(user_vector, question_vectors)
    best_match_index = similarities.argmax()
    best_score = similarities[0][best_match_index]

    if best_score < 0.2:
        answer = "Sorry, mujhe samajh nahi aaya. Dobara poochain."
    else:
        answer = faqs['Answer'][best_match_index]

    st.session_state.chat_history.append((user_question, answer))

if clear_clicked:
    st.session_state.chat_history = []

st.write("---")
for question, answer in reversed(st.session_state.chat_history):
    st.markdown(f"**You:** {question}")
    st.success(answer)