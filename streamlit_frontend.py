import streamlit as st
from langgraph_backend import chatbot

try:
    from langchain_core.messages import HumanMessage
except ImportError:
    HumanMessage = None

user_input = st.chat_input("Type your message here...")
CONFIG = {'configurable': {'thread_id': 'thread_1'}}

if 'messages_history' not in st.session_state:
    st.session_state['messages_history'] = []

for message in st.session_state['messages_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

if user_input:
    with st.chat_message("user"):
        st.session_state['messages_history'].append({'role': 'user', 'content': user_input})
        st.text(user_input)

    if HumanMessage is not None:
        message = HumanMessage(content=user_input)
    else:
        message = {'role': 'user', 'content': user_input}

    response = chatbot.invoke({'messages': [message]}, config=CONFIG)

    ai_message = response['messages'][-1].content
    with st.chat_message("assistant"):
        st.session_state['messages_history'].append({'role': 'assistant', 'content': ai_message})
        st.text(ai_message)
    
    # with st.chat_message("assistant"):
    #     st.session_state['messages_history'].append({'role': 'assistant', 'content': user_input})
    #     st.text(user_input)




# with st.chat_message("user"):
#     st.text("Hi")

# with st.chat_message("assistant"):
#     st.text("Hello! How can I assist you today?")

# with st.chat_message("user"):
#     st.text("My Name is Trupti..")

# user_input = st.chat_input("Type your message here...")

# if user_input:
#     with st.chat_message("user"):   
#         st.text(user_input)