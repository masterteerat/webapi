from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS
CORS(app)

@app.route("/register", methods=["POST"])
def register():

    if request.method == "POST":    		
        name = request.form["name"]
        sid = request.form["sid"]
        mid = request.form["mid"]

        result = name + ":" + sid + ":" + mid
        print(result)
        
    return jsonify(
		prediction=result
	),201
