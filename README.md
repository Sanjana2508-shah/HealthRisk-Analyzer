<<<<<<< HEAD
<<<<<<< HEAD
# 🏥 HealthRisk Analyzer v2.0

AI-powered Healthcare Staff Portal built with **Flask**, **SQLite**, and **Groq AI (Llama 3.3 70B)**.

Designed for **medical staff** to manage patient records, compute health metrics automatically, and receive AI-generated clinical remarks.

---

## ✨ Features

- 🧑‍⚕️ Add, View, Edit, Delete patient records
- 📊 Auto-calculated **BMI** and **BMR**
- 🩺 Health condition auto-detection (Hypertension, Diabetic Risk, Obese, etc.)
- 🤖 AI-generated clinical remarks powered by **Groq (Llama 3.3 70B)**
- 🔍 Search and filter patients by name or condition
- 📋 Dashboard with real-time stats

---

## 📁 Project Structure

```
HealthRisk-Analyzer/
├── app.py
├── requirements.txt
├── README.md
├── Procfile
├── .env               ← API key (do NOT push to GitHub)
└── templates/
    ├── base.html
    ├── home.html
    ├── add_patient.html
    ├── patients.html
    ├── patient_detail.html
    └── edit.html
```

---

## ⚙️ Setup

```bash
# 1. Clone
git clone https://github.com/Sanjana2508-shah/HealthRisk-Analyzer.git
cd HealthRisk-Analyzer

# 2. Install
pip install -r requirements.txt

# 3. Create .env file and add your Groq API key
# Get free key from: https://console.groq.com
echo "GROQ_API_KEY=your_groq_api_key_here" > .env

# 4. Run
python app.py

# 5. Open
http://127.0.0.1:5000
```

---

## 📊 Health Parameters Tracked

| Parameter | Normal Range | Unit |
|---|---|---|
| BMI | 18.5 – 24.9 | kg/m² |
| BMR | Calculated | kcal/day |
| Blood Pressure | < 120/80 | mmHg |
| SpO₂ | 95 – 100% | % |
| Fasting Glucose | 70 – 99 | mg/dL |
| Haemoglobin | 12 – 17 | g/dL |
| Cholesterol | < 200 | mg/dL |

---

## 🎯 Health Conditions Auto-Detected

- ✅ Healthy
- ⚠ Underweight / Overweight / Obese
- 🔴 Hypertension / Pre-Hypertension
- 🔴 Diabetic Risk / Pre-Diabetic
- 🔴 High Cholesterol
- 🔴 Low Oxygen

---

## 🛠️ Technologies

- Python, Flask, SQLite
- Bootstrap (via CDN)
- Groq API — Llama 3.3 70B
- Gunicorn (for deployment)

---

## 👩‍💻 Author

**Sanjana Kumari Shah**
B.Tech Information Technology (2025)
=======
<<<<<<< HEAD
=======
>>>>>>> 627989d956bc58cb5888bb7aa878bb64e9dbd619
AI Health Prediction Application

Overview

This application predicts possible health risks using patient blood test values and Google Gemini AI.

Features

- Create Patient Record
- View Patient Record
- Update Patient Record
- Delete Patient Record
- AI Generated Health Remarks
- SQLite Database Storage

Technologies

- Python
- Flask
- SQLite
- HTML
- CSS
- Bootstrap
- Google Gemini API

Run Project

1. Install requirements

pip install -r requirements.txt

2. Add Gemini API Key

3. Run

python app.py

4. Open browser

http://127.0.0.1:5000
=======
 Health Risk Analyzer

AI-powered healthcare web application built using Flask, SQLite, and Google Gemini AI to manage patient records and generate health risk assessments.

🚀 Features

- Patient Registration System
- CRUD Operations (Create, Read, Update, Delete)
- AI Health Risk Prediction
- SQLite Database Integration
- Responsive User Interface
- Patient Health Records Dashboard

🛠️ Tech Stack

Frontend  : HTML, CSS, Bootstrap
Backend   : Flask (Python)
Database  : SQLite
AI Model  : Google Gemini AI

📂 Project Structure

HealthRisk-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── static/
│   └── style.css
│
└── templates/
    ├── index.html
    └── edit.html

⚙️ Installation

Clone the repository:

git clone https://github.com/Sanjana2508-shah/HealthRisk-Analyzer.git
cd HealthRisk-Analyzer

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

🧠 AI Prediction Workflow

Patient Data
     ↓
Flask Backend
     ↓
Google Gemini AI
     ↓
Health Risk Analysis
     ↓
Results Display

📊 Patient Parameters

- Date of Birth (DOB)
- Glucose Level
- Haemoglobin Level
- Cholesterol Level
- Email Address

🎯 Future Improvements

- User Authentication
- PDF Report Generation
- Email Notifications
- Advanced Health Analytics
- Doctor Dashboard

👩‍💻 Author

Sanjana Kumari Shah
B.Tech Information Technology (2025)
>>>>>>> 3833dddf645d33e8dd5de9b2cadb4bb67b2a7db4
<<<<<<< HEAD
>>>>>>> 627989d956bc58cb5888bb7aa878bb64e9dbd619
=======
>>>>>>> 627989d956bc58cb5888bb7aa878bb64e9dbd619
