from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='static', template_folder='.')

@app.route("/")
def index():
    return render_template("index.html")

# لتقديم الملفات الصوتية والصور (Flask يقدّم static بشكل تلقائي)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == "__main__":
    app.run(debug=True)

