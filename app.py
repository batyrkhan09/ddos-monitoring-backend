from flask import Flask, jsonify, request
from flask_cors import CORS
from detector import detect_ddos
from traffic_monitor import get_traffic_stats, set_mode

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["GET"])
def analyze():
    stats = get_traffic_stats()
    result = detect_ddos(stats)
    return jsonify(result)

@app.route("/mode", methods=["POST"])
def set_monitoring_mode():
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

if __name__ == "__main__":
    print("🚀 Flask сервер запущен на http://127.0.0.1:5000")
    app.run(debug=True)


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
        from traffic_monitor import get_current_mode
        return jsonify({"mode": get_current_mode()})
