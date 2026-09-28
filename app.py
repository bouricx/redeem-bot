import os
from flask import Flask, render_template, request, jsonify
from scraper import redeem_key

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/redeem", methods=["POST"])
def api_redeem():
    data = request.get_json(silent=True) or {}
    key = data.get("key", "").strip()

    if not key:
        return jsonify(ok=False, error="กรุณาใส่คีย์ก่อน"), 400

    try:
        result = redeem_key(key)
    except Exception as e:
        return jsonify(ok=False, error=str(e)), 502

    return jsonify(ok=True, data=result)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
