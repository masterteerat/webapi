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
        elif cmd == "checkorder":
            ret = checkorder()    
        else:
            return jsonify(
		    result="an error has occured: command not found"
	        )

    print(ret)
        
    return ret,201
	

def register():

    status = "no"

    try:
        content = request.json
        mid = content["mid"]
        sid = content["sid"]
        name = content["name"]
        print(mid)
        print(sid)
        print(name)

        sql = "INSERT INTO user (mid, sid, name) VALUES (%s, %s, %s)"
        val = (mid, sid, name)
        mycursor.execute(sql, val)
        mydb.commit()
        status = "yes"
    except ValueError as er:
        print("Function register: value error")
  
          
    except TypeError as er:
        print("Function register: Type error")
       
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print('register has responded')
      
    
    
    return jsonify(
		    status=status
    )        
	
def order():

    content = request.json
    mid = content["mid"]
    name = content["name"]

    prodid0 = content["prodid0"]
    imgresid0 = content["imgresid0"]
    description0 = content["description0"]
    quantity0 = content["quantity0"]
    price0 = content["price0"]
    totalprice0 = content["totalprice0"]
    prodstatus0 = content["prodstatus0"]

    prodid1 = content["prodid1"]
    imgresid1 = content["imgresid1"]
    description1 = content["description1"]
    quantity1 = content["quantity1"]
    price1 = content["price1"]
    totalprice1 = content["totalprice1"]
    prodstatus1 = content["prodstatus1"]

    prodid2 = content["prodid2"]
    imgresid2 = content["imgresid2"]
    description2 = content["description2"]
    quantity2 = content["quantity2"]
    price2 = content["price2"]
    totalprice2 = content["totalprice2"]
    prodstatus2 = content["prodstatus2"]
    
    prodid3 = content["prodid3"]
    imgresid3 = content["imgresid3"]
    description3 = content["description3"]
    quantity3 = content["quantity3"]
    price3 = content["price3"]
    totalprice3 = content["totalprice3"]
    prodstatus3 = content["prodstatus3"]

    prodid4 = content["prodid4"]
    imgresid4 = content["imgresid4"]
    description4 = content["description4"]
    quantity4 = content["quantity4"]
    price4 = content["price4"]
    totalprice4 = content["totalprice4"]
    prodstatus4 = content["prodstatus4"]

    prodid5 = content["prodid5"]
    imgresid5 = content["imgresid5"]
    description5 = content["description5"]
    quantity5 = content["quantity5"]
    price5 = content["price5"]
    totalprice5 = content["totalprice5"]
    prodstatus5 = content["prodstatus5"]

    prodid6 = content["prodid6"]
    imgresid6 = content["imgresid6"]
    description6 = content["description6"]
    quantity6 = content["quantity6"]
    price6 = content["price6"]
    totalprice6 = content["totalprice6"]
    prodstatus6 = content["prodstatus6"]

    prodid7 = content["prodid7"]
    imgresid7 = content["imgresid7"]
    description7 = content["description7"]
    quantity7 = content["quantity7"]
    price7 = content["price7"]
    totalprice7 = content["totalprice7"]
    prodstatus7 = content["prodstatus7"]
    
    prodid8 = content["prodid8"]
    imgresid8 = content["imgresid8"]
    description8 = content["description8"]
    quantity8 = content["quantity8"]
    price8 = content["price8"]
    totalprice8 = content["totalprice8"]
    prodstatus8 = content["prodstatus8"]

    prodid9 = content["prodid9"]
    imgresid9 = content["imgresid9"]
    description9 = content["description9"]
    quantity9 = content["quantity9"]
    price9 = content["price9"]
    totalprice9 = content["totalprice9"]
    prodstatus9 = content["prodstatus9"]
    
    status = "yes"
    

    try:
         if quantity0 != "0":
             if insertorder(mid, name, prodid0, imgresid0, description0, quantity0, price0, totalprice0, prodstatus0) == False:
                 status = "no"
         if quantity1 != "0":
             if insertorder(mid, name, prodid1, imgresid1, description1, quantity1, price1, totalprice1, prodstatus1) == False:
                 status = "no"
         if quantity2 != "0":
             if insertorder(mid, name, prodid2, imgresid2, description2, quantity2, price2, totalprice2, prodstatus2) == False:
                 status = "no"
         if quantity3 != "0":
             if insertorder(mid, name, prodid3, imgresid3, description3, quantity3, price3, totalprice3, prodstatus3) == False:
                 status = "no"  
         if quantity4 != "0":
             if insertorder(mid, name, prodid4, imgresid4, description4, quantity4, price4, totalprice4, prodstatus4) == False:
                 status = "no"
         if quantity5 != "0":
             if insertorder(mid, name, prodid5, imgresid5, description5, quantity5, price5, totalprice5, prodstatus5) == False:
                 status = "no"
         if quantity6 != "0":
             if insertorder(mid, name, prodid6, imgresid6, description6, quantity6, price6, totalprice6, prodstatus6) == False:
                 status = "no"
         if quantity7 != "0":
             if insertorder(mid, name, prodid7, imgresid7, description7, quantity7, price7, totalprice7, prodstatus7) == False:
                 status = "no"
         if quantity8 != "0":
             if insertorder(mid, name, prodid8, imgresid8, description8, quantity8, price8, totalprice8, prodstatus8) == False:
                 status = "no"
         if quantity9 != "0":
             if insertorder(mid, name, prodid9, imgresid9, description9, quantity9, price9, totalprice9, prodstatus9) == False:
                 status = "no"                                                                                 
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
		    status=status
        )	


def insertorder(mid, name, prodid, imgresid, description, quantity, price, totalprice, prodstatus):

    try:
        sql = "INSERT INTO orderlist (mid, name, prodid, imgresid, description, quantity, price, totalprice, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (mid, name, prodid, imgresid, description, quantity, price, totalprice, prodstatus)
        mycursor.execute(sql, val)
        mydb.commit()
        

    except ValueError as er:
        print("Function user: value error")
        return False
    
    except TypeError as er:
        print("Function user: Type error")
        return False

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        print('user has responded')
        return False
    
    return True

def checkorder():

    content = request.json
    mid = content["mid"]
    id = content["id"]
    
    status = "no"
    recid = ""
    name = ""
    prodid = ""
    imgresid = ""
    description = ""
    quantity = ""
    price = ""
    totalprice = ""
    prodstatus = ""
    
    print(id)
    print(mid)

    try:
        
        sql = "select * from orderlist where mid = %s AND status != 'done' order by id limit " + id + " ,1"
        mycursor.execute(sql, (mid,))
        record = mycursor.fetchone()   
        
        recid = record[0]
        name = record[3]
        prodid = record[4]
        imgresid = record[5]
        description = record[6]
        quantity = record[7]
        price = record[8]
        totalprice = record[9]
        prodstatus = record[10]
    
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
            recid=recid,
            name=name,
            prodid=prodid,
            imgresid=imgresid,
            description=description,
            quantity=quantity,
            price=price,
            totalprice=totalprice,
            prodstatus=prodstatus      
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



    