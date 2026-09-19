from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

LOG_FILE = "logs.json"
DEVICES_FILE = "devices.json"


# ================= LOAD / SAVE LOGS =================
def load_logs():
    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_log(log):
    logs = load_logs()
    logs.append(log)
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)


# ================= LOAD / SAVE DEVICES =================
def load_devices():
    try:
        with open(DEVICES_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_devices(devices):
    with open(DEVICES_FILE, "w") as f:
        json.dump(devices, f, indent=4)


# ================= MODELS =================
class Log(BaseModel):
    device_id: str
    device_type: str
    ip: str
    status: str
    failed_attempts: int
    timestamp: str


class Device(BaseModel):
    id: str
    ip: str
    password: str
    device_type: str = "unknown"


# ================= ANALYZE =================
from analyzer import analyze_log

@app.post("/analyze")
def analyze(log: Log):
    log_dict = log.dict()

    result = analyze_log(log_dict)

    log_dict["risk_score"] = result["risk_score"]
    log_dict["risk_level"] = result["risk_level"]
    log_dict["reasons"] = result["reasons"]

    save_log(log_dict)

    return result


# ================= DEVICES =================
@app.post("/add-device")
def add_device(device: Device):
    devices = load_devices()
    devices.append(device.dict())
    save_devices(devices)
    return {"message": "device added"}


@app.get("/devices")
def get_devices():
    return load_devices()


@app.get("/logs")
def get_logs():
    return load_logs()