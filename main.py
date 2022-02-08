import os
from flask import Flask, render_template
from flask import request
import urllib.request
from urllib.request import urlopen
from flask import json
import re
from flask import Response


app = Flask(__name__)

@app.route("/")
def forms():
    return (render_template('access.html'))

@app.route("/", methods=['POST'])
def form():
    error = "API key error"
    text = request.form['key']
    access_key = text
    return index()


@app.route("/")
def index():
    text = request.form['key']
    access_key = text
    ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    ip_space = ip.replace(" ", "")
    ip_split = ip_space.split(",", 1)
    ip_api = ip_split[0]

    check_api = "http://api.ipstack.com/check?access_key="+ access_key +"&output=json&fields=ip,city,zip,latitude,longitude"
    api = "http://api.ipstack.com/" + ip_api + "?access_key="+ access_key +"&output=json&fields=ip,city,zip,latitude,longitude"

    check_response = urllib.request.urlopen(check_api).read().decode('UTF-8')
    check_data = json.loads(check_response)
    code = "200"
    if code == "200":
        stackip = (check_data['ip'])
        stackcity = (check_data['city'])
        stackzip = (check_data['zip'])
    else:
        error = (check_response['error'])
        print (error)

    ip_response = urllib.request.urlopen(api).read().decode('UTF-8')
    ip_data = json.loads(ip_response)
    if code == "200":
        stack_ip = (ip_data['ip'])
        stack_city = (ip_data['city'])
        stack_zip = (ip_data['zip'])
        return (render_template('index.html', **locals()))
    else:
        error = (ip_response['error'])
        print (error)






if __name__ == "__main__":
    app.run(debug=True)
