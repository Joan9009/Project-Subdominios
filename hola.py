from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def hola():
    return render_template("index.html")

@app.route("/subdominios")
def mostrar_subdominios():
    with open('data/subdominios.json', 'r') as f:
        subdominios = json.load(f)
    return render_template("subdominios.html", subdominios=subdominios)

if __name__ == "__main__":
    app.run(debug=True)
