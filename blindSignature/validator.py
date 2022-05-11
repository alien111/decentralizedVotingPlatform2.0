from tools import *
import json
from flask import Flask, jsonify, request
import requests
import sys


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

if (sys.argv[1] == '--port'):
	validatorPort = int(sys.argv[2])


@app.route('/getPublicKey', methods=['GET'])
def getPublicKey():
	answer = {'publicKey' : publicKey}
	return jsonify(answer), 200


@app.route('/signData', methods=['POST'])
def signData():
	values = request.get_json(force=True, silent=True, cache=False)
	required = ['data']

	if not all(i in values for i in required):
		return "Some data is missing", 400

	data = values['data']

	signedData = sign(data, privateKey)
	answer = {'signedData' : signedData}

	return jsonify(answer), 201


@app.route('/nodes/ping', methods=['GET'])
def ping():
	answer = {'message' : 'Working...'}
	return jsonify(answer), 200


if __name__ == '__main__':
	publicKey, privateKey = keysGeneration(2 ** 256)
	app.run(host='0.0.0.0', port=validatorPort)