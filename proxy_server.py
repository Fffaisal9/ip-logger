from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/get_location', methods=['GET'])
def get_location():
    ip = request.args.get('ip')
    if not ip:
        return jsonify({"error": "IP address is required"}), 400

    try:
        res = requests.get(f"http://ip-api.com/json/{ip}?fields=66846719")
        return jsonify(res.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
