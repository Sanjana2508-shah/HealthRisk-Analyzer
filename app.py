<<<<<<< HEAD
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from google import genai

app = Flask(__name__)
client = genai.Client(api_key="AQ.Ab8RN6IgOlEmgnAaz5FtUFYnKjGEAnPu46Js2QPlba-SiR-F8g")

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

@app.route('/')

def index():

    patients = Patient.query.all()

    return render_template(
        'index.html',
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

    return redirect('/')

@app.route('/delete/<int:id>')

def delete(id):

    patient = Patient.query.get(id)

    db.session.delete(patient)

    db.session.commit()

    return redirect('/')
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

    return redirect('/')


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from google import genai

app = Flask(__name__)
client = genai.Client(api_key="YOUR_API_KEY")

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

@app.route('/')

def index():

    patients = Patient.query.all()

    return render_template(
        'index.html',
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

    return redirect('/')

@app.route('/delete/<int:id>')

def delete(id):

    patient = Patient.query.get(id)

    db.session.delete(patient)

    db.session.commit()

    return redirect('/')
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

    return redirect('/')


with app.app_context():
    db.create_all()

app.run(debug=True)
>>>>>>> 3833dddf645d33e8dd5de9b2cadb4bb67b2a7db4
