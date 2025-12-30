from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>App Wildan dah LIVE! 🚀</h1><p>Deploy guna CI/CD GitHub Actions & Docker.</p>"

if __name__ == "__main__":
    # Ini supaya app kau boleh ikut port yang cloud bagi nanti
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
