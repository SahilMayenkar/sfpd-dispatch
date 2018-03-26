from flask import render_template, jsonify, request
from app import app
from datetime import timedelta
from app.dataprocess import callTypeCounts, timeDiffs, watchDateCount
from app.predict import predict

@app.route('/')
def home():
    return render_template('index.html',
                           callTypeCounts=callTypeCounts,
                           timeDiffs=timeDiffs,
                           watchDateCount=watchDateCount,
                           timedelta=timedelta)

@app.route('/predict', methods=['POST'])
def predict_dispatch():
    return jsonify({'text': predict(request.form['latitude'],
                                    request.form['longitude'],
                                    request.form['time'])})

