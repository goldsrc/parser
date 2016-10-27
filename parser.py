from flask import request,Flask,Response
from nltk.tokenize import word_tokenize
import nltk,json,argparse
from itertools import izip

app = Flask(__name__)
@app.route('/parse', methods=['GET', 'POST'])

def test():
    dt=''
    if request.method == 'POST':
        sentence = request.form['sent']
        tokens = word_tokenize(sentence)
        tags = nltk.pos_tag(tokens)
        dt=json.dumps(fixer(tags),indent=4, sort_keys=True)
    return Response(dt, mimetype='text/json')

def fixer(lst):
    retval=[]
    for item in lst:
        it=iter(item)
        dic=dict(izip(it,it))
        retval.append(dic)
    return retval

if __name__ == '__main__':
    #----------- Parsing Arguments ---------------
    p = argparse.ArgumentParser()
    p.add_argument("--port", help="Port (default: 5000)")
    args = p.parse_args()
    port = int(args.port) if args.port else 5000
    if not args.model:
        print "Usage: parser.py [--port 1234]"
    app.run(port=port)