import streamlit as st
import requests

st.set_page_config(page_title="Chatbot Made by Taskeen Merchant", page_icon="🤖")

API_KEY = st.secrets["GOOGLE_GEMINI_API_KEY"]
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

# Custom CSS for background, spacing, and font size
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1e1e2f;
        background-image: url('https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZGFyayUyMGJhY2tncm91bmR8ZW58MHx8MHx8fDA%3D&fm=jpg&q=60&w=3000');
        background-size: cover;
        background-attachment: fixed;
        color: white;
        font-family: Arial, sans-serif;
    }
    /* Header h1 */
    h1 {
        font-size: 3rem !important;
        font-weight: 700 !important;
        margin-bottom: 40px !important;
        text-align: center;
        color: #34B3F1;
    }
    /* Text input label */
    label[data-baseweb="label"] {
        font-size: 1.5rem !important;
        margin-bottom: 10px !important;
    }
    /* Text input itself */
    input[data-baseweb="input"] {
        font-size: 1.25rem !important;
        padding: 10px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1>Simple Chatbot with Google Gemini</h1>", unsafe_allow_html=True)

user_input = st.text_input("Ask me anything:", placeholder="Type your message...", key="input")

if user_input:
    payload = {
        "contents": [{
            "parts": [{"text": user_input}]
        }]
    }
    with st.spinner("Thinking..."):
        response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        data = response.json()
        answer = data['candidates'][0]['content']['parts'][0]['text']
        st.success(answer)
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
