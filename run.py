from gensim.models import Word2Vec
from flask import Flask, jsonify
import time

app = Flask(__name__)

MODEL_URL = 'https://storagerat.blob.core.windows.net/telda/word2vec.model?sp=r&st=2020-07-29T14:24:29Z&se=2020-12-29T22:24:29Z&spr=https&sv=2019-12-12&sr=b&sig=KmUc2NjsbLa9NHrs4uytJ5WCxQUKymW2pbKVS%2F1GGyo%3D'
st = time.time()
print('Loading Model .....')
model = Word2Vec.load(MODEL_URL)
ed = time.time() - st
print('Model Loaded in : {0} s'.format(ed))

@app.route('/')
def hello():
    return 'Hello to Aspect model'


@app.route('/word2vec/<string:word>')
def hello_user(word):
    print('Word is: {0}'.format(word))
    data = {
        "word" : word,
        "vector": model[word].tolist()
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug = True)