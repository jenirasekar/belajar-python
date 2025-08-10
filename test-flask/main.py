from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    web_title = "Halaman Utama"
    return f"<p>{ web_title }</p><br/><a href='/about'>masuk ke about page</a>"

@app.route("/about")
def about():
    web_title = "Halaman About"
    return f"<p>{ web_title }</p><br/><a href='/'>kembali</a>"