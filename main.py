import os
from flask import Flask
from flask import request
import urllib.request
from flask import json


app = Flask(__name__)

@app.route("/")
def index():
    #access_key = ""
    api = "http://api.ipstack.com/check?access_key=37a43eb5e02577a7ede5e49de1e5b330&output=json&fields=ip,city,zip,latitude,longitude"
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR')
    response = urllib.request.urlopen(api).read().decode('UTF-8')
    data = json.loads(response)

    return (
    (data['ip'])
    +(data['city'])
    +(data['zip'])
    )




if __name__ == "__main__":
    app.run(debug=True)
