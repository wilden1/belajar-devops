from flask import Flask
import redis
import os

app = Flask(__name__)

# 1. Sambung ke Redis (Mesti kat atas sebelum app.run)
cache = redis.Redis(host=os.environ.get('REDIS_HOST', 'localhost'), port=6379)

def get_hit_count():
    try:
        return cache.incr('hits')
    except redis.exceptions.ConnectionError:
        return "DATABASE_ERROR"

@app.route('/')
def hello():
    count = get_hit_count()
    if count == "DATABASE_ERROR":
        # Kalau database tak sambung, dia keluar ayat ni
        return "<h1>App Wildan dah POWER! 🔥</h1><p>Tapi database Redis belum manja dengan web ni.</p>"
    
    # Kalau berjaya, dia keluar jumlah visit
    return f"<h1>App Wildan dah POWER! 🔥</h1><p>Web ni dah dilawat sebanyak <b>{count}</b> kali.</p>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
