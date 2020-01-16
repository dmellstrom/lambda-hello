from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/time")
def time():
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print("time() called at " + current_time)
  return current_time