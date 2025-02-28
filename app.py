# __import__('pysqlite3')
# import sys
# sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
from streamlit_chat import message
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from function import *
from langchain.chains import LLMChain
import os
from langchain_groq import ChatGroq
import time

def  main():
    st.set_page_config(layout="wide")

    if "history" not in st.session_state:
        st.session_state.history = ""

    st.markdown("<h1 style='text-align: center; color: blue;'> Medical Assistant </h1>", unsafe_allow_html=True)
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What would you like to ask?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Update sales history in session_state
        st.session_state.history += "\nUser: " + prompt

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            output = chat_response_qroq(st.session_state.history)
            output = output.lstrip("\n")
            response = st.write_stream(response_generator(output))


        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        # Update sales history with assistant response
        st.session_state.history += "\nAI: " + output

    
from streamlit.web import cli as stcli
from streamlit import runtime
import sys

if __name__ == '__main__':
    main()
