import os
import MySQLdb
import smtplib
import random
import string
from datetime import datetime
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash, send_file
from database import db_connect,inc_reg,admin_loginact,ins_loginact,cust_reg,cust_login,upload_act,view1,vtcact2,vp1,acart2,vc1,purchase2,vq1
from database import db_connect,req1,accept1,mo1,review2,status1
import io
import json

# def db_connect():
#     _conn = MySQLdb.connect(host="localhost", user="root",
#                             passwd="root", db="assigndb")
#     c = _conn.cursor()

#     return c, _conn


app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def FUN_root():
    return render_template("index.html")



@app.route("/owner.html")
def owner():
    return render_template("owner.html")

@app.route("/ohome.html")
def ohome():
    return render_template("ohome.html")

@app.route("/chome.html")
def chome():
    return render_template("chome.html")

@app.route("/about.html")
def about():
    return render_template("about.html")
@app.route("/contact.html")
def contact():
    return render_template("contact.html")


@app.route("/mhome.html")
def mhome():
    return render_template("mhome.html")


@app.route("/oreg.html")
def oreg():
    return render_template("oreg.html")

@app.route("/cust.html")
def cust():
    return render_template("cust.html")

@app.route("/creg.html")
def creg():
    return render_template("creg.html")

@app.route("/ml.html")
def ml():
    return render_template("ml.html")
 
@app.route("/index.html")
def Logout():
    return render_template("index.html") 

@app.route("/upload.html")
def upload():
    return render_template("upload.html") 

@app.route("/view.html")
def view():
    if 'username' not in session:
        flash("You need to log in first!", "error")
        return redirect(url_for("cust"))  # Redirect to login page
    
    seller = session['username']
    data = view1(seller)
    print(data)
    return render_template("view.html", data=data)

@app.route("/vp.html")
def vp():
    seller = session['username']
    data = vp1()
    print(data)
    return render_template("vp.html",data=data) 

@app.route("/vc.html")
def vc():
    customer = session['username']
    data = vc1(customer)
    print(data)
    return render_template("vc.html",data=data) 

@app.route("/req.html")
def req():
    owner = session['username']
    data = req1(owner)
    print(data)
    return render_template("req.html",data=data) 


@app.route("/status.html")
def status():
    owner = session['username']
    data = status1(owner)
    print(data)
    return render_template("status.html",data=data) 

@app.route("/mo.html")
def mo():
    customer = session['username']
    data = mo1(customer)
    print(data)
    return render_template("mo.html",data=data) 


@app.route("/vtcact1", methods = ['GET','POST'])
def vtcact1():
    name = request.args.get('name')
    owner = request.args.get('owner')
    status = vtcact2(name,owner)
    if status == 1:
        return render_template("view.html",m1="sucess")
    else:
       return render_template("view.html",m1="failed")




@app.route("/acart", methods = ['GET','POST'])
def acart():
    ptype = request.args.get('ptype')
    name = request.args.get('name')
    quantity = request.args.get('quantity')
    price = request.args.get('price')
    image = request.args.get('image')
    owner = request.args.get('owner')
    return render_template("acart.html",m1="sucess",ptype=ptype,name=name,quantity=quantity,price=price,image=image,owner=owner)

@app.route("/purchase", methods = ['GET','POST'])
def purchase():
    ptype = request.args.get('ptype')
    name = request.args.get('name')
    quan = request.args.get('quan')
    tc = request.args.get('tc')
    image = request.args.get('image')
    address = request.args.get('address')
    owner = request.args.get('owner')
    customer = request.args.get('customer')
    return render_template("purchase.html",m1="sucess",ptype=ptype,name=name,quan=quan,tc=tc,image=image,owner=owner,address=address,customer=customer)
   
@app.route("/acart1", methods=['GET', 'POST'])
def acart1():
    ptype = request.form['ptype']
    name = request.form['name']
    quan = request.form['quan']
    address = request.form['address']
    quantity = request.form['quantity']
    price = request.form['price']
    image = request.form['image']
    owner = request.form['owner']
    customer = session['username']
    date = request.form['date']  # Capture date from form

    # Convert price and quantity to integers for calculation
    p = int(price)
    q = int(quan)
    tc = p * q  # Total Cost

    # Call the function to insert data into the database (assuming acart2 accepts 'date')
    status = acart2(ptype, name, quan, price, tc, image, owner, customer, address, date)

    if status == 1:
        return render_template("chome.html", m1="success")
    else:
        return render_template("vp.html", m1="failed")

@app.route("/purchase1", methods = ['GET','POST'])
def purchase1():
    ptype = request.form['ptype']
    name = request.form['name']
    quan = request.form['quan']
    address = request.form['address']
    tc = request.form['tc']
    image = request.form['image']
    owner = request.form['owner']
    customer = session['username']
    q = int(quan)
    data = vq1(ptype,name,owner)
    print(data)
    quant = data[0][0]
    print(quant)
    q1 = int(quant)
    tq = q1-q
    status = purchase2(ptype,name,quan,tc,image,owner,customer,address,tq)
    if status == 1:
        return render_template("chome.html",m1="sucess")
    else:
       return render_template("vc.html",m1="failed")


@app.route("/accept", methods = ['GET','POST'])
def accept():
    ptype = request.args.get('ptype')
    name = request.args.get('name')
    owner = request.args.get('owner')
    customer = request.args.get('customer')
    status =  accept1(ptype,name,owner,customer) 
    if status == 1:
        return render_template("ohome.html",m1="sucess")
    else:
        return render_template("ohome.html",m1="failed")

@app.route("/review", methods = ['GET','POST'])
def review():
    ptype = request.args.get('ptype')
    name = request.args.get('name')
    owner = request.args.get('owner')
    customer = request.args.get('customer')
    return render_template("review.html",m1="sucess",ptype=ptype,name=name,owner=owner,customer=customer)

@app.route("/review1", methods = ['GET','POST'])
def review1():
    ptype = request.form['ptype']
    name = request.form['name']
    owner = request.form['owner']
    rating = request.form['rating']
    customer = session['username']
    
    status = review2(ptype,name,owner,customer,rating)
    if status == 1:
        return render_template("chome.html",m1="sucess")
    else:
       return render_template("review.html",m1="failed")
# -------------------------------Registration-----------------------------------------------------------------    



@app.route("/inceregact", methods = ['GET','POST'])
def inceregact():
   if request.method == 'POST':    
      
      status = inc_reg(request.form['username'],request.form['password'],request.form['email'],request.form['mobile'],request.form['address'])
      
      if status == 1:
       return render_template("owner.html",m1="sucess")
      else:
       return render_template("oreg.html",m1="failed")

@app.route("/cregact", methods = ['GET','POST'])
def cregact():
   if request.method == 'POST':    
      
      status = cust_reg(request.form['username'],request.form['password'],request.form['email'],request.form['mobile'],request.form['address'])
      
      if status == 1:
       return render_template("cust.html",m1="sucess")
      else:
       return render_template("creg.html",m1="failed")


@app.route("/uploadact", methods = ['GET','POST'])
def uploadact():
   if request.method == 'POST':    
      
      status = upload_act(request.form['ptype'],request.form['name'],request.form['quantity'],request.form['price'],request.form['image'],request.form['time'],request.form['address'])
      
      if status == 1:
       return render_template("upload.html",m1="sucess")
      else:
       return render_template("upload.html",m1="failed")

# #-------------------------------ADD_END---------------------------------------------------------------------------
# # -------------------------------Loginact-----------------------------------------------------------------
@app.route("/adminlogact", methods=['GET', 'POST'])       
def adminlogact():
    if request.method == 'POST':
        status = admin_loginact(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("mhome.html", m1="sucess")
        else:
            return render_template("ml.html", m1="Login Failed")






@app.route("/inslogin", methods=['GET', 'POST'])       
def inslogin():
    if request.method == 'POST':
        status = ins_loginact(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("ohome.html", m1="sucess")
        else:
            return render_template("owner.html", m1="Login Failed")
        
@app.route("/cact", methods=['GET', 'POST'])       
def cact():
    if request.method == 'POST':
        status = cust_login(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("chome.html", m1="sucess")  # ✅ Correct
        else:
            return render_template("cust.html", m1="Login Failed")


# # -------------------------------Loginact End-----------------------------------------------------------------


   
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
