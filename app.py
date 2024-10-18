from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(_name_)

# Load your model here
chatbot = pipeline('conversational', model='your-fine-tuned-model')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = chatbot(user_input)
    return jsonify({'response': response})

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8080)
