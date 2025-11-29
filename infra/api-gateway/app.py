from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

ANDROID_BUILD_SERVICE_URL = os.getenv("ANDROID_BUILD_SERVICE_URL", "http://android-build-service:5001")
LOG_SERVICE_URL = os.getenv("LOG_SERVICE_URL", "http://log-service:5002")

@app.route("/status")
def status():
    # Получаем данные от сервиса сборки
    try:
        build_info = requests.get(f"{ANDROID_BUILD_SERVICE_URL}/build/info", timeout=2).json()
    except Exception as e:
        build_info = {"error": str(e)}

    # Логируем обращение
    try:
        requests.post(f"{LOG_SERVICE_URL}/log", json={"event": "status_checked"}, timeout=2)
        log_status = "logged"
    except Exception as e:
        log_status = f"log_error: {e}"

    return jsonify({
        "api": "ok",
        "build_service": build_info,
        "log_status": log_status
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)