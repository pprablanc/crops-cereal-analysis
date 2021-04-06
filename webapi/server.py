#!/usr/bin/env python3

from flask import render_template, jsonify
import connexion


app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')


# To put in view.py
@app.route("/")
def home():
    return "Home page"


@app.route("/dashboard/")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":

    app.run(port=5000, debug=True)
    # app.run(port=5000)
