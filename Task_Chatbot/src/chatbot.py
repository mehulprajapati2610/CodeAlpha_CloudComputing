from flask import Flask, request, jsonify
from flask_cors import CORS 
from google.genai import Client
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = Client(api_key=api_key)
MODEL = "models/gemini-2.5-flash"

app = Flask(__name__)
CORS(app)  

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")
    if not user_msg:
        return jsonify({"reply": "Please send a message!"})

    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=user_msg
        )
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
