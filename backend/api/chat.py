from flask import Blueprint, request, jsonify
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # 加载 .env 文件中的环境变量

chat_bp = Blueprint('chat', __name__)

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

if not DEEPSEEK_API_KEY:
    raise ValueError("DeepSeek API key not found in environment variables.")

client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

@chat_bp.route('/completions', methods=['POST'])
def create_completion():
    data = request.get_json()
    message = data.get('message')

    if not message:
        return jsonify({'error': 'Message is required'}), 400

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ],
            stream=False
        )
        return jsonify({'response': response.choices[0].message.content})
    except Exception as e:
        return jsonify({'error': str(e)}), 500