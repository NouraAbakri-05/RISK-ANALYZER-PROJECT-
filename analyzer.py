import json

DEVICES_FILE = "devices.json"

def load_devices():
    try:
        with open(DEVICES_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def get_trusted_ips():
    devices = load_devices()
    return [d["ip"] for d in devices]


def analyze_log(log):
    score = 0
    reasons = []

    failed_attempts = log.get("failed_attempts", 0)
    ip = log.get("ip", "")
    status = log.get("status", "")

    trusted_ips = get_trusted_ips()  

    # Rule 1: brute force
    if failed_attempts >= 3:
        score += 0.4
        reasons.append("Too many failed attempts")

    # Rule 2: unknown IP
    if ip not in trusted_ips:
        score += 0.3
        reasons.append("Unknown IP address")

    # Rule 3: failed login
    if status == "failed":
        score += 0.3
        reasons.append("Login failed")

    # final level
    if score < 0.3:
        level = "low"
    elif score < 0.7:
        level = "medium"
    else:
        level = "high"

    return {
        "risk_score": round(score, 2),
        "risk_level": level,
        "reasons": reasons
    }