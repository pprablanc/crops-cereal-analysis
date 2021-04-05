#!/usr/bin/env python3

from flask import Flask, render_template, jsonify
from functions import load_data

df = load_data()

app = Flask(__name__)

@app.route('/')
def titre():
    return "Accueil"

@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html")

@app.route('/api/cereal/')
def culture():
    cereal_trend = df.groupby(['time']).agg({'time': 'first', 'yield_mean': 'mean'})
    data = [[k, v] for k,v in cereal_trend['yield_mean'].items()]

    return jsonify({
        'status': 'ok',
        'data': data
    })


if __name__ == "__main__":
    app.run(port=5000, debug=True)
