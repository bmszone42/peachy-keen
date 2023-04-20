Llamalytics Buddy 🦙📊
Llamalytics Buddy is a user-friendly, GPT-based file reader and Q&A bot that dives into your data and delivers insights by answering questions like a knowledgeable companion. It supports document formats such as .docx, .doc, and .pdf.

Features
Upload and process documents in .docx, .doc, and .pdf formats
Retrieve answers to your questions based on the content of uploaded files
Utilizes GPT-based information retrieval for fast and accurate responses
Friendly and intuitive Streamlit-based web interface
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/llamalytics-buddy.git
Change the working directory:
bash
Copy code
cd llamalytics-buddy
Install the requirements:
Copy code
pip install -r requirements.txt
Set the OpenAI API key as an environment variable:
arduino
Copy code
export OPENAI_API_KEY="your_api_key_here"
Usage
Run the Streamlit app:
arduino
Copy code
streamlit run app.py
Access the app on your browser by navigating to the URL displayed in your terminal, usually http://localhost:8501.

Upload your document(s) by clicking on "Upload your doc" and selecting the desired file(s).

Type your question in the text input box and click "Send" to get an answer based on the content of the uploaded file(s).

The app will display both your query and the Llamalytics Buddy's response.

Dependencies
streamlit
docx2txt
PyPDF2
llama_index
GPTSimpleVectorIndex
SimpleDirectoryReader
Contributing
Fork the repository
Create your feature branch (git checkout -b feature/fooBar)
Commit your changes (git commit -am 'Add some fooBar')
Push to the branch (git push origin feature/fooBar)
Create a new Pull Request
License
This project is licensed under the MIT License - see the LICENSE file for details.
