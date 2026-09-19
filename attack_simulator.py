import streamlit as st
import requests
import random
from datetime import datetime

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Attack Simulator", layout="centered")

st.title("Attack Simulator")

# ================= LOAD DEVICES =================
def load_devices():
    try:
        return requests.get(f"{API_URL}/devices").json()
    except:
        return []

devices = load_devices()

if len(devices) == 0:
    st.warning("No devices available. Please add devices first.")
    st.stop()

device_names = [d["id"] for d in devices]

selected = st.selectbox("Target Device", device_names)

device = next(d for d in devices if d["id"] == selected)

st.write("Target IP:", device["ip"])

# ================= ATTACK TYPE =================
attack_type = st.selectbox("Attack Type", [
    "normal_access",
    "password_guess",
    "bruteforce",
    "ip_spoof"
])

# ================= MODE =================
mode = st.radio("Mode", ["Normal User", "Hacker"])

# ================= IP LOGIC =================
if mode == "Normal User":
    fake_ip = device["ip"]
    st.success(f"Using trusted IP: {fake_ip}")
else:
    generated_ip = f"10.0.0.{random.randint(1,255)}"

    use_custom_ip = st.checkbox("Use custom attacker IP")

    if use_custom_ip:
        fake_ip = st.text_input("Attacker IP", value=generated_ip)
    else:
        fake_ip = generated_ip
        st.warning(f"Hacker IP: {fake_ip}")

# ================= ATTEMPTS =================
failed_attempts = st.slider("Failed Attempts", 0, 15, 2)

status = "failed"

# ================= LAUNCH ATTACK =================
if st.button("Launch Attack"):

    # 🔥 Behavior logic based on attack type
    if attack_type == "normal_access":
        fake_ip = device["ip"]
        status = "success"
        failed_attempts = 0

    elif attack_type == "password_guess":
        fake_ip = device["ip"]
        failed_attempts += 3

    elif attack_type == "bruteforce":
        fake_ip = f"10.0.0.{random.randint(1,255)}"
        failed_attempts += 6

    elif attack_type == "ip_spoof":
        fake_ip = f"172.16.0.{random.randint(1,255)}"
        failed_attempts += 2

    # ================= LOG =================
    log = {
        "device_id": device["id"],
        "device_type": device.get("device_type", "unknown"),
        "ip": fake_ip,
        "status": status,
        "failed_attempts": failed_attempts,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # ================= SEND TO API =================
    try:
        res = requests.post(f"{API_URL}/analyze", json=log).json()

        st.error("Attack sent to system")

        st.metric("Risk Score", res["risk_score"])
        st.metric("Risk Level", res["risk_level"])

        st.write("Reasons:")
        for r in res["reasons"]:
            st.write("-", r)

    except:
        st.error("Cannot connect to backend. Make sure FastAPI is running.")