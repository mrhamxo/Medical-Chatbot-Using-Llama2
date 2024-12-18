# Medical Chatbot Using Llama 

This project is a **Generative AI Medical Chatbot** built using **Llama 2** and **Pinecone** for document retrieval. The chatbot is capable of understanding medical inquiries and providing responses based on indexed medical documents. It utilizes advanced NLP techniques to assist users with medical information while retrieving relevant information from PDFs and other documents.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The **Medical Chatbot** is designed to:
- Provide accurate answers to medical-related questions.
- Utilize a vector database for efficient document retrieval.
- Employ a lightweight and performant language model (Llama 2) for real-time question answering.

This project has the potential to assist users in obtaining preliminary medical information, making it easier to find relevant data from large medical datasets.

## Features
- **Real-time Medical Question Answering**: Provides responses to user queries based on the context of medical documents.
- **Pinecone Integration**: Utilizes Pinecone for fast, efficient vector-based document retrieval.
- **Llama 2 Integration**: Uses the Llama 2 model for natural language understanding and generation.
- **Document Loader**: Supports loading medical PDFs and indexing them for future retrieval.
- **User-Friendly Web Interface**: Built with Flask to provide an intuitive interface for users.

## Tech Stack
- **Llama 2**: A generative AI model used for text completion and answering questions.
- **Pinecone**: A vector database for fast and scalable document search.
- **Flask**: A web framework for building the chatbot interface.
- **Sentence-Transformers**: For embedding medical documents into vectors.
- **LangChain**: Manages the document retrieval process and LLM integrations.
- **HTML/CSS/JS**: For building the frontend of the chatbot.

## Installation

### Prerequisites
- Python 3.11+
- Pinecone account and API key
- Hugging Face account for downloading models (sentence-transformers/all-MiniLM-L6-v2)
- Download Llama 2 model from hugging face (llama-2-7b-chat.ggmlv3.q4_0.bin)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/medical-chatbot.git
   cd medical-chatbot
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root and add the following environment variables:
   ```plaintext
   PINECONE_API_KEY=your-pinecone-api-key
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in browser**
   Go to `http://127.0.0.1:5000` to access the chatbot interface.

## How It Works

### Document Embedding
The project uses **sentence-transformers** to embed medical documents (PDFs) into vectors. These embeddings are stored in a Pinecone index, allowing for fast retrieval based on user queries.

### Question Answering
The user asks a medical question via the web interface. The chatbot:
1. Converts the question into an embedding using Llama 2.
2. Uses Pinecone to retrieve the most relevant documents based on the embedding.
3. The Llama 2 model generates a response based on the retrieved documents.

### Workflow
1. Upload and index medical documents (PDFs).
2. User submits a question via the web interface.
3. The chatbot retrieves relevant documents from Pinecone.
4. Llama 2 generates and returns the answer.

## Usage

1. **Ask a question**: Use the web interface to input medical questions.
2. **Get an answer**: The chatbot will fetch the most relevant information from the documents and provide an answer.
3. **Upload medical documents**: You can upload new medical PDFs to enhance the chatbot’s knowledge base.

## Project Structure
```
medical-chatbot/
│
├── data/
│   └── Medical_book.pdf         # Medical document for chatbot knowledge base
│
├── model/
│   ├── instruction.txt          # Instruction file for model usage
│   └── llama-2-7b-chat.ggmlv3.q4_0.bin  # Llama 2 model weights for chatbot
│
├── research/
│   └── experiments.ipynb        # Jupyter notebook for research and experiments
│
├── src/
│   ├── __pycache__/             # Compiled Python files
│   ├── chatbotlogo.jpg          # Chatbot logo for web interface
│   ├── helper.py                # Helper functions for downloading models and embeddings
│   └── prompt.py                # Prompt template and structure for the chatbot
│
├── static/
│   └── style.css                # CSS for the web interface
│
├── templates/
│   └── chat.html                # HTML template for the chatbot UI
│
├── .env                         # Environment variables for the project
├── .gitignore                   # Git ignore file for ignoring unnecessary files
├── app.py                       # Flask application entry point
├── folder_structure.py           # Script for managing folder structure
├── LICENSE                      # License file for the project
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies for the project
├── setup.py                     # Setup script for the project
└── store_index.py               # Script for indexing documents into Pinecone

```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
### Conclusion

The **Medical Chatbot Using Llama 2** successfully demonstrates the potential of leveraging Generative AI models, like Llama 2, to enhance healthcare services. By integrating Pinecone for vector storage and a state-of-the-art embedding model, the chatbot can retrieve relevant medical information from PDFs and respond to user queries in real-time. This application not only provides a conversational interface for users to access medical knowledge but also serves as a foundation for further enhancements, such as integrating more medical datasets and improving the model's understanding of complex medical queries.

This project highlights the growing significance of AI in healthcare, enabling more accessible and efficient communication of medical knowledge to patients and professionals alike. As technology evolves, further advancements can be made in this chatbot to support a broader range of medical queries, including diagnosis assistance and symptom analysis, ensuring it can be used for practical and commercial purposes in the healthcare industry.
