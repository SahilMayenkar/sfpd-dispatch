from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes

from rq import Queue
from worker import conn
from app.dataprocess import process_data

q = Queue(connection=conn)
q.enqueue(process_data)
