from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from mysql.connector.errors import Error
import mysql.connector

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
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
        content = request.json
        cmd = content["cmd"]

        if cmd == "register":
            ret = register()
        elif cmd == "order":
            ret = order()
        elif cmd == "checkuser":
            ret = checkuser()
        else:
            return jsonify(
		    result="an error has occured: command not found"
	        )

 
        
    return ret,201
	

def register():

    status = "no"

    try:
        content = request.json
        mid = content["mid"]
        sid = content["sid"]
        name = content["name"]

        sql = "INSERT INTO user (mid, sid, name) VALUES (%s, %s, %s)"
        val = (mid, sid, name)
        mycursor.execute(sql, val)
        mydb.commit()
        status = "yes"
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
    
    
    
    return jsonify(
		    status=status
    )        
	

def order():

    print('menu has responded')
    return jsonify(
		    result="process complete"
        
	)

    
def checkuser():

    content = request.json
    mid = content["mid"]
    status = "no"
    name = "none"
    sid = "none"

    print(mid)
    try:
        sql = "select sid, name from user where mid = %s ;"
        mycursor.execute(sql, (mid,))
        record = mycursor.fetchone()   
        
        sid = record[0]
        name = record[1]
        status = "yes"
        mydb.commit()

    except ValueError as er:
        print("Function user: value error")
        status = "no"
    
    except TypeError as er:
        print("Function user: Type error")
        status = "no"

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print('user has responded')
        status = "no"
    
    return jsonify(
		    status=status,
            name=name, 
            sid=sid 
        )   



    