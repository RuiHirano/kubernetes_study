from flask import Flask, jsonify
from flask_cors import CORS
import os
#from command import Command
import sys

# Flask App設定
path = os.getcwd()
app = Flask(__name__)
CORS(app) #Cross Origin Resource Sharing

@app.route("/test", methods=['GET'])
def test():
    return jsonify("success"), 200

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
