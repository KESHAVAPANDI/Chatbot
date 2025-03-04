from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

genai.configure(api_key="AIzaSyDN21QhPgXTWrahnoNf8WnVTTdhHTlEucw")

# models = genai.list_models()

# for model in models:
#     print(model.name, model.supported_generation_methods)


model = genai.GenerativeModel("gemini-2.0-flash")

system_prompt = """
You are a highly intelligent AI personal assistant. You can chat freely on any topic, 
answer questions, provide suggestions, and assist with daily tasks. 
Engage in conversations naturally while being helpful and professional.
"""

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Message cannot be empty"}), 400

    response = model.generate_content(system_prompt + "\nUser: " + user_message)
    return jsonify({"response": response.text})

if __name__ == "__main__":
    app.run(debug=True)
