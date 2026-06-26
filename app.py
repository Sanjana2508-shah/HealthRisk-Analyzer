
from flask import Flask, render_template, request, redirect, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from dotenv import load_dotenv
load_dotenv()
from groq import Groq
import os

app = Flask(__name__)
app.secret_key = "healthrisk123"

client = Groq(api_key="GROQ_API_KEY")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
db = SQLAlchemy(app)


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    dob = db.Column(db.String(20))
    gender = db.Column(db.String(10))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    weight = db.Column(db.Float)       # kg
    height = db.Column(db.Float)       # cm
    bmi = db.Column(db.Float)
    bmr = db.Column(db.Float)
    bp_systolic = db.Column(db.Integer)
    bp_diastolic = db.Column(db.Integer)
    oxygen_level = db.Column(db.Float)  # SpO2 %
    glucose = db.Column(db.Float)
    haemoglobin = db.Column(db.Float)
    cholesterol = db.Column(db.Float)
    health_condition = db.Column(db.String(50))
    remarks = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return round(weight / (height_m ** 2), 2)


def calculate_bmr(weight, height_cm, age, gender):
    if gender.lower() == "male":
        return round(88.362 + (13.397 * weight) + (4.799 * height_cm) - (5.677 * age), 2)
    else:
        return round(447.593 + (9.247 * weight) + (3.098 * height_cm) - (4.330 * age), 2)


def get_age(dob_str):
    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
        today = date.today()
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    except:
        return 30


def get_health_condition(bmi, bp_sys, bp_dia, glucose, cholesterol, oxygen):
    risks = []
    if bmi < 18.5:
        risks.append("Underweight")
    elif bmi >= 30:
        risks.append("Obese")
    elif bmi >= 25:
        risks.append("Overweight")

    if bp_sys >= 140 or bp_dia >= 90:
        risks.append("Hypertension")
    elif bp_sys >= 130 or bp_dia >= 80:
        risks.append("Pre-Hypertension")

    if glucose >= 126:
        risks.append("Diabetic Risk")
    elif glucose >= 100:
        risks.append("Pre-Diabetic")

    if cholesterol >= 240:
        risks.append("High Cholesterol")

    if oxygen < 95:
        risks.append("Low Oxygen")

    if not risks:
        return "Healthy"
    return ", ".join(risks)


def predict(patient_data):
    prompt = f"""
You are a clinical health advisor. Based on the following patient vitals, give a concise professional health remark in 2-3 sentences.

Patient: {patient_data['name']}, Age: {patient_data['age']}, Gender: {patient_data['gender']}
BMI: {patient_data['bmi']} | BMR: {patient_data['bmr']} kcal/day
Blood Pressure: {patient_data['bp_sys']}/{patient_data['bp_dia']} mmHg
Oxygen Level: {patient_data['oxygen']}%
Glucose: {patient_data['glucose']} mg/dL
Haemoglobin: {patient_data['haemoglobin']} g/dL
Cholesterol: {patient_data['cholesterol']} mg/dL
Condition: {patient_data['condition']}
"""
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"AI Service unavailable: {str(e)}"


@app.route("/")
def home():
    total = Patient.query.count()
    today_str = date.today().strftime("%Y-%m-%d")
    today_count = Patient.query.filter(
        db.func.date(Patient.created_at) == today_str
    ).count()

    healthy = Patient.query.filter(Patient.health_condition == "Healthy").count()
    at_risk = total - healthy

    recent = Patient.query.order_by(Patient.created_at.desc()).limit(5).all()

    return render_template("home.html",
                           total=total,
                           today_count=today_count,
                           healthy=healthy,
                           at_risk=at_risk,
                           recent=recent)


@app.route("/add-patient")
def add_patient_page():
    return render_template("add_patient.html")


@app.route("/patients")
def patients_page():
    search = request.args.get("search", "")
    filter_condition = request.args.get("condition", "")

    query = Patient.query
    if search:
        query = query.filter(Patient.full_name.ilike(f"%{search}%"))
    if filter_condition:
        query = query.filter(Patient.health_condition.ilike(f"%{filter_condition}%"))

    patients = query.order_by(Patient.created_at.desc()).all()
    return render_template("patients.html", patients=patients, search=search, filter_condition=filter_condition)


@app.route('/add', methods=['POST'])
def add():
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    glucose = float(request.form['glucose'])
    haemoglobin = float(request.form['haemoglobin'])
    cholesterol = float(request.form['cholesterol'])
    bp_sys = int(request.form['bp_systolic'])
    bp_dia = int(request.form['bp_diastolic'])
    oxygen = float(request.form['oxygen_level'])
    dob = request.form['dob']
    gender = request.form['gender']
    age = get_age(dob)

    bmi = calculate_bmi(weight, height)
    bmr = calculate_bmr(weight, height, age, gender)
    condition = get_health_condition(bmi, bp_sys, bp_dia, glucose, cholesterol, oxygen)

    patient_data = {
        'name': request.form['full_name'],
        'age': age,
        'gender': gender,
        'weight': weight,
        'height': height,
        'bmi': bmi,
        'bmr': bmr,
        'bp_sys': bp_sys,
        'bp_dia': bp_dia,
        'oxygen': oxygen,
        'glucose': glucose,
        'haemoglobin': haemoglobin,
        'cholesterol': cholesterol,
        'condition': condition
    }

    remarks = predict(patient_data)

    patient = Patient(
        full_name=request.form['full_name'],
        dob=dob,
        gender=gender,
        email=request.form['email'],
        phone=request.form.get('phone', ''),
        weight=weight,
        height=height,
        bmi=bmi,
        bmr=bmr,
        bp_systolic=bp_sys,
        bp_diastolic=bp_dia,
        oxygen_level=oxygen,
        glucose=glucose,
        haemoglobin=haemoglobin,
        cholesterol=cholesterol,
        health_condition=condition,
        remarks=remarks
    )

    db.session.add(patient)
    db.session.commit()

    flash(f"SUCCESS|{remarks}|{condition}|{bmi}|{bmr}")
    return redirect('/add-patient')


@app.route('/delete/<int:id>')
def delete(id):
    patient = Patient.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    flash("Patient record deleted.")
    return redirect('/patients')


@app.route('/edit/<int:id>')
def edit(id):
    patient = Patient.query.get_or_404(id)
    return render_template('edit.html', patient=patient)


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    patient = Patient.query.get_or_404(id)
    patient.full_name = request.form['full_name']
    patient.dob = request.form['dob']
    patient.gender = request.form['gender']
    patient.email = request.form['email']
    patient.phone = request.form.get('phone', '')
    patient.weight = float(request.form['weight'])
    patient.height = float(request.form['height'])
    patient.glucose = float(request.form['glucose'])
    patient.haemoglobin = float(request.form['haemoglobin'])
    patient.cholesterol = float(request.form['cholesterol'])
    patient.bp_systolic = int(request.form['bp_systolic'])
    patient.bp_diastolic = int(request.form['bp_diastolic'])
    patient.oxygen_level = float(request.form['oxygen_level'])

    age = get_age(patient.dob)
    patient.bmi = calculate_bmi(patient.weight, patient.height)
    patient.bmr = calculate_bmr(patient.weight, patient.height, age, patient.gender)
    patient.health_condition = get_health_condition(
        patient.bmi, patient.bp_systolic, patient.bp_diastolic,
        patient.glucose, patient.cholesterol, patient.oxygen_level
    )

    patient_data = {
        'name': patient.full_name, 'age': age, 'gender': patient.gender,
        'weight': patient.weight, 'height': patient.height,
        'bmi': patient.bmi, 'bmr': patient.bmr,
        'bp_sys': patient.bp_systolic, 'bp_dia': patient.bp_diastolic,
        'oxygen': patient.oxygen_level, 'glucose': patient.glucose,
        'haemoglobin': patient.haemoglobin, 'cholesterol': patient.cholesterol,
        'condition': patient.health_condition
    }
    patient.remarks = predict(patient_data)

    db.session.commit()
    flash("Patient updated successfully!")
    return redirect('/patients')


@app.route('/patient/<int:id>')
def patient_detail(id):
    patient = Patient.query.get_or_404(id)
    return render_template('patient_detail.html', patient=patient)


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)