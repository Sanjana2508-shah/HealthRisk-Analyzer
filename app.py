from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from google import genai
import os

app = Flask(__name__)
app.secret_key = "healthrisk123"
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
db = SQLAlchemy(app)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    dob = db.Column(db.String(20))
    email = db.Column(db.String(100))
    glucose = db.Column(db.Float)
    haemoglobin = db.Column(db.Float)
    cholesterol = db.Column(db.Float)
    remarks = db.Column(db.String(500))

def predict(glucose, haemoglobin, cholesterol):

    prompt = f"""
    Glucose: {glucose}
    Haemoglobin: {haemoglobin}
    Cholesterol: {cholesterol}

    Give a short health remark in one sentence.
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"AI Service Busy: {str(e)}"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add-patient")
def add_patient_page():
    return render_template("add_patient.html")


@app.route("/patients")
def patients_page():

    patients = Patient.query.all()

    return render_template(
        "patients.html",
        patients=patients
    )

@app.route('/add', methods=['POST'])

def add():

    glucose = float(request.form['glucose'])
    haemoglobin = float(request.form['haemoglobin'])
    cholesterol = float(request.form['cholesterol'])

    remarks = predict(
        glucose,
        haemoglobin,
        cholesterol
    )

    patient = Patient(
        full_name=request.form['full_name'],
        dob=request.form['dob'],
        email=request.form['email'],
        glucose=glucose,
        haemoglobin=haemoglobin,
        cholesterol=cholesterol,
        remarks=remarks
    )

    db.session.add(patient)
    db.session.commit()

    flash("✅ New patient added successfully!")

    return redirect('/add-patient')

@app.route('/delete/<int:id>')

def delete(id):

    patient = Patient.query.get(id)

    db.session.delete(patient)

    db.session.commit()

    return redirect('/patients')
@app.route('/edit/<int:id>')

def edit(id):

    patient = Patient.query.get(id)

    return render_template(
        'edit.html',
        patient=patient
    )


@app.route('/update/<int:id>', methods=['POST'])

def update(id):

    patient = Patient.query.get(id)

    patient.full_name = request.form['full_name']
    patient.dob = request.form['dob']
    patient.email = request.form['email']

    patient.glucose = float(
        request.form['glucose']
    )

    patient.haemoglobin = float(
        request.form['haemoglobin']
    )

    patient.cholesterol = float(
        request.form['cholesterol']
    )

    patient.remarks = predict(
        patient.glucose,
        patient.haemoglobin,
        patient.cholesterol
    )

    db.session.commit()

    return redirect('/patients')


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)