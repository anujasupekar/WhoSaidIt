from flask import Flask, send_from_directory
from Quotes import Quotes
import json

app = Flask(__name__)

WEB_URL = '/Users/gautam/anju/WhoSaidIt/web/'
f = open('/Users/gautam/anju/WhoSaidIt/data/quoteData.json', 'r')
quoteData = json.loads(f.read())

quotes = Quotes(quoteData)

@app.route('/')
def root():
    return send_from_directory(WEB_URL, 'index.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory(WEB_URL+'js/', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory(WEB_URL+'css/', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory(WEB_URL+'img/', path)

#list of ids
@app.route("/quotes")
def IDList():
	return json.dumps(quotes.getJSON())

@app.route("/quotes/<quoteid>")
def getQuote(quoteid):
	return json.dumps((quotes.getQuote(quoteid)).getJSON())

@app.route("/quotes/<quoteid>/<personKey>")
def getName(quoteid, personKey):
	return json.dumps(((quotes.getQuote(quoteid)).getCharactersObj()).getNameByKey(personKey))

if __name__ == "__main__":
    app.run()