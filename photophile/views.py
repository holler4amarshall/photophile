from flask import render_template

from photophile import app

from keys import *

def authenticate(): 
    """authenticate instagram credentials to get secret key"""
    import oauth2client.file
    import oauth2client.client_id
    import oauth2client.tools
    storage = oauth2client.file.Storage("credentials.dat")
    credentials = storage.get()
	

@app.route("/")
def get_index():
    return render_template("index.html")
    
@app.route("/login")
def get_login():
    return render_template("login.html")
    
@app.route("/create-account")
def get_create_account():
    return render_template("create_account.html")
    
@app.route("/search")
def get_search():
    return render_template("search.html")
    
@app.route('/search', methods=['POST'])
def submit_search():

    query = request.form['search'].strip()
    return query


    
    
    
    
    