from flask import Flask, jsonify, render_template_string
import psutil
import time

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>System Health Checker</title>
    <style>
        body {
            font-family: Arial;
            background: #f4f7fb;
            text-align: center;
            padding: 30px;
        }

        h1 {
            margin-bottom: 30px;
        }

        .container {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
        }

        .card {
            background: white;
            padding: 20px;
            width: 220px;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }

        .value {
            font-size: 32px;
            color: blue;
            margin-top: 10px;
        }
    </style>
</head>
<body>

<h1>Automated System Health Checker</h1>

<div class="container">
    <div class="card">
        <h2>CPU Usage</h2>
        <div class="value" id="cpu">0%</div>
    </div>

    <div class="card">
        <h2>Memory Usage</h2>
        <div class="value" id="memory">0%</div>
    </div>

    <div class="card">
        <h2>Disk Usage</h2>
        <div class="value" id="disk">0%</div>
    </div>

    <div class="card">
        <h2>Uptime</h2>
        <div class="value" id="uptime">0 mins</div>
    </div>
</div>

<script>
async function fetchData() {
    const response = await fetch('/data');
    const data = await response.json();

    document.getElementById('cpu').innerText = data.cpu + '%';
    document.getElementById('memory').innerText = data.memory + '%';
    document.getElementById('disk').innerText = data.disk + '%';
    document.getElementById('uptime').innerText = data.uptime;
}

setInterval(fetchData, 2000);
fetchData();
</script>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/data')
def data():
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_minutes = int(uptime_seconds // 60)

    return jsonify({
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
        "uptime": f"{uptime_minutes} mins"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
