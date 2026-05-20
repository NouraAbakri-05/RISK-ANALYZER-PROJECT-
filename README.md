IoT Device Authentication Risk Analyzer

An interactive cybersecurity monitoring system designed to analyze authentication activities of IoT devices, detect suspicious login attempts, simulate attacks, and calculate authentication risk levels in real time.

📌 Project Overview

The rapid growth of IoT (Internet of Things) devices has introduced major security challenges, especially in authentication systems.
This project aims to provide a lightweight and interactive solution for monitoring authentication activities and detecting potential cyberattacks.

The application:

Monitors IoT authentication logs
Detects suspicious activities
Simulates cyberattacks
Calculates dynamic risk scores
Displays results through a real-time dashboard
🚀 Features
🔐 Authentication Monitoring
Track login attempts from IoT devices
Analyze authentication logs in real time
Detect failed login attempts
⚠️ Risk Analysis
Calculate authentication risk scores
Classify risks into:
Low Risk
Medium Risk
High Risk
🛡️ Attack Simulation
Simulate brute-force attacks
Simulate unauthorized access attempts
Test system detection capabilities
📊 Interactive Dashboard
Real-time monitoring interface
Security log visualization
Device management system
Alert display for suspicious activities
🏗️ System Architecture
+----------------------+
|   Streamlit Dashboard |
|  (User Interface)    |
+----------+-----------+
           |
           | HTTP Requests
           v
+----------------------+
|      FastAPI API     |
|   (Backend Server)   |
+----------+-----------+
           |
           v
+----------------------+
| Risk Analysis Module |
| Authentication Logs  |
| Risk Score Engine    |
+----------+-----------+
           |
           v
+----------------------+
|     JSON Storage     |
| Devices & Security   |
|       Logs           |
+----------------------+
🧰 Technologies Used
Python
FastAPI
Streamlit
Pandas
Requests
JSON
📂 Project Structure
iot-device-authentication-risk-analyzer/
│
├── backend/
│   ├── main.py
│   ├── risk_analysis.py
│   ├── api_routes.py
│   └── logs/
│
├── dashboard/
│   ├── app.py
│   └── components/
│
├── simulator/
│   ├── attack_simulator.py
│
├── data/
│   ├── devices.json
│   ├── auth_logs.json
│
├── requirements.txt
└── README.md
⚙️ Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/iot-device-authentication-risk-analyzer.git
cd iot-device-authentication-risk-analyzer
2️⃣ Create a Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
Linux / macOS
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Running the Project
Start the Backend Server
uvicorn main:app --reload

The backend API will run on:

http://127.0.0.1:8000
Launch the Streamlit Dashboard
streamlit run app.py
Run the Attack Simulator
python attack_simulator.py
📈 Risk Analysis Workflow
Authentication Attempt
        ↓
Log Collection
        ↓
Risk Analysis Module
        ↓
Risk Score Calculation
        ↓
Risk Classification
        ↓
Dashboard Visualization
📊 Example Risk Classification
Risk Score	Classification
0 - 30	Low Risk
31 - 70	Medium Risk
71 - 100	High Risk
🔮 Future Improvements
Machine Learning anomaly detection
Multi-Factor Authentication (MFA)
Cloud deployment
Real IoT device integration
Database integration (MongoDB / MySQL)
Email and SMS alerts
Advanced analytics dashboard
👥 Team Members
Noura Abakri
Salma Boumart
Bahiya El Hajali
Fatim-Zahra Bouharroud
Khadija Anezzjar
                  🎓 Academic Information
                  
                  Module: Advanced Python Programming
                  Program: Computer Engineering and Embedded Systems Engineering
                  Academic Year: 2025/2026
