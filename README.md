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