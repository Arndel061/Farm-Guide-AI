from flask import Flask, request, jsonify
import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file (for OpenAI key)
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to FarmGuard-AI 👨‍🌾🚜"

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    crop = data.get('crop')
    symptom = data.get('symptom')
    location = data.get('location')

    # Dummy response — we’ll make it smarter later using AI
    advice = f"For your {crop} in {location} showing '{symptom}', it's best to apply compost and monitor water drainage."

    return jsonify({
        "crop": crop,
        "symptom": symptom,
        "location": location,
        "advice": advice
    })

if __name__ == '__main__':
    app.run(debug=True)
