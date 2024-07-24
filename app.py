from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=data['prompt'],
        max_tokens=150
    )
    return jsonify(response.choices[0].text.strip())

if __name__ == '__main__':
    app.run(debug=True)
