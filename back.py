from flask import Flask, render_template, request
import requests
import simplejson as json

app = Flask(__name__)

@app.route("/doit", methods = ['GET','POST'])
def jawn():
	if request.method == 'POST':	
		user = request.form.get('user', '')
		print user
		number = request.form.get('number', '')
		print number
	else:
		user = request.args.get('user', '')
		print user
		number = request.form.get('number', '')
		print number
	
	url = requests.get("https://api.twitter.com/1.1/search/tweets.json?q=@" + user + "&count=100")

if name == "__main__":
	app.run()
	
