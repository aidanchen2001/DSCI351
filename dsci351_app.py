from flask import FlaskForm, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, BooleanField, SubmitField, RadioField

app = FlaskForm(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Lifeis2good!@localhost/colleges.info'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialize database
db = SQLAlchemy(app)

class Colleges(db.Model):
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

# https://www.youtube.com/watch?v=I2dJuNwlIH0
# https://www.youtube.com/watch?v=-O9NMdvWmE8

class Form(FlaskForm):
    maxTuition = IntegerField('Tuition Preference')
    SATScore = RadioField('SAT Score', choices=[])
    size = BooleanField('Size Preference', choices=[])
    region = SelectField('Region Preference', choices=['U.S. Service','New England','Mid West','Great Lakes','Plains','Southeast','Southwest','Rocky Mountains','Far West'])
    submit = SubmitField('Submit')

# StringField: A text input.
# TextAreaField: A text area field.
# IntegerField: A field for integers.
# BooleanField: A checkbox field.
# RadioField: A field for displaying a list of radio buttons for the user to choose from.

@app.route('/', methods=['GET','POST'])
def index():
    form = Form()  # instantiate form
    if request.method == 'POST':
        colleges = Colleges.query.filter_by(Colleges.region == form.region.data).all()  # list of college objects
        # colleges = db.execute("SELECT * FROM Colleges.info WHERE region=")

    return render_template('index.html', form=form)
    
