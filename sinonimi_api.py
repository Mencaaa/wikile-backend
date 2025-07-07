# sinonimi_api.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from gensim.models import KeyedVectors

app = Flask(__name__)
CORS(app)  # permette l'accesso da JavaScript in browser
model = KeyedVectors.load("C:\Wikile\wikile2\wikile3\Scripts\word2vec.wordvectors", mmap='r')

@app.route('/sinonimi', methods=['GET'])
def sinonimi():
    parola = request.args.get('word')
    try:
        simili = model.most_similar(parola, topn=50)
        filtrati = [item for item in simili if item[1] >= 0.5]
        return jsonify(filtrati)

    except KeyError:
        return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
