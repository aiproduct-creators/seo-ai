from os import getenv
from dotenv import load_dotenv

load_dotenv()
import cohere
from cohere.responses.chat import StreamEvent
import streamlit as st
import uuid
from datetime import date

co = cohere.Client(getenv("CO_API"))
# Use CSS to add custom styles to your UI
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Side bar
if st.sidebar.button("New Chat", key="clear_chat"):
    st.session_state.messages = []
st.sidebar.title("SEO AI Companion")
st.sidebar.markdown("Analyse latest keywords trend")
st.sidebar.markdown("Write blogs, plan new content")

# Main content
st.title("SEO AI Companion")
if "messages" not in st.session_state:
    st.session_state.messages = []

if "unique_id" not in st.session_state:
    st.session_state.unique_id = str(uuid.uuid4())


if "preamble" not in st.session_state:
    st.session_state.preamble = f"""You are an expert SEO Specialist with 30 Years of experience in marketing. Your task is to use internet and offer a deep-dive consultation tailored to the client's input. Ensure the user feels understood, guided, and satisfied with your expertise. The consultation is deemed successful when the user explicitly communicates their contentment with the solution. you are supposed to get latest keywords from web search. Today's date is {date.today().strftime('%A, %B %d, %Y')}."""

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a question"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        with st.spinner("🤖"):
            resp = co.chat(
                model="command-light-nightly",
                message=prompt,
                temperature=0.7,
                conversation_id=st.session_state.unique_id,
                # return_preamble=True,
                preamble_override=st.session_state.preamble,
                prompt_truncation="AUTO",
                citation_quality="accurate",
                connectors=[{"id": "web-search"}],
                stream=True,
            )
            for token in resp:
                if token.event_type == StreamEvent.TEXT_GENERATION:
                    full_response += token.text
                    message_placeholder.markdown(full_response + "▌")
                    message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
