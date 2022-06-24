from flask import Flask, render_template
import os, string, requests
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Configure application
app = Flask(__name__)
engine = create_engine("postgresql://kygwglvkegtnav:d6363097ee2eeb63362c5743c8aa96cc6be687cc513d7a4efbe831915e67a938@ec2-52-206-182-219.compute-1.amazonaws.com:5432/d4berc81tuqtf0")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    juegos = db.execute("SELECT * from juegos")
    for i in juegos:
        print(i)
    return render_template("index.html")
