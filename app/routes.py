from flask import render_template, jsonify, request
from app import app
from datetime import timedelta
from app.dataprocess import callTypeCounts, timeDiffs, watchDateCount,zipCodeTops
from app.predict import predict
import sys

@app.route('/')
def home():
    return render_template('index.html',
                           callTypeCounts=callTypeCounts,
                           timeDiffs=timeDiffs,
                           watchDateCount=watchDateCount,
                           timedelta=timedelta,
                           zipCodeTops=zipCodeTops)

@app.route('/predict', methods=['POST'])
def predict_dispatch():
    print('Hello world!', file=sys.stderr)
    return jsonify({'text': predict(request.form['latitude'],
                                    request.form['longitude'],
                                    request.form['time'])})

