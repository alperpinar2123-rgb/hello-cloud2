from flask import Flask, render_template_string, request

import os

import psycopg2

app = Flask(__name__)

#Render in otomatik tanımladığı veritabanı bağlantı bilgisi (DATABASE_URL ortam değişkeni)

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://hello_kloud2_db_user:UxLdeEE4UxcNel2MieU1ZPlQ3NcexdXf@dpg-d3tjheggjchc73fan2ng-a.oregon-postgres.render.com/hello_kloud2_db")

#HTML ŞABLONU (tek sayfada form + liste)

HTML = """

<!doctype html>

<html>

<head>

<title>Buluttan Selam!</title>

<style>

body font-family: Arial: text-align: center: nadding: 50px: background: #eef7f3: }

h1 { color: #333; }

form (margin: 20px auto; }

Input { padding: 10px; font-size: 16px; }

button {padding: 10px 15px; background: #4CAF50; color: white; border: none; border-radius: 6px; cursor:

ul { list-style: none; padding: 0; ]

li {background: white; margin: 5px auto; width: 200px; padding: 8px; border-radius: 5px; }

</style>

</head>

<body>

<h1> Buluttan Selam!</h1>

<p>Adını yaz, selamını bırak</p>

<form method="POST">

<input type="text" name="isim" placeholder="Adını yaz"required>

<button type="submit">Gönder</button>

</form>

<h3>Ziyaretçiler:</h3>

<ul>

(for ad in isimler %)

<li>{{ ad })</li>

{% endfor %)

</ul>

</body>

</html>
"""
def connect_db():

conn = psycopg2.connect(DATABASE_URL)

return conn

@app.route("/", methods=["GET", "POST"])

def index():

conn = connect_db()

cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS ziyaretciler (id SERIAL PRIMARY KEY, isim TEXT)")

if request.method == "POST":

isim = request.form.get("isim")

if isim:

cur.execute("INSERT INTO ziyaretciler (isim) VALUES (%s)", (isim,))

conn.commit()

cur.execute("SELECT isim FROM ziyaretciler ORDER BY id DESC LIMIT 10")

isimler [row[0] for row in cur.fetchall()]

cur.close()

conn.close()

return render_template_string(HTML, isimler-isimler)

if _name_ == "main":

app.run(host="0.0.0.0", port=5000)
