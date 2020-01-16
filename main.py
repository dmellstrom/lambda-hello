from flask import Flask
from datetime import datetime
from zappa.asynchronous import task
import random
from time import sleep

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/time")
def time():
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  nap(current_time)
  return current_time

@task
def nap(start):
  print("[SILLY] Nip man Crinkle is going to sleep at " + start)
  delay = random.random() * 20 + 60
  sleep(delay)
  print("[SILLY] Nip man Crinkle woke up!")