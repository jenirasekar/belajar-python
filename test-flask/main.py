from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "<p>ini home ges</p><br/><a href='/about'> masuk ke about page</a>"

@app.route("/about")
def about():
    return "<p>about!</p>"