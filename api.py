from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from mysql.connector.errors import Error
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

    try:
        mid = request.form["mid"]
        sid = request.form["sid"]
        name = request.form["name"]
        sql = "INSERT INTO user (mid, sid, name) VALUES (%s, %s, %s)"
        val = (mid, sid, name)
        mycursor.execute(sql, val)
        mydb.commit()
    except ValueError as er:
        print("Function register: value error")
        return jsonify(
		    result="process failed"
        )   
    except TypeError as er:
        print("Function register: Type error")
        return jsonify(
            result="process failed"
        )
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

    mid = (request.form["mid"],)

    try:
        sql = "select sid, name from user where mid =%s"
        mycursor.execute(sql, mid)
        record = mycursor.fetchone()   
        print(record)
        print(record[0])
        print(record[1])
    except ValueError as er:
        print("Function user: value error")
        return jsonify(
		    result="process failed"
        )   
    except TypeError as er:
        print("Function user: Type error")
        return jsonify(
            result="process failed"
        )

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print('user has responded')
        return jsonify(
		    result="process failed"
        )   
    return jsonify(
		    result="process complete"
        )   