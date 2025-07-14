
import os
import json
import time
import requests
from flask import Flask, request, jsonify

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


app = Flask(__name__)


request_logs = []
LOG_FILE = "logs.json"


if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r") as f:
        request_logs = json.load(f)

@app.route('/chat', methods=['POST'])
def chat_handler():
    
    if not GROQ_API_KEY:
        return jsonify({"error": "GROQ_API_KEY environment variable not set."}), 500

    start_time = time.time()
    
    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({"error": "Prompt not found in request body"}), 400
    
    user_prompt = data['prompt']

    model_choice = request.args.get('model', 'llama3-8b') 

    
    api_url = "https://api.groq.com/openai/v1/chat/completions"
    
    
    if model_choice.lower() == 'llama3-8b':
        model_name = "llama3-8b-8192"
    elif model_choice.lower() == 'llama3-70b':
        model_name = "llama3-70b-8192"  
    else:
        return jsonify({"error": f"Model '{model_choice}' is not supported. Please use 'llama3-8b' or 'llama3-70b'."}), 400

    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    formatted_prompt = [{"role": "user", "content": user_prompt}]

    
    try:
        response = requests.post(
            api_url,
            headers=headers,
            json={"model": model_name, "messages": formatted_prompt}
        )
        response.raise_for_status()
        
        api_response_data = response.json()
        
        model_response_text = api_response_data['choices'][0]['message']['content']
        token_count = api_response_data['usage']['total_tokens']

    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"API request failed: {e}"}), 500
    
    end_time = time.time()
    latency = round((end_time - start_time) * 1000)

    log_entry = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "model_used": model_choice,
        "prompt": user_prompt,
        "response": model_response_text,
        "latency_ms": latency,
        "token_count": token_count
    }
    request_logs.append(log_entry)

    with open(LOG_FILE, "w") as f:
        json.dump(request_logs, f, indent=4)

    return jsonify({
        "status": "success",
        "model": model_choice,
        "response": model_response_text
    })

if __name__ == '__main__':
    app.run(port=5001, debug=True)