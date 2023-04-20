# Llamalytics Buddy 🦙📊

Llamalytics Buddy is a user-friendly, GPT-based file reader and Q&A bot that dives into your data and delivers insights by answering questions like a knowledgeable companion. It supports document formats such as `.docx`, `.doc`, and `.pdf`.

## Features

- Upload and process documents in `.docx`, `.doc`, and `.pdf` formats
- Retrieve answers to your questions based on the content of uploaded files
- Utilizes GPT-based information retrieval for fast and accurate responses
- Friendly and intuitive Streamlit-based web interface

## Installation

1. Clone the repository:

git clone https://github.com/yourusername/llamalytics-buddy.git


2. Change the working directory:

cd llamalytics-buddy

3. Install the requirements:

pip install -r requirements.txt

4. Set the OpenAI API key as an environment variable:

export OPENAI_API_KEY="your_api_key_here"


## Usage

1. Run the Streamlit app:

streamlit run app.py

2. Access the app on your browser by navigating to the URL displayed in your terminal, usually `http://localhost:8501`.

3. Upload your document(s) by clicking on "Upload your doc" and selecting the desired file(s).

4. Type your question in the text input box and click "Send" to get an answer based on the content of the uploaded file(s).

5. The app will display both your query and the Llamalytics Buddy's response.

## Dependencies

- streamlit
- docx2txt
- PyPDF2
- llama_index
- GPTSimpleVectorIndex
- SimpleDirectoryReader

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
