from agent_1 import AGENT_1
from agent_2 import AGENT_2

import validators
import streamlit as st
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler

# st.set_page_config(page_title="Eddy - Your AI Assistant", layout="wide")
st.title("🤖 Eddy - Your AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask me anything...")

if user_input:  
    # Determine which agent to use
    if validators.url(user_input):
        response = AGENT_2(user_input)
    else:
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = AGENT_1.invoke({"user_input":user_input},
                                  config={"callbacks": [st_cb]})["output"]

    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Display response
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
