# 🔐 IoT Device Authentication Risk Analyzer

A cybersecurity monitoring system developed as a **five-member academic team project** to simulate and analyze authentication activity in an IoT environment.

The project combines a **FastAPI backend**, a **rule-based risk analysis engine**, and interactive **Streamlit interfaces** to register IoT devices, simulate authentication scenarios, calculate security risk scores, and monitor suspicious activity.

## 🎯 Project Objective

IoT devices can be exposed to authentication threats such as repeated login attempts, access from unknown IP addresses, and brute-force attempts.

This project demonstrates a lightweight security monitoring approach that can:

- Register trusted IoT devices
- Simulate normal and suspicious authentication activity
- Analyze authentication events
- Calculate a risk score for each event
- Classify events as Low, Medium, or High risk
- Identify the reasons contributing to the risk
- Store authentication logs
- Provide security monitoring through an interactive dashboard

## 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │   Attack Simulator   │
                    │      Streamlit       │
                    └──────────┬───────────┘
                               │
                               │ Authentication Event
                               ▼
                    ┌──────────────────────┐
                    │    FastAPI Backend   │
                    │      /analyze        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Risk Analyzer     │
                    │   Rule-Based Engine  │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 ▼                           ▼
          ┌─────────────┐             ┌─────────────┐
          │  logs.json  │             │devices.json │
          └──────┬──────┘             └─────────────┘
                 │
                 ▼
          ┌──────────────────────┐
          │  Security Dashboard  │
          │      Streamlit       │
          └──────────────────────┘
```

## 🛡️ Risk Analysis Engine

The system uses a transparent **rule-based scoring mechanism** to evaluate authentication events.

| Security Condition | Risk Contribution |
|---|---:|
| 3 or more failed attempts | +0.4 |
| Unknown IP address | +0.3 |
| Failed login | +0.3 |

The accumulated score determines the final security level:

| Risk Score | Classification |
|---|---|
| `< 0.3` | Low |
| `0.3 – < 0.7` | Medium |
| `≥ 0.7` | High |

The analyzer also returns the specific reasons that contributed to the calculated risk score.

## ⚔️ Attack Simulator

The project includes a dedicated **Streamlit attack simulator** for generating different authentication scenarios and sending them to the FastAPI backend for analysis.

Supported scenarios include:

- **Normal Access** — successful authentication using the trusted device IP
- **Password Guessing** — repeated failed authentication attempts
- **Brute Force** — multiple failed attempts originating from an untrusted IP
- **IP Spoof Simulation** — authentication activity using a generated external IP

The simulator allows the user to select a registered IoT device as the target and displays the resulting:

- Risk score
- Risk level
- Detection reasons

## 📊 Security Dashboard

The main Streamlit interface provides a centralized security monitoring dashboard.

### Main Features

- Security overview
- Registered device count
- Total authentication log count
- High-risk event count
- Medium-risk event count
- Risk-score visualization
- IoT device registration
- Registered device listing
- Recent security event monitoring
- Authentication log inspection

## 🔌 REST API

The backend is implemented using **FastAPI** and provides the following endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| `POST` | `/analyze` | Analyze an authentication event and store its result |
| `POST` | `/add-device` | Register a trusted IoT device |
| `GET` | `/devices` | Retrieve registered IoT devices |
| `GET` | `/logs` | Retrieve authentication analysis logs |

FastAPI also automatically provides interactive **Swagger API documentation**.

## 🖥️ Screenshots

### 🔐 Security Dashboard

![IoT Security Dashboard](screenshots/dashboard.png)

### ⚔️ Attack Simulator

![Attack Simulator](screenshots/attack_simulator.png)

### 🔌 FastAPI Documentation

![FastAPI Swagger Documentation](screenshots/api_docs.png)

## 🛠️ Technologies

### Programming

- Python

### Backend

- FastAPI
- Pydantic
- Uvicorn

### Dashboard & Simulation

- Streamlit
- Pandas
- Requests

### Data Storage

- JSON

### Security Concepts

- IoT authentication
- Authentication monitoring
- Risk scoring
- Brute-force detection
- Failed-login monitoring
- Trusted IP verification
- Attack simulation

## 📁 Project Structure

```text
iot-authentication-risk-analyzer/
│
├── analyzer.py
├── main.py
├── app1.py
├── attack_simulator.py
│
├── devices.json
├── logs.json
│
├── requirements.txt
├── .gitignore
│
├── screenshots/
│   ├── dashboard.png
│   ├── attack_simulator.png
│   └── api_docs.png
│
└── README.md
```

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/NouraAbakri-05/iot-authentication-risk-analyzer.git
```

Navigate to the project directory:

```bash
cd iot-authentication-risk-analyzer
```

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

## ▶️ Running the Project

The complete system consists of **three running components**.

### 1️⃣ Start the FastAPI Backend

Open a terminal in the project directory and run:

```bash
python -m uvicorn main:app --reload
```

The API will run locally on:

```text
http://127.0.0.1:8000
```

FastAPI Swagger documentation is available at:

```text
http://127.0.0.1:8000/docs
```

### 2️⃣ Start the Security Dashboard

Keep the backend running and open a second terminal:

```bash
python -m streamlit run app1.py
```

The Streamlit security dashboard will open in the browser.

### 3️⃣ Start the Attack Simulator

Open a third terminal:

```bash
python -m streamlit run attack_simulator.py
```

The attack simulator will run as a separate Streamlit interface.

> **Note:** Register at least one IoT device from the main dashboard before launching an authentication simulation.

## 🔄 System Workflow

```text
Register IoT Device
        ↓
Store Trusted Device
        ↓
Select Target Device
        ↓
Choose Authentication Scenario
        ↓
Generate Authentication Event
        ↓
Send Event to FastAPI
        ↓
Analyze Security Conditions
        ↓
Calculate Risk Score
        ↓
Determine Risk Level
        ↓
Store Authentication Log
        ↓
Display Results on Dashboard
```

## 🔍 Example Risk Analysis

For example, an authentication event with:

```text
Failed attempts: 6
IP address: Unknown
Login status: Failed
```

would trigger all three security rules:

```text
Failed attempts ≥ 3     → +0.4
Unknown IP              → +0.3
Failed login            → +0.3
--------------------------------
Final Risk Score         → 1.0
Risk Level               → HIGH
```

The corresponding detection reasons are returned by the API and stored with the authentication log.

## 🚀 Future Improvements

Possible extensions of the project include:

- Database integration instead of JSON-based storage
- Authentication and authorization for the dashboard
- Real-time security event streaming
- Configurable risk rules and thresholds
- IP reputation analysis
- Automated security alerts and notifications
- Integration with physical IoT devices
- Machine-learning-based anomaly detection
- More advanced attack scenarios
- Docker containerization and deployment

## 🎓 Academic Information

This project was developed as a **team academic project** within the Computer Engineering and Embedded Systems program.

**Module:** Advanced Python Programming  
**Program:** Computer Engineering and Embedded Systems Engineering  
**Academic Year:** 2025/2026  
**University:** Ibn Zohr University — Faculty of Sciences, Agadir

The project explores the intersection of **Python development, IoT, backend systems, and cybersecurity** through IoT authentication monitoring and attack simulation.

## 👥 Team Members

- **Noura Abakri**
- **Salma Boumart**
- **Bahiya El Hajali**
- **Fatim-Zahra Bouharroud**
- **Khadija Anezzjar**

---

### 🔐 IoT Device Authentication Risk Analyzer

Academic team project — **Advanced Python Programming • 2025/2026**
