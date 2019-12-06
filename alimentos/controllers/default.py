from alimentos import app
from flask.templating import render_template


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/cadastro")
def cadastro():
    return render_template('cadastro.html')