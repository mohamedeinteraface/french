from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/levels")
def levels():
    return "<h1>صفحة المستويات</h1>"

@app.route("/grammar")
def grammar():
    return "<h1>صفحة القواعد</h1>"

@app.route("/vocab")
def vocab():
    return "<h1>صفحة المفردات</h1>"

@app.route("/exercises")
def exercises():
    return "<h1>صفحة التمارين</h1>"

if __name__ == "__main__":
    app.run(debug=True)
