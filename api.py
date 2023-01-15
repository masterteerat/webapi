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
        elif cmd == "user":
            ret = user()
        else:
            return jsonify(
		    result="an error has occured: command not found"
	        )

 
        
    return ret,201
	

def register():

    mid = request.form["mid"]
    sid = request.form["sid"]
    name = request.form["name"]
    try:
        sql = "INSERT INTO user (mid, sid, name) VALUES (%s, %s, %s)"
        val = (mid, sid, name)
        mycursor.execute(sql, val)
        mydb.commit()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print('register has responded')
        return jsonify(
		    result="process failed"
        )   
    
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

    
def user():

    sql = "select sid, name from user where mid =%s"
    mid = (request.form["mid"],)

    mycursor.execute(sql, mid)
    record = mycursor.fetchone()   
    print(record)
    print(record[0])
    print(record[1])

    return jsonify(
		result="process complete"
    )