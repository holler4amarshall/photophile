from flask import render_template

from photophile import app

@app.route("/")
def get_index():
    return render_template("index.html")
    
@app.route("/login")
def get_login():
    return render_template("login.html")
    
@app.route("/create-account")
def get_create_account():
    return render_template("create_account.html")

    
    
    
    
    