import os
import random
import time
import streamlit as st
from datetime import datetime
from streamlit_chat import message, chat
from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
import docx2txt
import PyPDF2
from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image
from io import BytesIO
import docx

st.markdown("<h1 style='text-align: center; color: green;'>Llamalytics Buddy 🦙📊</h1>", unsafe_allow_html=True)
custom_css = """
<style>
    @keyframes float {
        0% {
            transform: translateY(0px);
        }
        50% {
            transform: translateY(-10px);
        }
        100% {
            transform: translateY(0px);
        }
    }
    h1 {
        animation: float 3s ease-in-out infinite;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)


buff, col, buff2 = st.columns([1,3,1])
# openai_key = col.text_input('OpenAI Key:')
# os.environ["OPENAI_API_KEY"] = openai_key


if 'all_messages' not in st.session_state:
    st.session_state.all_messages = []

def save_uploaded_file(uploadedfile):
  with open(os.path.join("data",uploadedfile.name),"wb") as f:
     f.write(uploadedfile.getbuffer())

# Create a function to get bot response
def get_bot_response(user_query):
    response = index.query(user_query)
    return str(response)

# # Create a function to display messages
# def display_messages(all_messages):
#     for msg in all_messages:
#         if msg['user'] == 'user':
#             message(
#                 f'**You ({msg["time"]}):** {msg["text"]}',
#                 is_user=True,
#                 avatar_style="adventurer",
#                 seed=123,
#             )
#         else:
#             message(
#                 f'**Bot ({msg["time"]}):** {msg["text"]}',
#                 is_user=False,
#                 avatar_style="adventurer",
#                 seed=123,
#             )

def display_messages(all_messages):
    user_style = "bottts"
    bot_style = "bottts"

    user_base_color = "f44336"
    user_eyes = 5
    user_face = 6
    user_mouth = 6

    bot_base_color = "4caf50"
    bot_eyes = 4
    bot_face = 4
    bot_mouth = 4

    user_avatar_style = f"{user_style}?baseColor={user_base_color}&eyes={user_eyes}&face={user_face}&mouth={user_mouth}"
    bot_avatar_style = f"{bot_style}?baseColor={bot_base_color}&eyes={bot_eyes}&face={bot_face}&mouth={bot_mouth}"

    for msg in all_messages:
        if msg['user'] == 'user':
            message(
                f"You ({msg['time']}): {msg['text']}",
                is_user=True,
                avatar_style=user_avatar_style,
                seed=123,
            )
        else:
            message(
                f"Bot ({msg['time']}): {msg['text']}",
                is_user=False,
                avatar_style=bot_avatar_style,
                seed=456,
            )
    chat_object.display()
            
# Create a function to send messages
def send_message(user_query, all_messages):
    if user_query:
        all_messages.append({'user': 'user', 'time': datetime.now().strftime("%H:%M"), 'text': user_query})
        
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
                
        bot_response = get_bot_response(user_query)
        all_messages.append({'user': 'bot', 'time': datetime.now().strftime("%H:%M"), 'text': bot_response})

        st.session_state.all_messages = all_messages

     
# Create a list to store messages
st.sidebar.title("Settings")
# st.sidebar.subheader("Theme")
# theme = st.sidebar.radio("Choose your theme", ("Light", "Dark", "Crazy Llama"))

# custom_theme_css = ""
# if theme == "Dark":
#     custom_theme_css = """
#     <style>
#         body {
#             background-color: #1f1f1f;
#             color: #ffffff;
#         }
#     </style>
#     """
# elif theme == "Crazy Llama":
#     custom_theme_css = """
#     <style>
#         body {
#             background-color: #ffffff;
#             color: #1aff00;
#         }
#     </style>
#     """
# else:
#     custom_theme_css = """
#     <style>
#         body {
#             background-color: #ffffff;
#             color: #000000;
#         }
#     </style>
#     """

# st.markdown(custom_theme_css, unsafe_allow_html=True)

datafile = st.sidebar.file_uploader("Upload your doc",type=['docx', 'doc', 'pdf'])
if datafile is not None:
    if not os.path.exists('./data'):
        os.mkdir('./data')
    save_uploaded_file(datafile)
    documents = SimpleDirectoryReader('data').load_data()
    index = GPTSimpleVectorIndex.from_documents(documents)

    index.save_to_disk('index.json')

    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    
     # Add a file preview
    st.markdown("**File Preview:**")
    if datafile.type == 'application/pdf':
        images = convert_from_bytes(datafile.read())
        for idx, img in enumerate(images):
            st.subheader(f"Page {idx + 1}")
            st.image(img, width=600)
    elif datafile.type in ['application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
        doc = docx.Document(BytesIO(datafile.read()))
        for idx, paragraph in enumerate(doc.paragraphs):
            st.write(paragraph.text)
            if idx > 10:  # Limit the number of paragraphs displayed
                break

                
    # Add this line before the "Create input text box for user to send messages" line
    progress_bar = st.progress(0)

    # Create input text box for user to send messages
    user_query = st.text_input("You: ","", key= "input")

    # Create a button to send messages
    send_button = st.button("Send")

    # Send message when button is clicked
    if send_button:
        send_message(user_query, st.session_state.all_messages)
        display_messages(st.session_state.all_messages)
        st.markdown(f"LLM Tokens Used: {index.service_context.llm_predictor._last_token_usage}")
        st.markdown(f"Embedding Tokens Used: {index.service_context.embed_model._last_token_usage}")
    
