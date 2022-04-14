from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Lifeis2good!@localhost/colleges.info'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialize database
db = SQLAlchemy(app)

class colleges(db.Model):
    unitID = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String)
    state = db.Column(db.String)
    level = db.Column(db.String)
    region = db.Column(db.String)
    category = db.Column(db.Integer)
    sizeSetting = db.Column(db.Integer)
    sizeCategory = db.Column(db.Integer)
    basic = db.Column(db.Integer)
    undergradProfile = db.Column(db.Integer)
    enrollmentProfile = db.Column(db.Integer)
    priceInState = db.Column(db.Integer)
    priceOutState = db.Column(db.Integer)
    admitRate = db.Column(db.Integer)
    admitYield = db.Column(db.Integer)
    enrollmentTotal = db.Column(db.Integer)
    gradRate = db.Column(db.Integer)
    finaidRate = db.Column(db.Integer)
    fedloanRate = db.Column(db.Integer)
    fedloanAvg = db.Column(db.Integer)
    applicantTotal = db.Column(db.Integer)
    admitTotal = db.Column(db.Integer)
    enrollTotal = db.Column(db.Integer)
    SAT_RW_25 = db.Column(db.Integer)
    SAT_RW_75 = db.Column(db.Integer)
    SAT_M_25 = db.Column(db.Integer)
    SAT_M_75 = db.Column(db.Integer)
    ACT_25 = db.Column(db.Integer)
    ACT_75 = db.Column(db.Integer)
    ACT_E_25 = db.Column(db.Integer)
    ACT_E_75 = db.Column(db.Integer)
    ACT_M_25 = db.Column(db.Integer)
    ACT_M_75 = db.Column(db.Integer)
    submitSATRate = db.Column(db.Integer)
    submitACTRate = db.Column(db.Integer)
    ratio = db.Column(db.Integer)

# class TuitionForm(FlaskForm):
    # maxTuition = IntegerField("")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/')
def query():
    