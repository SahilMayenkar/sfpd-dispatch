from flask import render_template
from app import app
from datetime import timedelta
from .dataprocess import callTypeCounts, timeDiffs, watchDateCount

@app.route('/')
def home():
    return render_template('index.html',
                           callTypeCounts=callTypeCounts,
                           timeDiffs=timeDiffs,
                           watchDateCount=watchDateCount,
                           timedelta=timedelta)
