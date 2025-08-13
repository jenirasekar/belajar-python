from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    web_title = 'Halaman Utama'
    return render_template('home.html', data = web_title)

@app.route("/about")
def about():
    web_title = "Halaman About"
    return render_template('about.html', data = web_title)