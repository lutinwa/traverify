from flask_sqlalchemy import SQLAlchemy
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

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
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://soqvcujsnbhpne:01193a8bd24a94bbe9c9a4cdc0c47a1c5bbac7123cf3f8865725bedd274729a6@ec2-3-223-242-224.compute-1.amazonaws.com:5432/d2gb8n2jeakm30"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, name):
        self.name = name
class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sellername = db.Column(db.String(80), nullable=False)
    sellermobile = db.Column(db.String(80), nullable=False)
    sellertin = db.Column(db.String(80), nullable=False)
    sellervrn = db.Column(db.String(80), nullable=True)
    sellerserial = db.Column(db.String(80), nullable=False)
    selleruin = db.Column(db.String(120), nullable=False)
    sellertaxoffice = db.Column(db.String(80), nullable=False)
    customername = db.Column(db.String(80), nullable=True)
    customeridtype = db.Column(db.String(80), nullable=True)
    customerid = db.Column(db.String(80), nullable=True)
    customermobile = db.Column(db.String(80), nullable=True)
    receiptno = db.Column(db.String(80), nullable=False)
    znumber = db.Column(db.String(80), nullable=False)
    receiptdate = db.Column(db.String(80), nullable=False)
    receipttime = db.Column(db.String(80), nullable=False)
    receiptitem = db.Column(db.String(120), nullable=False)
    receiptamount = db.Column(db.String(120), nullable=False)
    amountexcltax = db.Column(db.String(120), nullable=False)
    taxamount = db.Column(db.String(120), nullable=False)
    verificationcode = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name



@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    return apology("ACCESS DENIED")

# create invoice
@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "POST":
        sn = request.form.get("sn")
        sm = request.form.get("sm")
        st = request.form.get("st")
        sv = request.form.get("sv")
        ss = request.form.get("ss")
        su = request.form.get("su")
        sto = request.form.get("sto")
        cn = request.form.get("cn")
        cit = request.form.get("cit")
        ci = request.form.get("ci")
        cm = request.form.get("cm")
        rn = request.form.get("rn")
        zn = request.form.get("zn")
        rd = request.form.get("rd")
        rt = request.form.get("rt")
        ri = request.form.get("ri")
        ra = request.form.get("ra")
        ext = request.form.get("ext")
        t = request.form.get("t")
        vx = request.form.get("vx")

        # db.execute("INSERT INTO invoice (sn,sm,st,sv,ss,su,sto,cn,cit,ci,cm,rn,zn,rd,rt,ri,ra,ext,t,vx) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", sn,sm,st,sv,ss,su,sto,cn,cit,ci,cm,rn,zn,rd,rt,ri,ra,ext,t,vx)
        new_invoice = Invoice(sn,sm,st,sv,ss,su,sto,cn,cit,ci,cm,rn,zn,rd,rt,ri,ra,ext,t,vx)
        db.session.add(new_invoice)
        db.session.commit()
        return redirect("/receipt/vx")
    return render_template("create.html")


@app.route("/receipt/<verification_id>")
def show(verification_id):
    try:
        invoice = Invoice.query.filter_by(verificationcode= verification_id).first()
        # row = db.execute("SELECT * FROM INVOICE WHERE vx = ?", verification_id)
        return render_template("receipt.html", row=invoice)
    except:
        return apology("Internal server error", 500)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        name = request.form.get("username")
        # rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        user = User.query.filter_by(username= name).first()

        # Ensure username exists and password is correct
        if not user or not check_password_hash(users.password, request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = user.id

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        # Ensure username and password are given
        username =  request.form.get("username")
        password = request.form.get("password")
        if not username and not password:
            return apology("must provide username and password", 403)

        # register user to database
        try:
            new_user = User(username, generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            # db.execute("INSERT INTO users (username, hash) VALUES (?,?)",name,generate_password_hash(password))
        except:
            return apology("username already taken")
        return redirect("/")


    return render_template("register.html")

