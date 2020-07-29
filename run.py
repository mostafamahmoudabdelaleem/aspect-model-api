from gensim.models import Word2Vec
from flask import Flask, jsonify
import time
import threading

app = Flask(__name__)

MODEL_URL = 'https://storagerat.blob.core.windows.net/telda/word2vec-100.model?sp=r&st=2020-07-29T17:11:38Z&se=2020-12-30T01:11:38Z&spr=https&sv=2019-12-12&sr=b&sig=0uLLfwejVAc%2FcDR3sESRgDIzaRSGvjCWpZrSWYZ57Xc%3D'
model = None

def load_model():
    global model
    if(model == None):
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
    global model
    print('Word is: {0}'.format(word))
    if model != None:
        if(word in model):
            data = {
                "word" : word,
                "vector": model[word].tolist()
            }
        else:
            data = {
                "err" : "Word <{0}> not found in model.".format(word),
            }
        return jsonify(data)
    else:
        threading.Thread(target=load_model).start()
        return 'model not loaded'

if __name__ == '__main__':
    threading.Thread(target=load_model).start()
    app.run(debug = True)