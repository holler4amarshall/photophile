from flask import render_template

from photophile import app

@app.route("/")
def get_index():
    return render_template("index.html")

    
    
    
    
    