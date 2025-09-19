from flask import Flask, request, render_template_string
from datetime import datetime
try:
    from zoneinfo import ZoneInfo
except Exception:
    ZoneInfo = None

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Московское время и ваш IP</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">
  <style>
    :root{
      --bg1: #0f172a;
      --bg2: #0b1220;
      --accent: linear-gradient(90deg,#7c3aed,#06b6d4);
    }
    *{box-sizing:border-box;font-family:Inter,system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial;}
    html,body{height:100%;margin:0;
      background:linear-gradient(180deg,var(--bg1),var(--bg2));
      color:#e6eef8}
    .wrap{min-height:100vh;display:flex;align-items:center;justify-content:center;padding:40px}
    .card{width:100%;max-width:600px;background:rgba(255,255,255,0.03);
          border-radius:20px;padding:28px;box-shadow:0 8px 30px rgba(2,6,23,0.6);backdrop-filter: blur(6px);}
    .header{display:flex;align-items:center;gap:14px}
    .logo{
      width:62px;height:62px;border-radius:12px;
      background:var(--accent);
      display:flex;align-items:center;justify-content:center;
      font-weight:800;color:white;font-size:22px;
    }
    h1{margin:0;font-weight:700;font-size:20px}
    .grid{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:20px}
    .info{background:rgba(255,255,255,0.02);
          padding:18px;border-radius:12px;border:1px solid rgba(255,255,255,0.05);}
    .label{font-size:12px;color:#b6d0ff;text-transform:uppercase;letter-spacing:0.08em}
    .value{font-size:20px;font-weight:600;margin-top:8px}
    .footer{margin-top:20px;text-align:center;font-size:14px;font-weight:600;color:orange}
    @media (max-width:600px){ .grid{grid-template-columns:1fr} }
  </style>
</head>
<body>
  <div class="wrap">
    <div class="card">
      <div class="header">
        <div class="logo">MSK</div>
        <div>
          <h1>Московское время и ваш IP</h1>
        </div>
      </div>

      <div class="grid">
        <div class="info" aria-live="polite">
          <div class="label">Московское время</div>
          <div class="value" id="msk-time">{{ server_time }}</div>
        </div>
        <div class="info" aria-live="polite">
          <div class="label">Ваш IP</div>
          <div class="value">{{ client_ip }}</div>
        </div>
      </div>

      <div class="footer">
        WebSite By Andey GubS
      </div>
    </div>
  </div>

<script>
  (function(){
    const el = document.getElementById('msk-time');
    let fmt;
    try {
      fmt = new Intl.DateTimeFormat('ru-RU', {
        timeZone: 'Europe/Moscow',
        hour: '2-digit', minute: '2-digit', second: '2-digit',
        day: '2-digit', month: '2-digit', year: 'numeric',
        hour12: false
      });
    } catch (e) { fmt = null; }

    function tick(){
      const now = new Date();
      if (fmt) {
        el.textContent = fmt.format(now) + ' (MSK)';
      } else {
        el.textContent = now.toLocaleString('ru-RU');
      }
    }
    tick();
    setInterval(tick, 1000);
  })();
</script>
</body>
</html>
"""

def get_client_ip(req):
    xff = req.headers.get('X-Forwarded-For', '') or req.environ.get('HTTP_X_FORWARDED_FOR', '')
    if xff:
        return xff.split(',')[0].strip()
    return req.remote_addr or 'неизвестно'

@app.route('/')
def index():
    client_ip = get_client_ip(request)
    if ZoneInfo is not None:
        msk = datetime.now(ZoneInfo("Europe/Moscow")).strftime("%d.%m.%Y %H:%M:%S")
    else:
        msk = datetime.utcnow().strftime("%d.%m.%Y %H:%M:%S")
    return render_template_string(TEMPLATE, client_ip=client_ip, server_time=msk)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)

