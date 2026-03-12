import sqlite3
import hashlib
import datetime
import MySQLdb
from flask import session
from flask import Flask, request, send_file
import io
import plotly.graph_objs as go
def db_connect():
    _conn = MySQLdb.connect(host="localhost", user="root",
                            passwd="kuram@6281",port=3366, db="farmarbook")
    c = _conn.cursor()

    return c, _conn



# -------------------------------Registration-----------------------------------------------------------------


    


def inc_reg(username,password,email,mobile,address):
    try:
        c, conn = db_connect()
        print(username,password,email,mobile,address)
        id="0"
        status = "pending"
        j = c.execute("insert into owner (id,username,password,email,mobile,address) values ('"+id +
                      "','"+username+"','"+password+"','"+email+"','"+mobile+"','"+address+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    
def cust_reg(username,password,email,mobile,address):
    try:
        c, conn = db_connect()
        print(username,password,email,mobile,address)
        id="0"
        status = "pending"
        j = c.execute("insert into customer (id,username,password,email,mobile,address) values ('"+id +
                      "','"+username+"','"+password+"','"+email+"','"+mobile+"','"+address+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))


def upload_act(ptype,name,quantity,price,image,time,address):
    try:
        c, conn = db_connect()
        print(ptype,name,quantity,price,image,time,address)
        id="0"
        status = "pending"
        owner = session['username']
        j = c.execute("insert into upload (id,ptype,name,quantity,price,image,time,address,owner) values ('"+id +
                      "','"+ptype+"','"+name+"','"+quantity+"','"+price+"','"+image+"','"+time+"','"+address+"','"+owner+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))

def acart2(ptype,name,quan,price,tc,image,owner,customer,address,date):
    try:
        c, conn = db_connect()
        print(ptype,name,quan,price,tc,image,owner,customer,address,date)
        id="0"
        status = "pending"
        j = c.execute("insert into cart (id,ptype,name,quan,price,tc,image,owner,customer,address,date) values ('"+id +
                      "','"+ptype+"','"+name+"','"+quan+"','"+price+"','"+str(tc)+"','"+image+"','"+owner+"','"+customer+"','"+address+"','"+date+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))


def purchase2(ptype,name,quan,tc,image,owner,customer,address,tq):
    try:
        c, conn = db_connect()
        print(ptype,name,quan,tc,image,owner,customer,address,tq)
        id="0"
        status = "pending"
        j = c.execute("insert into purchase (id,ptype,name,quan,tc,image,owner,customer,address,rating,status,status1) values ('"+id +
                      "','"+ptype+"','"+name+"','"+quan+"','"+str(tc)+"','"+image+"','"+owner+"','"+customer+"','"+address+"','"+status+"','"+status+"','"+status+"')")

        k = c.execute("update upload set quantity='"+str(tq)+"' where ptype='"+ptype+"' and name='"+name+"' and owner='"+owner+"'  ")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))

def accept1(ptype,name,owner,customer):
    try:
        c, conn = db_connect()
        print(ptype,name,owner,customer)
        id="0"
        status = "pending"

        j = c.execute("update purchase set status='accepted' where ptype='"+ptype+"' and name='"+name+"' and owner='"+owner+"' and customer='"+customer+"'  ")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
#--------------------------------ml code
def review2(ptype,name,owner,customer,rating):
    try:
        c, conn = db_connect()
        print(ptype,name,owner,customer,rating)
        id="0"
        status1 = "positive"

        j = c.execute("update purchase set rating='"+rating+"',status1='"+status1+"' where ptype='"+ptype+"' and name='"+name+"' and owner='"+owner+"' and customer='"+customer+"'  ")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))


# # -------------------------------Registration End-----------------------------------------------------------------
# # -------------------------------Loginact Start-----------------------------------------------------------------

def admin_loginact(username, password):
    try:
        c, conn = db_connect()
        j = c.execute("select * from ml where username='" +
                      username+"' and password='"+password+"'")
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))



def ins_loginact(username, password):
    try:
        c, conn = db_connect()
        
        j = c.execute("select * from owner where username='" +
                      username+"' and password='"+password+"' "  )
        c.fetchall()
        
        conn.close()
        return j
    except Exception as e:
        return(str(e))


def cust_login(username, password):
    try:
        c, conn = db_connect()
        
        j = c.execute("select * from customer where username='" +
                      username+"' and password='"+password+"' "  )
        c.fetchall()
        
        conn.close()
        return j
    except Exception as e:
        return(str(e))

def view1(seller):
    c, conn = db_connect()
    c.execute("select * from upload where owner='"+seller+"' ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def vp1():
    c, conn = db_connect()
    c.execute("select * from upload")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def vc1(customer):
    c, conn = db_connect()
    c.execute("select * from cart where customer='"+customer+"'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def req1(owner):
    c, conn = db_connect()
    
    # SQL query to get all columns from 'purchase', 'date' from 'cart', and 'mobile' from 'customer'
    query = """
    SELECT p.*, c.date, cu.mobile
    FROM purchase p
    JOIN cart c ON p.ptype = c.ptype AND p.name = c.name 
               AND p.owner = c.owner AND p.customer = c.customer
    JOIN customer cu ON p.customer = cu.username
    WHERE p.owner = %s
    """
    
    c.execute(query, (owner,))
    result = c.fetchall()
    
    conn.close()
    return result

def status1(owner):
    c, conn = db_connect()
    c.execute("select * from purchase where owner='"+owner+"'")
    result = c.fetchall()
    conn.close()
    print("result")
    return result

def mo1(customer):
    c, conn = db_connect()
    
    # SQL query to fetch all columns from 'purchase', 'mobile' from 'owner', and 'address' from 'upload'
    query = """
    SELECT p.*, o.mobile, u.address
    FROM purchase p
    JOIN owner o ON p.owner = o.username
    JOIN upload u ON p.name = u.name  -- Assuming 'name' is the common key
    WHERE p.customer = %s
    """
    
    c.execute(query, (customer,))
    result = c.fetchall()
    
    conn.close()
    return result


def vq1(ptype,name,owner):
    c, conn = db_connect()
    c.execute("select quantity from upload where ptype='"+ptype+"' and name='"+name+"' and owner='"+owner+"'  ")
    result = c.fetchall()
    conn.close()
    print("result")
    print(result)
    return result

def vtcact2(name, owner):
    try:
        c, conn = db_connect()
        print(name, owner)
        j = c.execute("Delete from upload where name='"+name+"' and owner='"+owner+"' "  )
        conn.commit()
        
        conn.close()
        return j
    except Exception as e:
        return(str(e))

if __name__ == "__main__":
    print(db_connect())
