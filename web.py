
from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")  
    client_ip = request.remote_addr 

    return f"Текущее время: {current_time}<br>IP: {client_ip}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)

