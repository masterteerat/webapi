from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
# Enable CORS
CORS(app)

mydb = mysql.connector.connect(
  host="192.168.1.111",
  user="root",
  password="mYsql01",
  database="schooldb"
)

mycursor = mydb.cursor()

@app.route("/api", methods=["POST"])
def api():
    ret = jsonify
    if request.method == "POST": 
        cmd = request.form["cmd"]

        if cmd == "register":
            ret = register()
        elif cmd == "order":
            ret = order()
        else:
            return jsonify(
		    result="an error has occured"
	        )

 
        
    return ret,201
	

def register():

    mid = request.form["mid"]
    sid = request.form["sid"]
    name = request.form["name"]
    
    sql = "INSERT INTO user (mid, sid, name) VALUES (%s, %s, %s)"
    val = (mid, sid, name)
    mycursor.execute(sql, val)
    mydb.commit()
    
    print(mid)
    print(sid)
    print(name)
    print('register has responded')
    
    return jsonify(
		    result="process complete"
    )        
	

def order():

    print('menu has responded')
    return jsonify(
		    result="process complete"
	)

    
