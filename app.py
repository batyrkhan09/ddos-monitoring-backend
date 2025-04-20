import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from detector import detect_ddos
from traffic_monitor import get_traffic_stats, set_mode, get_current_mode

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["GET"])
def analyze():
    stats = get_traffic_stats()
    result = detect_ddos(stats)
    return jsonify(result)

@app.route("/mode", methods=["POST", "GET"])
def monitoring_mode():
    if request.method == "POST":
        data = request.get_json()
        mode = data.get("mode")
        if mode == "test":
            set_mode(True)
            return jsonify({"status": "ok", "mode": "test"})
        elif mode == "real":
            set_mode(False)
            return jsonify({"status": "ok", "mode": "real"})
        else:
            return jsonify({"status": "error", "message": "Unknown mode"}), 400
    else:
        return jsonify({"mode": get_current_mode()})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 Flask сервер запущен на порту {port}")
    app.run(host="0.0.0.0", port=port)
