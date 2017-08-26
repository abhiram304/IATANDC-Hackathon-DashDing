#!flask/bin/python
from flask import request, render_template, Flask
import db, os, sys, json
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return  "hello"

'''
@app.route('/web_hook', methods=['POST'])
def web_hook():
	body = json.loads(request.data)
	return json.dumps(body)
'''
if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	#app.run(debug=True)
