from flask_sqlalchemy import SQLAlchemy
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

# Configure application
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
# db = SQL("sqlite:///tra.db")
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:kh5dEgWmPY75DLIdFvm9@containers-us-west-60.railway.app:7880/railway"
db = SQLAlchemy(app)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/27E1F429225")
def show():
    return render_template("27E1F429225.html")
def four("/DEC4O0994"):
    return render_template("DEC4O0994.html")
@app.route("/9E6481231")
def three():
    return render_template("9E6481231.html")

@app.route("/4D6J01924")
def index():
    return render_template("4D6J01924.html")

@app.route("/D6E73132")
def hi():
    return render_template("D6E73132.html")
    
@app.route("/7F968235623")
def two():
    return render_template("7F968235623.html")