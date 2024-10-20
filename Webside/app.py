from flask import Flask, render_template, request, jsonify
import pickle
import joblib
import os
import pandas as pd
import numpy as np

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=4000)
