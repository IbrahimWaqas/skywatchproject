# Lab 3: Chatbot page
# TODO: Rename this file to fit your page. Keep the number at the front.
#
# A chatbot built with Pydantic AI (see the Pydantic AI pages on Canvas).
# It should:
#   - use a Pydantic AI Agent with instructions that fit your project's theme (no tools yet)
#   - use Streamlit's chat elements: st.chat_message and st.chat_input
#   - remember the conversation (message_history, saved in st.session_state)
#   - use try/except so an error shows a message instead of crashing the page
#   - stay on theme, without using any API or external data
#
# Your Gemini API key goes in .streamlit/secrets.toml as GOOGLE_API_KEY.

import streamlit as st
from pydantic_ai import Agent
import os 

st.title("SkyBot")
st.write("Ask me anything about air quality and pollution!")

os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

if "messages" not in st.session_state:
    st.session_state.messages = []

if "history" not in st.session_state:
    st.session_state.history = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Ask SkyBot a question")

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        try:
            agent = Agent(
                "google:gemini-3.5-flash-lite",
                instructions="You are SkyBot. Only discuss air quality and pollution. Keep answers short and simple. Remember the conversation. You cannot access live data. Do not invent pollution readings."
            )

            result = agent.run_sync(
                prompt,
                message_history=st.session_state.history
            )

            answer = result.output
            st.session_state.history = result.all_messages()

        except Exception as e:
            print(type(e).__name__, str(e))
            answer = "Sorry, something went wrong. Please try again."

        st.write(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })