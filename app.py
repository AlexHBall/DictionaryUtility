from flask import Flask, jsonify

from dictionary_entry import Dictonary_Entry

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_SORT_KEYS'] = False


@app.route('/fortune', methods=['GET'])
def fortune():
    return jsonify({
        'data': 'How many of you believe in psycho-kinesis? Raise my hand.',
        'status': 'awesome'
    }), 200

@app.route('/<word>')
def profile(word):
    entry = Dictonary_Entry(word)
    return jsonify({
      'word' : word,
      'defitions' : entry.defitions
    }), 200

