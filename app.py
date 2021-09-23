#!/usr/bin/env python3
from flask import Flask, request, jsonify, make_response, abort
import json


# Set key "field1": http://localhost:8081/post
# Get key "field1": http://localhost:8081/get/field1
# Get history key "field1" : http://localhost:8081/history/field1

app = Flask(__name__)
#keyValue_db=[{
#        'key': name,
#        'value': value,
#        'version': version
#    }]
keyValue_db=[]

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/get/<name>', methods=['GET'])
def get_name(name):
    #Retrieving all elements where key=name
    list = [item['value'] for item in keyValue_db if item['key'] == name]
    if len(list) == 0:
        abort(404)
    #Returning the last one
    return jsonify(value = list[-1])


@app.route('/history/<name>', methods=['GET'])
def get_history_name(name):
    # Retrieving all elements where key=name
    list = [item for item in keyValue_db if item['key'] == name]
    if len(list) == 0:
        abort(404)
    return json.dumps(list)


@app.route('/post', methods=['POST'])
def post():

    r = request.form.to_dict()
    if not r["key"] or not r["value"]:
        abort(400)
    #retrieving key and value form the request
    name = r["key"]
    value = r["value"]

    version = 1
    version += len([item for item in keyValue_db if item['key'] == name])
    #building a new entry for the database
    item = {
        'key': name,
        'value': value,
        'version': version
    }
    #adding a new entry to the memory-based database
    keyValue_db.append(item)
    return jsonify({'result': 'done'})


if __name__ == "__main__":
    app.run(debug=True, port=8081)


