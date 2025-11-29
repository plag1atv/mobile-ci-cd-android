from flask import Flask, request, jsonify
import sys

app = Flask(__name__)

@app.route("/log", methods=["POST"])
def log():
    data = request.get_json() or {}
    # Для простоты просто печатаем событие в stdout
    print(f"LOG_EVENT: {data}", file=sys.stdout, flush=True)
    return jsonify({"status": "logged"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)