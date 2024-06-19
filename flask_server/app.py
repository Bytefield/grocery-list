from flask import Flask, jsonify, request
from flask_cors import CORS
from transformers import BertTokenizer

app = Flask(__name__)
CORS(app)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

@app.route('/api/data', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        data = request.get_json()
        # Tokenize the data here
        tokenized_data = tokenizer.tokenize(data['text'])
        return jsonify(tokenized_data)
    else:
        return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(debug=True)