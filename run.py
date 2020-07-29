from gensim.models import Word2Vec
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
   return 'Hello to Aspect model'


@app.route('/word2vec/<word>')
def hello_user(word):
   return jsonify({"word":word})

if __name__ == '__main__':
   app.run(debug = True)