from flask import Flask, jsonify
import time

app = Flask(__name__)

# Счетчик запросов к /time
time_requests_count = 0

@app.route('/time')
def get_time():
    global time_requests_count
    time_requests_count += 1
    return jsonify({"time": int(time.time())})

@app.route('/metrics')
def get_metrics():
    return jsonify({"count": time_requests_count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
