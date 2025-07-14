# 🚀 PromptCue AI Engineer Internship Project: Multi-Model LLM Chat Service

This repository contains my technical submission for the **PromptCue AI Engineer Internship**. It showcases a clean, minimal, and functional **multi-model LLM chat API** built using Python and Flask, integrating with hosted models via the **Groq API**.

---

## 📌 Project Overview

The core of this project is a RESTful Flask service that allows users to interact with two different Large Language Models (LLMs) by sending prompts via a single HTTP endpoint. The design emphasizes simplicity, performance logging, and ease of configuration.

---

## 🔧 Key Features

- **`/chat` HTTP Endpoint**  
  Accepts `POST` requests with a user prompt in JSON format.

- **Multi-Model Routing**  
  Dynamically selects between two hosted models:  
  - `llama3-8b`  
  - `llama3-70b`  
  Controlled via a query parameter: `?model=llama3-8b`.

- **Structured Logging**  
  Each request is logged into `logs.json` with:
  - Timestamp  
  - Selected model  
  - Input prompt  
  - Generated response  
  - Latency in milliseconds  
  - Token usage

- **API Key Security**  
  Uses environment variables to manage the Groq API key securely.

- **Clean Dependencies**  
  All required packages are listed in `requirements.txt` for easy setup.

---

## 📁 Project Structure

```bash
.
├── app.py            # Main Flask server logic
├── requirements.txt  # Python dependencies
├── logs.json         # Sample log file (auto-generated)
└── README.md         # Project documentation


## ⚙️ Setup & Installation
1. Prerequisites

    Python 3.8 or higher

    Valid Groq API Key

2. Clone & Set Up

# Clone this repository
git clone <your-repo-url>
cd <your-project-directory>

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt



## ▶️ Running the Service
1. Set the API Key

Set your Groq API key as an environment variable:

export GROQ_API_KEY="your_groq_api_key_here"

2. Start the Flask Server

python app.py

The server will be accessible at:
http://127.0.0.1:5001/chat


## 🧪 Testing the API

You can test the chat service using curl:
✅ Test 1: Use Llama 3 (8B) Model

curl -X POST http://127.0.0.1:5001/chat?model=llama3-8b \
-H "Content-Type: application/json" \
-d '{"prompt": "What are three fun facts about the ocean?"}'

✅ Test 2: Use Llama 3 (70B) Model

curl -X POST http://127.0.0.1:5001/chat?model=llama3-70b \
-H "Content-Type: application/json" \
-d '{"prompt": "Write a short story about a robot who discovers music."}'

You will receive a JSON response with the model’s reply. Each request is logged in logs.json.


## 💬 Author
Pranav Mohan