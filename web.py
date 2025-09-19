
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()

    current_time = now.strftime("%d/%m/%y %H:%M:%S")
    return current_time
@app.route('/')
def addres():
    return 'IP: '+ request.remote_addr
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
