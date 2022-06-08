from flask import Flask, render_template, jsonify, send_from_directory, request
import json
import pandas as pd
import numpy as np
import os

from sympy import content 

#init app and class
app = Flask(__name__)


# Route to render index.html template
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

@app.route("/team")
def about():
    # Return template and data
    return render_template("team.html")

#route to Tableau
@app.route("/tableau")
def tableau():
    # Return template and data
    return render_template("tableauviz.html")
    #route to Tableau

@app.route("/tableau2")
def tableau2():
    # Return template and data
    return render_template("tableauviz2.html")
    
@app.route("/reference")
def references():
    # Return template and data
    return render_template("worksCited.html")

@app.route("/data")
def data():
    # Return template and data
    return render_template("table.html")

@app.route("/model")
def model():
    # Return template and data
    return render_template("model.html")

@app.route("/writeup")
def writeUp():
    # Return template and data
    return render_template("MLWriteup.html")




###########################################################################
#main
if __name__ == "__main__":
    app.run(debug=True)