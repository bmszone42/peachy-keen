import os
import streamlit as st
from datetime import datetime
from streamlit_chat import message
import random
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader, ServiceContext
from llama_index.llm_predictor.chatgpt import ChatGPTLLMPredictor

index_name = "./index.json"
documents_folder = "./documents"

st.markdown("<h1 style='text-align: center; color: red;'>Document Bot</h1>", unsafe_allow_html=True)

# @st.cache_resource
# def initialize_index(index_name, documents_folder):
#     llm_predictor = ChatGPTLLMPredictor()
#     service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
#     if os.path.exists(index_name):
#         index = GPTSimpleVectorIndex.load_from_disk(index_name, service_context=service_context)
#     else:
#         documents = SimpleDirectoryReader(documents_folder).load_data()
#         index = GPTSimpleVectorIndex.from_documents(documents, service_context=service_context)
#         index.save_to_disk(index_name)

#     return index

def save_uploaded_file(uploadedfile):
  with open(os.path.join("data",uploadedfile.name),"wb") as f:
     f.write(uploadedfile.getbuffer())
        
datafile = st.file_uploader("Upload your doc",type=['docx', 'doc', 'pdf'])

if datafile is not None:
    if not os.path.exists('./data'):
        os.mkdir('./data')
    save_uploaded_file(datafile)
    documents = SimpleDirectoryReader('data').load_data()
    
@st.cache_data(max_entries=200, persist=True)
def query_index(_index, query_text):
    response = _index.query(query_text)
    return str(response)

index = GPTSimpleVectorIndex.from_documents(documents)
index.save_to_disk('index.json')

index = GPTSimpleVectorIndex.load_from_disk('index.json')

user_query = st.text_input("You: ","", key= "input")
send_button = st.button("Send")

if send_button:
    send_message(user_query, st.session_state.all_messages)
    display_messages(st.session_state.all_messages)
    
if msg['user'] == 'user':
    message(f"You ({msg['time']}): {msg['text']}", is_user=True, key=int(time.time_ns()))
else:
    message(f"Bot ({msg['time']}): {msg['text']}", key=int(time.time_ns()))

     st.markdown(f"LLM Tokens Used: {index.service_context.llm_predictor._last_token_usage}")
     st.markdown(f"Embedding Tokens Used: {index.service_context.embed_model._last_token_usage}")
    
# st.title("🦙 Llama Index Demo 🦙")
# st.header("Welcome to the Llama Index Streamlit Demo")
# st.write("Enter a query about Paul Graham's essays. You can check out the original essay [here](https://raw.githubusercontent.com/jerryjliu/llama_index/main/examples/paul_graham_essay/data/paul_graham_essay.txt). Your query will be answered using the essay as context, using embeddings from text-ada-002 and LLM completions from ChatGPT. You can read more about Llama Index and how this works in [our docs!](https://gpt-index.readthedocs.io/en/latest/index.html)")

#st.secrets['OPENAI_API_KEY'] = api_key

# index = initialize_index(index_name, documents_folder)

# text = st.text_input("Query text:", value="What did the author do growing up?")

# if st.button("Run Query") and text is not None:
#     response = query_index(index, text)
#     st.markdown(response)
    
#     llm_col, embed_col = st.columns(2)
#     with llm_col:
#         st.markdown(f"LLM Tokens Used: {index.service_context.llm_predictor._last_token_usage}")
    
#     with embed_col:
#         st.markdown(f"Embedding Tokens Used: {index.service_context.embed_model._last_token_usage}")
