from flask import Flask, jsonify

from dictionary_entry import Dictonary_Entry

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_SORT_KEYS'] = False

@app.route('/<word>')
def word(word):
    entry = Dictonary_Entry(word)
    return jsonify({
      'word' : word,
      'defitions' : entry.defitions
    }), 200

@app.route('/<word>/pronounciation')
def summary(word):
    entry = Dictonary_Entry(word)
    return entry.get_pronounciation(), 200