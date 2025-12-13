# *Task 4: Cloud-Based AI Chatbot*

This project implements a cloud-powered AI chatbot using *Google Gemini 2.5 Flash*. The chatbot provides instant responses via a simple web interface and demonstrates how cloud-based AI services integrate with real-world applications.

---

## *✨ Features*

- Fully generative chatbot using *Gemini AI*
- Simple and clean Web UI (HTML, CSS, JS)
- Flask backend for handling API requests
- Fast, cloud-based AI response generation

---

## *⚙ How It Works*

### *Step 1: Frontend*
index.html contains the user interface with a message input box and a chat display area.

### *Step 2: Backend*
chatbot.py built using Flask receives the user message and sends it to the Gemini API.

### *Step 3: Cloud AI*
Google Gemini (running on Google Cloud servers) processes the text and generates the AI response.

### *Step 4: Response Display*
The Flask backend returns the generated text to the browser, where it is displayed instantly.

---

# Setup Instructions

## Clone the repository

```bash
git clone https://github.com/username/repo-name.git
cd repo-name
```

## Create a .env file from the example

```bash
cp .env.example .env
```

## Add your Gemini API key

```env
GEMINI_API_KEY=YOUR_API_KEY
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Flask backend

```bash
python chatbot.py
```

## Open the web UI

Open `index.html` using **VS Code Live Server** or a browser.

Type a message and get instant responses from the cloud AI chatbot.

---

# Cloud Computing Role

* The chatbot uses **Google Gemini API**, which runs entirely on **Google Cloud**.
* All message processing and AI computations happen in the cloud, not on the local machine.
* The backend only sends requests and receives responses, demonstrating serverless cloud inference.
* This shows practical integration of cloud AI services into a web application.
