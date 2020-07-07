from flask import Flask, request, abort, jsonify
import os

app = Flask(__name__)

@app.route("/status")
def status():
    return("The Visualisation Test Plugin Flask Server is up and running")

@app.route("/evaluate", methods=["POST", "GET"])
def evaluate():
    return("The type sent is an accepted type")

@app.route("/run", methods=["POST"])
def run():
    data = request.get_json(force=True)
    return jsonify(data)
    #cwd = os.getcwd()
    #filename = os.path.join(cwd, "Test.html")
    #
    #data = request.get_json(force=True)
    #return jsonify(data)
    #
    #url = data['complete_sbol'].replace('/sbol','')
    #instance = data['instanceUrl']
    #uri = data['top_level']
    #
    #try:
        #with open(filename, 'r') as htmlfile:
            #result = htmlfile.read()
            #print("Hello")
            #
            #put in the url, uri, and instance given by synbiohub
            #result = result.replace("URL_REPLACE", url)
            #result = result.replace("URI_REPLACE", uri)
            #result = result.replace("INSTANCE_REPLACE", instance)
            #
        #result = result.replace("REQUEST_REPLACE", data)
        #
        #return result 
    #except Exception as e:
        #print(e)
        #abort(404)
#
