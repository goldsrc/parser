#importing required libraries
from flask import request,Flask,Response
from nltk.tokenize import word_tokenize
import nltk,json,argparse
from itertools import izip

#initialize flask app
app = Flask(__name__)
@app.route('/parse', methods=['GET', 'POST'])

#flask main method
def tagger():
    tags=[{}]
    if request.method == 'POST':
        sentence = request.form['sent']
        tokens = word_tokenize(sentence)
        tags = nltk.pos_tag(tokens)
    return Response(json.dumps(fixer(tags),indent=4, sort_keys=True), mimetype='text/json')

#convert list to dictionary
def fixer(lst):
    retval=[]
    for item in lst:
        it=iter(item)
        dic=dict(izip(it,it))
        retval.append(dic)
    return retval

if __name__ == '__main__':
    #Parsing Arguments
    p = argparse.ArgumentParser()
    p.add_argument("--port", help="Port (default: 5000)")
    args = p.parse_args()
	#setting port for the service
    port = int(args.port) if args.port else 5000
    app.run(port=port)
