import os
from flask import Flask, render_template
from flask import request
import urllib.request
from flask import json
import re


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    #access_key = ""
    ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    ip_space = ip.replace(" ", "")
    ip_split = ip_space.split(",", 1)
    ip_api = ip_split[0]
    check_api = "http://api.ipstack.com/check?access_key=7bb51c62bdd1247a480ed6f5c972635f&output=json&fields=ip,city,zip,latitude,longitude"
    api = "http://api.ipstack.com/" + ip_api + "?access_key=7bb51c62bdd1247a480ed6f5c972635f&output=json&fields=ip,city,zip,latitude,longitude"

    check_response = urllib.request.urlopen(check_api).read().decode('UTF-8')
    check_data = json.loads(check_response)
    stackip = (check_data['ip'])
    stackcity = (check_data['city'])
    stackzip = (check_data['zip'])

    ip_response = urllib.request.urlopen(api).read().decode('UTF-8')
    ip_data = json.loads(ip_response)
    stack_ip = (ip_data['ip'])
    stack_city = (ip_data['city'])
    stack_zip = (ip_data['zip'])


    return (
    render_template('index.html', **locals())
    )



if __name__ == "__main__":
    app.run(debug=True)
