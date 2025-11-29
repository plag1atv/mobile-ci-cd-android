from flask import Flask, jsonify

app = Flask(__name__)

# В реальности тут можно запускать Gradle и возвращать реальные данные,
# но для учебной задачи эмулируем информацию о сборке.
@app.route("/build/info")
def build_info():
    return jsonify({
        "status": "success",
        "app": "CiCdDemoApp",
        "version": "1.0.0",
        "last_build": "handled by CI/CD pipeline"
    })

if __name__ == "__main__":
    # Важно: host="0.0.0.0", чтобы сервис был доступен извне контейнера
    app.run(host="0.0.0.0", port=5001)