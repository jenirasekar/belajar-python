from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    web_title = 'Halaman Utama'
    return render_template('home.html', data = web_title)

@app.route("/about")
def about():
    web_title = "Halaman About"
    return render_template('about.html', data = web_title)

@app.route("/usia", methods=['GET', 'POST'])
def usia():
    if request.method == 'POST':
        tahun_lahir = int(request.form['tahun_lahir'])
        tahun_sekarang = 2025
        usia = tahun_sekarang - tahun_lahir
        return render_template('cek_usia.html', data = usia)
    return render_template('cek_usia.html', usia = None)
    