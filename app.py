from flask import Flask,jsonify
import sys
import json
import urllib
import requests
import base64

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

@app.route("/v1/<filename>")
def getFileFromGithub(filename):
       loadUrl= requested_url + '/'+filename
       resp = urllib.urlopen(loadUrl)

       if resp.getcode() == 200:
           data = json.load(resp)
           downloadUrl = data['download_url']
           requested_data  = urllib.urlopen(downloadUrl)
           return requested_data.read()
       return 'Enter Valid URL!'


if __name__ == "__main__":
    entered_url = sys.argv[1]
    github_api_url = "https://api.github.com/repos/"
    url = entered_url.replace("https://github.com/",github_api_url)
    requested_url = url+"/contents"
    app.run(debug=True,host='0.0.0.0')
