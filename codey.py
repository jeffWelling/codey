# Copyright (c) 2024, Jeff Welling
# All rights reserved.
# 
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. 

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.embeddings import resolve_embed_model
from llama_index.llms.ollama import Ollama
import streamlit as st
import asyncio

@st.cache_resource(show_spinner=False)
def load_data() -> VectorStoreIndex:
    with st.spinner(text="Loading and indexing the document data..."):
        documents = SimpleDirectoryReader("codey_data").load_data()
        return VectorStoreIndex.from_documents(documents)

my_model = "llama3:latest"
help_prompt = "How can I help?"
system_prompt = """You are an expert software developer specializing in golang,
python, algorithms, and data structures. Your job is to assist with the design
and development of software, but you answer general questions as well. You are
very helpul, creative, witty and excellent at problem solving. Assume the
language being used is golang unless specified. You do not hallucinate or make
up facts."""

# Setup the web interface
st.title("Codey")
st.subheader(help_prompt)

# bge embedding model
Settings.embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5")

# ollama
Settings.llm = Ollama(model=my_model, request_timeout=900)

#query_engine = index.as_query_engine()
#response = query_engine.query("Please explain giticket")
#print(response)

if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": help_prompt}
    ]

index = load_data()

chat_engine = index.as_chat_engine(
    chat_mode="context", verbose=True, system_prompt=system_prompt
)

if prompt := st.chat_input(help_prompt):
    st.session_state.messages.append({"role": "user", "content": prompt})

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Hmmmm..."):

            # Ensure there is an event loop for the current thread
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            # Now call the asynchronous operation with the new event loop
            streaming_response = chat_engine.stream_chat(prompt)
            placeholder = st.empty()
            full_response = ''
            for token in streaming_response.response_gen:
                full_response += token
                placeholder.write(full_response)
            placeholder.markdown(full_response)
            message = {"role": "assistant", "content": full_response}
            st.session_state.messages.append(message)

            # Close the event loop
            loop.close()
