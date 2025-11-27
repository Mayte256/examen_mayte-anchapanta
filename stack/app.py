from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Vinueza App</title>
    <style>
        body { margin:0; font-family:'Segoe UI',sans-serif; background:linear-gradient(135deg,#6a11cb,#2575fc); color:white; display:flex; height:100vh; justify-content:center; align-items:center;}
        .card { background: rgba(255,255,255,0.15); padding:40px; border-radius:18px; backdrop-filter:blur(10px); text-align:center; box-shadow:0 8px 18px rgba(0,0,0,0.3); width:450px; animation:fadeIn 1s ease-in-out;}
        .card h1{margin:0;font-size:2.2rem;}
        .card p{font-size:1.2rem;margin-top:10px;}
        .btn{display:inline-block;background:#00e6b8;color:#1f1f1f;padding:12px 20px;margin-top:20px;border-radius:8px;text-decoration:none;font-weight:bold;transition:0.3s;}
        .btn:hover{background:#00b894;}
        @keyframes fadeIn{from{opacity:0;transform:translateY(20px);}to{opacity:1;transform:translateY(0);}}
    </style>
</head>
<body>
    <div class="card">
        <h1>Vinueza App</h1>
        <p>Aplicación funcionando correctamente con diseño modernoooo.</p>
        <a href="/api" class="btn">Ver API JSON</a>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

@app.route("/api")
def api_info():
    return jsonify({
        "status": "ok",
        "message": "API funcionando correctamente",
        "version": "1.0"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1003)
