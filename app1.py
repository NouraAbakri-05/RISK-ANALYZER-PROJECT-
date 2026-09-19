import streamlit as st
import requests
import pandas as pd
import random

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="IoT Security Shield", layout="wide")

# ================= STYLE =================
st.markdown("""
<style>

body {
    background-color: #0b1220;
    color: white;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111b2e;
}

/* CARD STYLE */
.card {
    background: linear-gradient(135deg, #1f2a44, #121c33);
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.5);
    border: 1px solid rgba(255,255,255,0.05);
}

/* TITLE */
h1, h2, h3 {
    color: #e5e7eb;
}

/* METRIC BOX */
.metric-box {
    background: #162238;
    padding: 20px;
    border-radius: 14px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.4);
}

.metric-title {
    font-size: 14px;
    color: #9ca3af;
}

.metric-value {
    font-size: 28px;
    font-weight: bold;
    color: #60a5fa;
}

</style>
""", unsafe_allow_html=True)


# ================= BACKEND =================
def get_logs():
    try:
        return requests.get(f"{API_URL}/logs").json()
    except:
        return []

def get_devices():
    try:
        return requests.get(f"{API_URL}/devices").json()
    except:
        return []


# ================= SIDEBAR =================
st.sidebar.title("IoT Security Panel")

menu = st.sidebar.radio("", [
    "Home",
    "Add Device",
    "Devices",
    "Live Security",
    "Logs"
])


# ================= HOME =================
if menu == "Home":
    st.title("Security Overview")

    logs = get_logs()
    devices = get_devices()

    total_devices = len(devices)
    total_logs = len(logs)
    high_risk = len([l for l in logs if l.get("risk_level") == "high"])
    medium_risk = len([l for l in logs if l.get("risk_level") == "medium"])
    low_risk = len([l for l in logs if l.get("risk_level") == "low"])

    # ===== STATS CARDS =====
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-title">Devices</div>
            <div class="metric-value">{total_devices}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-title">Total Logs</div>
            <div class="metric-value">{total_logs}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-title">High Risk</div>
            <div class="metric-value">{high_risk}</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-title">Medium Risk</div>
            <div class="metric-value">{medium_risk}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ===== CHART =====
    if logs:
        df = pd.DataFrame(logs)
        st.line_chart(df["risk_score"])
    else:
        st.info("No attacks yet")


# ================= ADD DEVICE =================
elif menu == "Add Device":
    st.header("Add Device")

    name = st.text_input("Device Name")
    password = st.text_input("Password", type="password")

    device_type = st.selectbox("Device Type", ["camera", "door", "sensor", "alarm"])

    auto_ip = f"192.168.1.{random.randint(50, 250)}"
    st.info(f"Auto IP: {auto_ip}")

    if st.button("Save Device"):
        device = {
            "id": name,
            "ip": auto_ip,
            "password": password,
            "device_type": device_type
        }

        requests.post(f"{API_URL}/add-device", json=device)

        st.success("Device added")


# ================= DEVICES =================
elif menu == "Devices":
    st.header("Devices List")

    devices = get_devices()

    if devices:
        st.dataframe(pd.DataFrame(devices), use_container_width=True)
    else:
        st.warning("No devices yet")


# ================= LIVE =================
elif menu == "Live Security":
    st.title("Live Monitoring")

    logs = get_logs()

    if not logs:
        st.info("No attacks yet")
    else:
        for log in logs[::-1][:10]:

            st.markdown(f"""
            <div class="card">
                <h3>{log['device_id']}</h3>
                <p><b>IP:</b> {log['ip']}</p>
                <p><b>Attempts:</b> {log['failed_attempts']}</p>
                <p><b>Risk:</b> {log['risk_level']}</p>
                <p><b>Score:</b> {log['risk_score']}</p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("---")


# ================= LOGS =================
elif menu == "Logs":
    logs = get_logs()
    st.dataframe(pd.DataFrame(logs))