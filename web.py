
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr
    return f"Ваш IP-адрес: {user_ip}"
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
